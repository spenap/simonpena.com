Title: And now, introducing maevies
Date: 2010-06-01 12:51
Author: Simón
Category: Butaca
Tags: maemo, maevies
Slug: and-now-introducing-maevies
Status: published

Back in October, [a friend](http://picandocodigo.wordpress.com) and I
started a project targeting Maemo. We had been thinking about
programming for maemo for a lot of time (but for [Diablo
devices](http://wiki.maemo.org/Internet_tablets)), and
[Fremantle](http://wiki.maemo.org/Fremantle)'s new UI, so appealing,
almost got us buying a N900 (we ended up buying a HTC Tattoo, but that's
another story).

At that moment, I was going to the cinema maybe twice a month, and as
some of my friends have the (sometimes annoying) habit of waiting after
the credits to see if the movie has extra scenes or something, I thought
it would be nice if I had an app in my phone which could tell me if it
was worth waiting. A nice brainstorm started, and we added showtimes and
other movie info to the app, so Maevies -from *movies + maemo*- was
born. After that, it was "just" a matter of researching which web
services could provide that info.

We got the backend "working" rather soon. We started using librest and
synchronous calls, so the user would be blocked until we got a response
from the web services. We wanted to have a basic backend functionality,
and quickly focus on the UI but... we stopped there. We met a couple of
times to get started with the UI, but didn't get too far.

About a month ago [I
announced]({filename}/master-sw-libre/introducing-jamp-a-jamendo-client.md)
that we were starting the development module in the master and that,
after having enjoyed [an introduction to
python](http://www.joaquimrocha.com/2010/04/25/python-class-at-master-in-free-software-0910/),
I was quite convinced to port Maevies to Python. Then, [I
commented]({filename}/master-sw-libre/introducing-jamp-a-jamendo-client.md#comment-513)
in the same post that I wouldn't port it, but mimic the architecture
we're using for the master app: C with GObject for the model, and Python
at the view, connected using DBus. Soon I had all the old maevies
backend adapted to use GObject, all the librest references removed and
replaced with libsoup's, and a basic prototype with PyMaemo, with a fake
behaviour like the one I would expect from the actual app.

Today, I can announce a "functional" pre-alpha version of Maevies. I've
created a [page](http://simonpena.com/projects/maevies/) for it at this
blog, and linked it from the [maemo garage's
one](https://garage.maemo.org/projects/maevies/), have taken [some
screenshots](http://picasaweb.google.es/spenap/Maevies?feat=directlink),
and pushed the last commits (yeah, I also migrated from subversion to
git, now that I'm feeling really comfortable with it).

**So what's going on with maevies?**

-   About the backend: A movie can be searched in
    [themoviedb.org](http://www.themoviedb.org/) -getting its basic
    info- and
    [whatsafterthecredits.com](http://whatsafterthecredits.com/) -getting
    the information about extra scenes. There is also a module which
    parses Google Movies html, not using GObject yet, but some changes
    in their API seem to have broken its support.
-   About the user interface: The user can query for a movie using
    themoviedb service, retrieve a list of results, and display the
    basic info for the selected movie. (The DBus service must be brought
    up manually, as I didn't create the .service file to allow DBus
    doing it). Besides the screenshots below which should give the
    general idea, there's this
    [screencast](http://dl.dropbox.com/u/3321982/maevies-pre-alpha-3_screencast.ogg).
    It has, however, a lot of flickering: it's been recorded with the
    app running under Xephyr, using
    [Istanbul](http://live.gnome.org/Istanbul). If you know a better way
    to record a screencast, please drop me a comment :)

**And what are the next steps?**

-   Not all the TMDb retrieved data is exported via DBus, nor displayed
    later on the UI, so that would be a point.
-   It would be nice to display the movie images, also.
-   Bringing the whatsafterthecredits info to the UI would finally add
    the initially desired functionallity

[caption id="" align="aligncenter" width="288" caption="Welcome
Window"][![Maevies - Welcome
window](http://lh5.ggpht.com/_e7POG3HT_zk/TATf1PC8u7I/AAAAAAAAAhk/nbQGM8n5ON0/s288/maevies-pre-alpha_welcome-window.png "Maevies - Welcome window")](http://picasaweb.google.es/lh/photo/K04xy0vsJM4zxI5ALyyFww?feat=directlink)[/caption]

[caption id="" align="aligncenter" width="288" caption="Search
Dialog"][![Maevies - Search
dialog](http://lh6.ggpht.com/_e7POG3HT_zk/TATf1A-lEfI/AAAAAAAAAho/-En1rcF5fyo/s288/maevies-pre-alpha_search-window.png "Maevies - Search dialog")](http://picasaweb.google.es/lh/photo/w5Xt4YKs_0JaFSVv0n2Rdw?feat=directlink)[/caption]

[caption id="" align="alignleft" width="288" caption="Search
Results"][![Maevies - Search
results](http://lh4.ggpht.com/_e7POG3HT_zk/TATf1aMi9QI/AAAAAAAAAhw/2vF-lx6ij0I/s288/maevies-pre-alpha_search-results.png "Maevies -  Search Results")](http://picasaweb.google.es/lh/photo/2_ny_D5Fy2wQM7akcLOGBA?feat=directlink)[/caption]

[caption id="" align="alignleft" width="288" caption="Movie
Info"][![Maevies - Movie
info](http://lh6.ggpht.com/_e7POG3HT_zk/TATf1ltryBI/AAAAAAAAAh0/MxwOl5GrTZ8/s288/maevies-pre-alpha_movie-info-up.png "Maevies - Movie Info")](http://picasaweb.google.es/lh/photo/JdBpWpLsOtEHT1iefU76Sg?feat=directlink)[/caption]
