Title: Butaca in Harmattan
Date: 2011-07-13 22:55
Author: Simón
Category: Butaca
Tags: harmattan, Igalia, maemo, meego, qml
Slug: butaca-in-harmattan
Status: published

Three weeks ago, the [N9 was announced](http://swipe.nokia.com/). Little
can be added to [what's been
written](http://blogs.igalia.com/berto/2011/06/23/n9/): it's a great
achievement, but also a [bitter
one](http://www.helsinkitimes.fi/htimes/domestic-news/business/15821-nokias-elop-says-n9-will-be-only-meego-handset-hs-.html).
Still, I really think that great things can be done on this platform,
and that's why I applied to the [N950 Devkit
Program](http://wiki.meego.com/Community_Office/Community_device_program/Nokia).

My initial idea was to port
[Maevies](/category/butaca/) from Fremantle to
Harmattan, keeping [the same
architecture](http://wiki.meego.com/User:Spenap/Butaca#In_Fremantle). In
the week or so that went between the N9 announcement and the filtering
of the candidates for the devkit program, I resumed the development on
the [client side](http://maemo.org/packages/view/maevies/), bringing the
ability to save and load favorite movies, as well as other minor UI
fixes, and also [updated the D-Bus
service](https://gitorious.org/butaca/butaca-server) so that it would
compile on HARMATTAN target.

When I knew I was selected for the program, I started using PySide
(specifically [Harmattan
Python](http://lists.pyside.org/pipermail/pyside/2011-June/002604.html))
to quickly get a working UI which could connect to the D-Bus service...
but it turned out that I didn't need it, thanks to the powerful way to
deal with XML models inside QML. Today I've uploaded "Butaca"
application to [gitorious](https://gitorious.org/butaca/butaca). Still a
draft of what I expect it to be, it lets the user search and browse
through movies, and get detailed information about them. I also created
an entry at the MeeGo Wiki at
[User:Spenap/Butaca](http://wiki.meego.com/User:Spenap/Butaca).

[caption id="" align="aligncenter" width="175" caption="Butaca - Welcome
View"][![](https://lh6.googleusercontent.com/-cS2qH9frOuE/Th4RzkZlL-I/AAAAAAAAAz4/kI6zPvGTU8k/s512/1-welcome-view.png "Butaca - Welcome View")](https://picasaweb.google.com/lh/photo/f-PxkIfi3ibgtMWpTDobww?feat=directlink)[/caption]

[caption id="" align="aligncenter" width="175" caption="Butaca - Search
View"][![](https://lh3.googleusercontent.com/-nHJeWCzlRew/Th4RzZovIdI/AAAAAAAAAz0/qTPHVfD7BmM/s512/2-search-view.png "Butaca - Search View")](https://picasaweb.google.com/lh/photo/TNlGznljCLmgdiddCNMOxQ?feat=directlink)[/caption]

[caption id="" align="aligncenter" width="175" caption="Butaca - Results
View"][![](https://lh3.googleusercontent.com/-VwFF1LaBm2A/Th4R0ujOCcI/AAAAAAAAAz8/ufkOTN15QEg/s512/3-browse-results.png "Butaca - Results View")](https://picasaweb.google.com/lh/photo/FwFqljVn8cXTxhsZhYNBLw?feat=directlink)[/caption]

[caption id="" align="aligncenter" width="175" caption="Butaca -
Detailed
Result"][![](https://lh4.googleusercontent.com/-wp5Fr94l3k8/Th4R0tsvoLI/AAAAAAAAA0A/s6vTsRj9utk/s512/4-detailed-result.png "Butaca - Detailed Result")](https://picasaweb.google.com/lh/photo/xGSlY52VK0BZy7DGpCNkkQ?feat=directlink)[/caption]

 
