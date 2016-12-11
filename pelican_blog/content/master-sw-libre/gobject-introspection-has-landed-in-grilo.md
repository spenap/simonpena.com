Title: GObject Introspection has landed in Grilo!
Date: 2010-08-18 21:28
Author: Simón
Category: Máster SW Libre
Tags: GObject Introspection, Grilo, Igalia, PyGObject, Python
Slug: gobject-introspection-has-landed-in-grilo
Status: published

If you're using [Grilo](http://live.gnome.org/Grilo "Grilo") from git,
[last patches](http://git.gnome.org/browse/grilo/log/) <s>enabled</s> improved [GObject
Introspection](http://live.gnome.org/GObjectIntrospection "GObject Introspection")
so you can start using Python with
[PyGObject](http://live.gnome.org/PyGObject "PyGObject - GLib/GObject/GIO Python bindings")
to develop your applications.

A Python clone of the grilo-test-ui is provided, and should give you an
idea of what can be done with these new bindings: basically enjoy all
the power in Grilo without needing to touch C code, and without us
having to maintain manually created bindings.

If you're a JavaScript user, then you need to watch bug
[\#616961](https://bugzilla.gnome.org/show_bug.cgi?id=616961 "Grilo's introspection data is incomplete/incorrect").
As JavaScript doesn't support GParamSpecs yet
([\#626047](https://bugzilla.gnome.org/show_bug.cgi?id=626047 " Can't create a Javascript object for ParamSpec")),
you'll need [this
patch](https://bugzilla.gnome.org/attachment.cgi?id=168225 "Patch replacing GParamSpec annotations with uints.")
which replaces GParamSpec annotations with uints. And now, time for unit
testing with PyGObject!

![Using Grilo bindings from Python console]({filename}/images/grilo-gobject-introspection.png)

![grilo-test-ui using GObject Introspection bindings]({filename}/images/grilo-test-ui-introspection.png)

![Missing GParamSpec when accessing from JavaScript]({filename}/images/gjs-grilo-introspection.png)
