Title: Debugging tips in WebKitGTK+
Date: 2013-08-16 16:34
Author: Simón
Category: Tech
Tags: GNOME, Samsung, WebKit, WebKitGTK+
Slug: debugging-tips-in-webkitgtk
Status: published

Since WebKit2 has a UIProcess and a WebProcess (and could
potentially have other processes, take a look at the
[talk](http://www.superlectures.com/guadec2013/webkit2-and-you "WebKit2 and you")
that my former colleague
[Martin](http://abandonedwig.info/ "Abandoned Wig") gave at
[GUADEC](https://www.guadec.org/session/webkit2-and-you/ "WebKit2 and you")),
debugging WebKit2GTK+ it is a bit different from debugging WebKitGTK+:
if the crash happens in the WebProcess, how do you attach gdb to it?
Lately at Samsung we have been contributing quite actively, and since
debugging is part of our daily workflow, I thought it would be
interesting to share it.

In
[WebProcessMainGtk](http://trac.webkit.org/browser/trunk/Source/WebKit2/WebProcess/gtk/WebProcessMainGtk.cpp "WebProcessMainGtk"),
you can find:

    #ifndef NDEBUG
        if (g_getenv("WEBKIT2_PAUSE_WEB_PROCESS_ON_LAUNCH"))
            sleep(30);
    #endif

so you can export **WEBKIT2\_PAUSE\_WEB\_PROCESS\_ON\_LAUNCH**, which
will give you enough time to launch gdb and attach it to the WebProcess,
something I do with:

    gdb -p `pidof lt-WebKitWebProcess`

(I imagine you will need to provide the right PID if you happen to have
more than one lt-WebKitWebProcess instance running).

In the case that you are debugging the IPC communication between the
UIProcess and the WebProcess, you might want to launch both sides within
gdb, like

    Tools/jhbuild/jhbuild-wrapper --gtk run gdb --args WebKitBuild/Debug/Programs/MiniBrowser

These are the contents of my *.gdbinit*:

    set history filename .gdb_history
    set history save on
    set breakpoint pending on
    python
    import sys
    sys.path.insert(0, "/path/to/WebKit/Tools/gdb/")
    import webkit

The interesting bits there are saving the history, so you can
interactively search your past history for expressions, breakpoints or
whatever. The "set breakpoint pending on" is also nice if you save
breakpoints into a file, since they symbols are usually loaded  
dynamically later, and by default, when reading them with "source",
they won't be found and will be ignored instead of left pending.
Finally, WebKit provides a set of nice
[PrettyPrinters](http://trac.webkit.org/browser/trunk/Tools/gdb/webkit.py "Tools/gdb/webkit.py"),
so you can visually inspect the values of the most common data types.

Additionally, you might want to use

    (gdb) handle SIG34 nostop

since that is a signal often received that can be a bit annoying when
debugging.

You might face a similar challenge if you want to debug the LayoutTests:
how do you attach to the each process? Which are the binaries? What
environment variables do you need to set, and how do you deal with time
outs? And what if you are debugging a test that needs a web server?

In this case, you're probably interested in using

    Tools/jhbuild/jhbuild-wrapper --gtk run gdb --args WebKitBuild/Debug/Programs/WebKitTestRunner

also with the same **gdb -p \`pidof lt-WebKitWebProcess\`** additional
bit. But here we need to set some environment variables first (assuming
\$WEBKIT\_HOME is /path/to/WebKit):

    export TEST_RUNNER_TEST_PLUGIN_PATH=/path/to/.libs/
    export TEST_RUNNER_INJECTED_BUNDLE_FILENAME=/path/to/libTestRunnerInjectedBundle.la

The previous path is usually
**\$WEBKIT\_HOME/WebKitBuild/Debug/Libraries**. As for the web server
bit, I have an Apache server installed with one virtual host pointing to
a directory in my home directory, so I just put there the tests I need
to debug.

There are probably many different approaches to debugging: some people
use logs and printfs, because they are very familiar with the code and
already suspect where to start looking: for those, there are interesting
[channel
logs](http://webkitgtk.org/reference/webkitgtk/stable/webkit-environment.html "WebKit Environment")
that you can enable (although this has changed recently, take a look at
[r153736](https://trac.webkit.org/changeset/153736 "r153736"). Others
generate core files and do post-mortem debugging with gdb, and others do
live-debugging.

For additional references, check:

[WebKitGTK/Debugging](https://trac.webkit.org/wiki/WebKitGTK/Debugging "WebKitGTK/Debugging")  

[WebKitGTK/StartHacking](https://trac.webkit.org/wiki/WebKitGTK/StartHacking "WebKitGTK/StartHacking")  
[WebKit Environment Channel
Logs](http://webkitgtk.org/reference/webkitgtk/stable/webkit-environment.html "WebKit Environment")  

[PrettyPrinters](http://trac.webkit.org/browser/trunk/Tools/gdb/webkit.py "Tools/gdb/webkit.py")
