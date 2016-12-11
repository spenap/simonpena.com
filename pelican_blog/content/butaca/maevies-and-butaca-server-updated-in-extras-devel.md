Title: Maevies and butaca-server updated in extras-devel
Date: 2010-08-24 22:57
Author: Simón
Category: Butaca
Tags: maemo, maevies
Slug: maevies-and-butaca-server-updated-in-extras-devel
Status: published

After almost a month without updates, today I've pushed some fixes and
improvements to [Maevies](http://gitorious.org/butaca/maevies)
and [butaca-server](http://gitorious.org/butaca/butaca-server).

-   Query results are freed once they're no longer needed
-   The service quits when the user closes the client
-   There's a proper About window (taken from [Joaquim
    Rocha](http://www.joaquimrocha.com/)'s
    [SeriesFinale](http://gitorious.org/seriesfinale))
-   Maemo packages
    ([Maevies](http://maemo.org/packages/view/maevies/), [butaca-server](http://maemo.org/packages/view/butaca-server/)) in
    extras-devel work fine (previous version for butaca-server lacked
    the butaca-service file, even if the autobuilder log said it was OK)

The nice news is that Maevies already had users! I haven't promoted this
app neither in [talk.maemo.org](http://talk.maemo.org/) nor in
[Identica's Maemo group](http://identi.ca/group/maemo), but several
Maemo-related blogs and forums were [listing
it](http://www.google.es/search?q=maevies+-site%3Asimonpena.com+-site%3Apicasaweb.google.es+-site%3Amaemo.org).
It's funny because, as butaca-server's previous version didn't work,
those users were happy just with python-webkit pointing to Google Movies
:). I hope they enjoy the new features they'll find.

[caption id="" align="aligncenter" width="288" caption="About
Window"][![](http://lh4.ggpht.com/_e7POG3HT_zk/THQ9qJmDv-I/AAAAAAAAAqk/iWxNLdYclPA/s288/Maevies%20-%20About%20Window.jpg "About Window")](http://picasaweb.google.es/lh/photo/QWtVwC54fkVMeODPDyGy3w?feat=embedwebsite)[/caption]

[caption id="" align="aligncenter" width="288" caption="Movie Info - The
Expendables"][![](http://lh5.ggpht.com/_e7POG3HT_zk/THQ9sg42a9I/AAAAAAAAAqo/RST21dhcgvw/s288/Maevies%20-%20Movie%20Info.jpg "Movie Info - The Expendables")](http://picasaweb.google.es/lh/photo/YxIk2s0PI_PImGMV-w69gw?feat=embedwebsite)[/caption]

[caption id="" align="aligncenter" width="288" caption="Movie Stingers -
The
Expendables"][![](http://lh3.ggpht.com/_e7POG3HT_zk/THQ9v8QLYuI/AAAAAAAAAqs/KIMmFa0V2Hs/s288/Maevies%20-%20Stingers.jpg "Movie Stingers - The Expendables")](http://picasaweb.google.es/lh/photo/wQv_Yfz7JScKcTDLgnxtJw?feat=embedwebsite)[/caption]
