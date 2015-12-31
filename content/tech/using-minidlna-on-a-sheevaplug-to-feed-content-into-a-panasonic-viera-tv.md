Title: Using minidlna on a SheevaPlug to feed content into a Panasonic Viera TV
Date: 2012-06-04 16:30
Author: Simón
Category: Tech
Tags: Igalia, minidlna, panasonic, plug computing, sheeva plug, TXL37E30E, viera
Slug: using-minidlna-on-a-sheevaplug-to-feed-content-into-a-panasonic-viera-tv
Status: published

Since I bought a [Panasonic Viera
TV](http://panasonic.net/avc/viera/index.html "Panasonic Viera TV"),
some 5 months ago, I had been connecting my laptop to it whenever I
wanted to watch a movie, some series or even the pictures I took on my
trips.

That was quite annoying: the VGA connection (since the laptop only has
HDMI output in its dockstation), checking that the laptop had enough
battery (or adding yet more wires to keep it plugged), connecting it to
some external speakers... and all of this while having a
[SheevaPlug](http://www.globalscaletechnologies.com/p-26-sheevaplug-dev-kit-europe.aspx "SheevaPlug Dev Kit")
almost 24/7.

So a couple of weeks ago I bought an external drive and configured it as
a media server. This is my setup now, in case someone is interested:

-   First generation SheevaPlug with the [HDD Western Digital 2TB My
    Book](http://wdc.com/en/products/products.aspx?id=240 "HDD Western Digital My Book")
-   Panasonic Viera TV

Software
--------

* [minidlna](http://sourceforge.net/projects/minidlna/ "MiniDLNA"). With a
very simple configuration, it exposes your media content and works great
with Viera's integrated upnp client.
* Viera is able to use external srt subtitle files for some of the
supported formats (typically avi or mp4), but that won't work with mkv. If you use mkv, you can add a new subtitles track to your mkv (for example, using mkvmerge, from the [mkvtoolnix](http://www.bunkus.org/videotools/mkvtoolnix/ "MKVToolNix -- Cross-platform tools for Matroska") package)

Oddities
--------

Viera is quite picky sometimes. If you create your own mkvs with
mkvmerge, be sure not to add compression (check *compression:none*
parameter). By default, mkvmerge tries to compress the header of the
audio track (and most players are fine with that, but Viera is not)

I currently use something like the following to add a subtitles track:

>     mkvmerge -o output.mkv --compression -1:none file.mkv file.srt

Not only that: Viera seems to support a limited set of encodings for
subtitles. *LATIN1* is known to work fine, so if you have your subtitles
in *UTF*, you can use unaccent and iconv to convert them to *LATIN1*.

>     cat subtitles-utf.srt | unaccent LATIN1 | iconv -f UTF-8 -t LATIN1 -c > subtitles-latin1.srt

And the previous script helps me striping non-LATIN1 characters out of a
subtitles file.
