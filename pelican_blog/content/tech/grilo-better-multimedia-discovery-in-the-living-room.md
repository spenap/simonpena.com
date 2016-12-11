Title: Grilo: better multimedia discovery in the living room
Date: 2012-06-20 10:55
Author: Simón
Category: Tech
Tags: Grilo, Igalia
Slug: grilo-better-multimedia-discovery-in-the-living-room
Status: published

Some days ago, I talked about [my current living-room
setup]({filename}/tech/using-minidlna-on-a-sheevaplug-to-feed-content-into-a-panasonic-viera-tv.md).
It is cool, since I'm reusing components I already have, but it's quite
clear that it has some issues:

* It won't extend well. If I ever want to browse my *Flickr* pictures,
  that won't be enough
    * The same goes for videos (*Youtube*, *Vimeo*, *blip.tv*...)
    * And many other services out there
* The TV supports part of the content, the *XBox*supports another part...
* The UI for the [UPnP](http://en.wikipedia.org/wiki/Universal_Plug_and_Play) clients is quite basic

TVs are no longer regular TVs: they are smart! (Think about the
[Panasonic Viera](http://panasonic.net/avc/viera/index.html), [Samsung
Smart TVs](http://www.samsung.com/us/2012-smart-tv/), [Philips
SmartTV](http://www.smarttv.philips.com/)...). Many other devices have
many different multimedia capabilities: some of them dedicated ([Asus
O!Play](http://www.asus.com/Multimedia/Digital_Media_Player/OPlay_HDPR1/),[Blusens
Blubrain](http://www.blusens.com/en/productos/hogar-digital/blu:brain/)...)
others are gaming devices that include these features (*PS3*, *XBox*...).

They solve different subsets of the problem: for example, providing
*Flickr*, *Youtube*, *Vimeo*... applications, or having a better *UPnP*
client, or even providing application markets so you get new apps for
new services. But for that to happen, some developer has to provide the
apps, maybe having to learn the API for a web service: **none of these
devices solve the need for a unified path, for a single experience, both
from the developer and the user point of view**.

With [Grilo](https://live.gnome.org/Grilo), you can get that. Grilo is a
framework, developed and maintained by [Igalia](http://www.igalia.com/),
focused on making media discovery and browsing easy for application
developers. With it, you get

> -   A single, high-level API that abstracts the differences among
>     various media content providers, allowing application developers
>     to integrate content from various services and sources easily.
> -   A collection of plugins for accessing content from various media
>     providers. Developers can share efforts and code by writing
>     plugins for the framework that are application agnostic.
> -   A flexible API that allows plugin developers to write plugins of
>     various kinds.

Hardware vendors shipping their products with Grilo in their SDKs would
expose to third party developers consistent APIs to access the different
media providers. Developers targeting those platforms would only have to
care about Grilo's API, since most popular media providers are already
supported *out of the box*, and only if a service is very new (or less
popular) they would have to write a plugin for it. One consequence for
this is that developers will have more time to focus on what will let
them differentiate from their competitors: the UI.

Users would finally get revolutionary experiences, where, for example,
videos or pictures from different sources would be together, or where
the application would be interactive and gesture-driven. Or anything you
could imagine!

Check its [official page](https://live.gnome.org/Grilo) in the GNOME
project for all the details, its [page at
Igalia](http://www.igalia.com/nc/work/project/item/grilo/), or [Grilo at
Ohloh](http://www.ohloh.net/p/grilo-fw) for past blog posts and other
information. Also, if you come to Coruña for the
[GUADEC](http://www.guadec.org/), don't hesitate to ask any igalian
about it!
