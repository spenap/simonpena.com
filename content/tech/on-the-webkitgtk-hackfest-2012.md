Title: On the WebKitGTK+ Hackfest 2012
Date: 2012-12-13 16:30
Author: Simón
Category: Tech
Tags: GNOME, Igalia, WebKit, WebKitGTK+
Slug: on-the-webkitgtk-hackfest-2012
Status: published

This week I attended my first WebKitGTK+ hackfest. It was
hosted at our [Igalia](http://www.igalia.com/) office in A Coruña, so it
was the perfect opportunity to join [so many good
hackers](https://live.gnome.org/Hackfests/WebKitGTK2012)!

[Claudio](http://people.gnome.org/~csaavedra/) wrote a pretty good blog
post giving [an overview of the
hackfest](http://people.gnome.org/~csaavedra/news-2012-12.html#D11) ,
explaining who was doing what, so I'll just mention that I focused on
[improving the WebKit2GTK+ port sections
documentation](https://bugs.webkit.org/show_bug.cgi?id=104484) (because,
you know, we don't want
[this](http://geek-and-poke.com/2010/01/documentation-is-key.html) to
happen). You can see here how scarce it was looking previously:

![Original documentation]({filename}/images/WebKit2GTK+-doc-before-300x224.png)

and how it looks now:

![Updated documentation]({filename}/images/WebKit2GTK+-doc-after-300x224.png)

That's just the short description, but each of those sections has also
an extended description that tries to give an idea of how to use it.
Still, if something is not clear enough, just file a bug and we'll try
to improve it.

This updated documentation will be available at the [WebKit2GTK+
Reference
Manual](http://webkitgtk.org/reference/webkit2gtk/unstable/index.html)
in the next release, but since it's already upstream, you can build it
yourself simply passing the `--enable-gtk-doc` flag.

I also want to thank the GNOME Foundation and all the sponsors who have
made this event possible:

[![Igalia Logo](https://live.gnome.org/Hackfests/WebKitGTK2012?action=AttachFile&do=get⌖=igalia-logo.png)](http://www.igalia.com)

[![Collabora Logo](https://live.gnome.org/Hackfests/WebKitGTK2012?action=AttachFile&do=get⌖=collabora-logo.png)](http://www.collabora.co.uk)

[![GNOME Logo](http://blogs.gnome.org/xjuan/files/2012/09/sponsored-by-gnome-foundation.png)](http://foundation.gnome.org)
