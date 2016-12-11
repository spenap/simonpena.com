Title: Memory leak detection in WebKitGTK+
Date: 2013-07-19 17:18
Author: Simón
Category: Tech
Tags: GNOME, Samsung, WebKit, WebKitGTK+
Slug: memory-leak-detection-in-webkitgtk
Status: published

[Mario](http://mariospr.org/about/) already shared last week
[the effort he has been lately putting on accessibility in
WebKit](http://mariospr.org/2013/07/12/im-going-to-guadec/ "I’m going to GUADEC!").
Besides that, and among other things, here at
[Samsung](http://www.samsung.com/) we have been also paying attention to
memory usage.

Two months ago, my colleague
[Brian](http://uk.linkedin.com/pub/brian-holt/5/100/b90 "Brian Holt")
[introduced a memory leak detection
tool](https://lists.webkit.org/pipermail/webkit-dev/2013-May/024915.html "[webkit-dev] [WIP][GTK] Memory leak detection")
for the GTK port in WebKit –although it could be easily extended to
other ports where valgrind is available. This tool hooks into
[run-webkit-tests](http://trac.webkit.org/browser/trunk/Tools/Scripts/run-webkit-tests),
and when the `--leaks` flag is used together with `--wrapper`, it
launches `DumpRenderTree` under valgrind, gets the leaks found and
parses them to generate a report.

There are some differences between how valgrind works and how the
leak-tool in Mac works, so while most of the design of
`run-webkit-tests` can be reused (hooking, for example, into
`--check_for_leaks` and `--print_leaks_summary`), there are some
additional pieces that need to be done, such as passing `--wrapper` as
well. Anyway, not having to pass `--wrapper` is in the roadmap as a
future improvement.

You can take a look at the patch
[here](https://bugs.webkit.org/show_bug.cgi?id=116317 "[GTK] Metabug: Memory leak detection using valgrind")
and contribute to the discussion with additional design ideas. Or simply
apply it locally and use it to detect leaks: Brian has already done that
with a set of the LayoutTests, [finding and fixing a number of
leaks](https://bugs.webkit.org/buglist.cgi?query_format=advanced&short_desc_type=allwordssubstr&short_desc=Leak%3A&long_desc_type=substring&long_desc=&bug_file_loc_type=allwordssubstr&bug_file_loc=&keywords_type=allwords&keywords=&bug_status=UNCONFIRMED&bug_status=NEW&bug_status=ASSIGNED&bug_status=REOPENED&bug_status=RESOLVED&bug_status=VERIFIED&bug_status=CLOSED&resolution=FIXED&resolution=INVALID&resolution=WONTFIX&resolution=LATER&resolution=REMIND&resolution=DUPLICATE&resolution=WORKSFORME&resolution=MOVED&resolution=---&emailreporter1=1&emailtype1=substring&email1=brian.holt%40samsung.com&emailassigned_to2=1&emailreporter2=1&emailcc2=1&emailtype2=substring&email2=&bugidtype=include&bug_id=&chfieldfrom=&chfieldto=Now&chfieldvalue=&cmdtype=doit&order=Reuse+same+sort+as+last+time&field0-0-0=noop&type0-0-0=noop&value0-0-0= "Issues identified with the memory leak detection tool.").
