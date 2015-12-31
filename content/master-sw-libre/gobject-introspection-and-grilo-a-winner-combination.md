Title: GObject Introspection and Grilo: A winner combination
Date: 2010-09-18 16:50
Author: Simón
Category: Máster SW Libre
Tags: GObject Introspection, Grilo, Igalia
Slug: gobject-introspection-and-grilo-a-winner-combination
Status: published

About GObject Introspection
---------------------------

A few days ago [Adrian Perez wrote about GObject
Introspection](http://blogs.igalia.com/aperez/2010/09/some-thoughts-and-code-around-gobject-introspection/#comments "Some thoughts (and code) around GObject-Introspection")
(abbreviated GI), explaining why it is gaining so much momentum. While
you're really encouraged to visit his blog entry to see the work he did
on [Lua's GI
bindings](http://gitorious.org/luigi "Dynamic Lua binding for GObject-Introspection"),
I'll take some of his words:

> In short, it *([GObject
> Introspection](http://live.gnome.org/GObjectIntrospection "GObject Introspection"))*
> works like this:
>
> -   Library developers add annotations to the documentation comments
>     of functions.
> -   The GI support tools generate XML and compiled API metadata.
> -   You have a library to use that metadata at runtime.
>
> The last thing is very interesting, especially the runtime usage of
> metadata... because it enables dynamic language bindings. This means
> that developers no longer have to build e.g. the Python bindings for
> themselves but just annotating the source code!

GObject Introspection in Grilo
------------------------------

As [Grilo](http://live.gnome.org/Grilo "Grilo")'s primary focus is to
allow application developers concentrate on making good user interfaces,
without having to deal with the low level stuff done at the framework
level, we consider very important providing them with the ability to use
their language of choice. At the same time, we'd like to avoid devoting
time to write manual bindings, and that's the reason we put so much
effort on GObject Introspection support: right now, if not all, most of
the API is accessible via GI, and we're working to fix the less
binding-friendly parts.

Building Grilo with GObject Introspection enabled
-------------------------------------------------

The best way to try Grilo from GI is, in my opinion, using
[jhbuild](http://live.gnome.org/Jhbuild "Jhbuild"). Clone it with

    git clone git://git.gnome.org/jhbuild

build and install it, and copy the configuration file provided
sample.jhbuildrc to \~/.jhbuilrc. The project page explains everything
in detail, from installation details to tweaking the configuration file,
but if you don't want to do it, that's fine. You'll probably need to
install the build prerequisites, by invoking

    $jhbuild bootstrap

To see the dependencies needed to get grilo and grilo plugins installed
you can type

    $jhbuild list grilo grilo-plugins

But to get the most from Grilo, you'd go for:

    $jhbuild build gtk+ pygobject grilo grilo-plugins

That will install grilo core and plugins, pygobject (which includes
Python's glue to use GObject Introspection, and has
gobject-introspection as a dependency) and Gtk+, needed to run the
grilo-test-ui sample done with GI. After a rather long build, you should
have an environment with Grilo installed with GI support.

From there, type

    $jhbuild shell

to enter the jhbuild environment and go to your Grilo's checkout
directory. If everything has worked fine, you should be able to do:

    $ python
    Python 2.5.2 (r252:60911, Aug  6 2010, 16:46:34)
    [GCC 4.4.3] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from gi.repository import Grl
    >>> Grl.init([])
    >>>

Under tools/python/ there's a grilo-test-ui.py program, which showcases
all the combined potential of GI and Grilo: run it with

    $python tools/python/grilo-test-ui.py

and enjoy :) (And then, start doing you own apps :D)
