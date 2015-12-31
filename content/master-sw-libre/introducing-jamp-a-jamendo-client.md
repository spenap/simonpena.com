Title: Introducing Jamp: a Jamendo client.
Date: 2010-04-29 09:28
Author: Simón
Category: Máster SW Libre
Tags: Jamp
Slug: introducing-jamp-a-jamendo-client
Status: published

This last weekend we had two very interesting sessions in the[Destkop
and Mobile development](http://www.mastersoftwarelibre.com/?page_id=273)
module. On Friday,  it was an [introduction to
Python](http://www.joaquimrocha.com/2010/04/25/python-class-at-master-in-free-software-0910/),
followed by a [PyGTK](http://www.pygtk.org/) app. While the app was very
simple, it covered the basics: using containers to add widgets, handling
signals, setting callback functions. I liked it so much that I'm
seriously considering porting
[maevies](https://garage.maemo.org/projects/maevies/) (the maemo app a
friend and I are developing, stalled for some months) to PyGTK. After
all, all we needed was [libRest](http://moblin.org/projects/librest),
and I'm confident that Python has something similar.

But that was on Friday. On Saturday, we started with the first workshop.
During the module, we are going to develop a Gnome desktop application,
which will be later ported / adapted to Maemo: a
[Jamendo](http://www.jamendo.com/en/) client called
[Jamp](http://gitorious.org/mswl2010/jamp). The application has ben
designed / is being designed with that port in mind, so hopefully we
won't need too many changes to achieve it. We've been distributed
between three teams: UI with PyGTK, web API connection with
[libsoup](http://live.gnome.org/LibSoup), and multimedia playback, with
[gstreamer](http://gstreamer.freedesktop.org/). Wikipedia
[says](http://en.wikipedia.org/wiki/Jamendo)

> **Jamendo** is a music platform and community.
>
> All music on Jamendo is free to download and licensed through one of
> several Creative Commons licenses or the Free Art License, making it
> legal to copy and share, as well as to modify and make commercial use
> of for some, depending on the license. Jamendo allows streaming of all
> of its thousands of albums in either Ogg Vorbis or MP3 format, and
> downloads through the BitTorrent and eDonkey networks.

So, while we learn, we'll be contributing to a Good Thing™ :). I'm very
motivated about using git, doing a team development, submitting patches,
and enjoying such a collaborative environment.

I'll try to keep you updated :)
