Title: From Maevies to Butaca: a change for the better
Date: 2010-06-28 21:38
Author: Simón
Category: Butaca
Tags: decouple, detach, gitorious, maemo, maevies, split
Slug: from-maevies-to-butaca-a-change-for-the-better
Status: published

Maevies was born twice. The first one, around the end of October, had a
limited lifespan. The second one, a couple of months ago, was much more
promising. As I've just told, I'm following the same architectural
approach we have for [Jamp](http://gitorious.org/mswl2010/jamp), the
[Free Software Master](/category/master-sw-libre)'s
project. I was progressing fairly well, and feeling close to what I'd
call a 0.1 release, I wanted to provide Debian packages. I started
packaging the backend: another blog entry could be great to explain how
I solved the issues I found, but
[these](http://gitorious.org/butaca/butaca/commit/37c1019b5ce4958bf88c6e5c14b98a2fb2a0e854)
[two](http://gitorious.org/butaca/butaca/commit/e6c463fc56384eabdfb2db16f046186a6eebce77)
commits should be pretty self-explanatory. The first one provides the
Debian package infrastructure, so the binary is created. The second one
does the necessary magic to get the service file in the appropriate
directory. My sources for this were [Vagalume
project](http://gitorious.org/vagalume) and [this DBus
tutorial](http://raphael.slinckx.net/blog/documents/dbus-tutorial).

However, I didn't know what to do with the Python part. Ship it
together? Separately? How? From what I've seen, Python apps often use
[distutils](http://docs.python.org/distutils/introduction.html#distutils-simple-example)
for distribution and installation: creating a setup.py for the python
part of maevies wasn't hard: with a simple file like [this
one](http://gitorious.org/butaca/maevies/blobs/master/setup.py), all the
Python code could be distributed. But I still had to put it in a
package... so I decided to stop losing time and do the following:

-   Maevies' backend and frontend will be separated from now on. That
    makes building Debian packages really easy, and later, will be
    better for i18n support.
-   Move from Maemo's garage to gitorious. In one of the latests IRC
    meetings, they [talked
    about](http://forums.internettablettalk.com/showpost.php?p=699842&postcount=1)
    shutting down the garage and start providing a migration path. The
    sooner I do it, the better.

Both the split up and the move to [gitorious](http://gitorious.org/)
have an additional benefit: the backend, being perfectly suited for any
modern GNU / Linux distro, is now separated and in a more visible site,
with the project being called [Butaca](http://gitorious.org/butaca), and
the backend [butaca-server](http://gitorious.org/butaca/butaca-server).
Maevies' UI is what will keep the
"[Maevies](http://gitorious.org/butaca/maevies)" name, being fully
developed in PyGTK, and focusing on Maemo. (A Gnome desktop client
should follow soon)

Something really nice about this move is that I'll preserve the git
history. Thanks to [this Stack
Overflow](http://stackoverflow.com/questions/359424/detach-subdirectory-into-separate-git-repository)
link, nothing will be lost: it explains how to split  (or detach as they
say) a directory, with its history, from the whole project.
