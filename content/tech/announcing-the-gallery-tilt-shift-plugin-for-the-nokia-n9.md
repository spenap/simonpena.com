Title: Announcing the Gallery Tilt Shift plugin for the Nokia N9
Date: 2012-09-21 12:19
Author: Simón
Category: Tech
Tags: harmattan, Igalia, maemo, meego
Slug: announcing-the-gallery-tilt-shift-plugin-for-the-nokia-n9
Status: published

A couple of weeks ago, we at
[Igalia](http://www.igalia.com/ "Igalia: Open Source Consultancy") got a
number of plugins published in the Nokia Store: [Enlarge &
Shrink](http://store.ovi.com/content/302893 "Enlarge & Shrink plugin"),
[Gallery Tilt Shift
plugin](http://store.ovi.com/content/274188 "Gallery Tilt Shift plugin"),
and [Facerecognition Reset
Plugin](http://store.ovi.com/content/274192 "Facerecognition Reset Plugin").
We had them ready for some time already, but still it was very difficult
to pass the Nokia Store Quality Assurance: there is a list of valid
directories where a Debian package can install its files, and they had
missed the ones for Gallery plugins. So, in order to finally get over
that problem, my friend and colleague
[Andrés](http://blog.andresgomez.org/ "Andrés Gómez") had to "fight"
with the Store QA people quite a bit: don't forget to thank him for
this!

Although I developed only the Tilt Shift one, I will briefly introduce
you the other two as well :-)

The [Enlarge & Shrink
plugin](http://store.ovi.com/content/302893 "Enlarge & Shrink plugin")
is an add-on to the built-in Gallery application. You can use it to
apply a radial distortion to a picture, so they look like enlarge and
shrink effects (also known as punch or pinch).

The[Face Recognition Reset
plugin](http://store.ovi.com/content/274192 "Facerecognition Reset Plugin")
also behaves as an add-on, but doesn't work on individual images.
Instead, it forces the deletion or un/protection of the facerecognition
database, something that you might need if for whatever reason the
database gets corrupted.

And finally, the [Tilt Shift
plugin](http://store.ovi.com/content/274188 "Gallery Tilt Shift plugin")
lets you make a picture look as a miniature, by applying the following
transformations:

1.  Blurring the image using a Gaussian Blur filter
2.  Keep an area of the image focused (either vertically or
    horizontally)
3.  Combine both parts of the image using a Gaussian filter (so the
    focus is lost gradually from the focused area to the rest of the
    image)
4.  Increase the saturation, so the colors seems those of a miniature

![Saint Isaac's Square -
Saint Petersburg, before applying the
effect](http://igalia.github.com/gallery-tiltshift-plugin/images/screenshot-before.jpg "Before")
Saint Isaac's Square - Saint Petersburg, before applying the
effect

![Saint Isaac's Square -
Saint Petersburg, after applying the
effect](http://igalia.github.com/gallery-tiltshift-plugin/images/screenshot-after.jpg "After")
Saint Isaac's Square - Saint Petersburg, after applying the
effect

There is a problem, however. Gallery uses
[Quill](https://maemo.gitorious.org/meego-image-editor/ "MeeGo Image Editor"),
and Quill was designed to use tiles in order to minimize the memory
footprint and work happily in mobile devices. That tiling mechanism
finally proved to be less flexible than it should, so for those edit
operations where you can't rely only on the local information in the
tile... things won't work.

You can still use these plugins for small images. Gallery doesn't do
tiling on images of 512x512px or smaller, so that is what is currently
supported. Another option is writing a complete new application to get
this miniature effect (either using Quill with a different tiling
configuration or not using it at all). You can check the full
explanation at the [GitHub page of the
project](https://github.com/Igalia/gallery-tiltshift-plugin#in-depth " In depth:").

All these plugins are Open Source, so you can go to their page at
GitHub: [Enlarge &
Shrink](http://igalia.github.com/gallery-enlarge-shrink-plugin/ "Enlarge & Shrink plugin"),
[Facerecognition
Reset](http://igalia.github.com/gallery-plugin-facerecognition-resetter/ "Facerecognition Reset Plugin"),
[Gallery Tilt
Shift](http://igalia.github.com/gallery-tiltshift-plugin/ "Gallery Tilt Shift plugin")

Take a look at all applications published by [Igalia at the Nokia
Store](http://store.ovi.com/publisher/Igalia/ "Igalia at the Nokia Store").

[![Download from the Nokia
Store](http://simonpena.com/blog/wp-content/uploads/2012/09/505c4a934475a13482256832121058997.jpg "Download from the Nokia Store")](http://store.ovi.com/content/274188)
