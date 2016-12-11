Title: Eclipse CDT indexer with autotools
Date: 2010-06-26 08:29
Author: Simón
Category: Tech
Tags: AM_SILENT_RULES, autotools, cdt, eclipse
Slug: eclipse-cdt-indexer-with-autotools
Status: published

Quick note on Eclipse's CDT indexer: when using it with a C autotools
project, it doesn't index headers and symbols with the AM\_SILENT\_RULES
activated.

    m4_ifdef([AM_SILENT_RULES],[AM_SILENT_RULES([yes])])

Commenting out the line let's Eclipse build its index, and then (it
looks like) there's no problem setting it back.

**UPDATE:** In the project properties, under the C/C++ Build page,
unclicking *Use default build command* and settingthe verbose mode for
Make,

    make V=1

does the trick, without the need to modify the *configure.ac*
