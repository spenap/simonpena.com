Title: Butaca, IMDb and TMDb
Date: 2011-07-25 23:37
Author: Simón
Category: Butaca
Tags: harmattan, Igalia, maemo, meego, qml
Slug: butaca-imdb-and-tmdb
Status: published

Right now, probably all of you know [IMDb](http://www.imdb.com/). The
Internet Movie Database is "the place" you'd go to look up a movie or
check the filmography of an actor, writer or director. Some of you will
also be familiar with [IMDb
Android](https://market.android.com/details?id=com.imdb.mobile) and
[iOS](http://itunes.apple.com/us/app/imdb-movies-tv/id342792525?mt=8)
applications, which allow you to check out that very same information on
your mobile device, providing the means to settle any arguments (who
directed *The Terminator*? And *Aliens*?). However, IMDb [doesn't
provide a free API](http://www.imdb.com/help/show_leaf?usedatasoftware):
it provides [a big ZIP file](http://www.imdb.com/interfaces) that you
can download and parse to get that info. Then... -if you don't want to
get a commercial license for the API- what are your chances as an Open
Source developer willing to get the same functionality?

[The open movie database](http://www.themoviedb.org/)

> TMDb was started in the fall of 2008 as a side project in order to
> help serve high resolution posters and fan art for the popular
> [XBMC](http://xbmc.org/) project. What started as just a simple single
> page linked with some zip files has morphed into one of the most
> active user built movie databases on the entire Internet.

> themoviedb.org is a free and open movie database. It's completely user
> driven by people like you. TMDb is currently used by millions of
> people every month and with our powerful
> [API](http://api.themoviedb.org/2.1), also used by the world's most
> popular media centers.

And indeed it is a powerful API. Butaca uses it to provide you with all
the movie information you could need :). At this moment, Butaca
implements almost all the API exposed by TheMovieDb, so you can
[search](http://www.flickr.com/photos/bulfaiter/5953679006/in/set-72157627229855748)
and get information from
[people](http://www.flickr.com/photos/bulfaiter/5953122925/in/set-72157627229855748)
and
[movies](http://farm7.static.flickr.com/6008/5953122627_1b30cdba75_s.jpg)
and [navigate through
genres](http://www.flickr.com/photos/bulfaiter/5953678574/in/set-72157627229855748):
the only thing you need is an Internet connection. Besides, Butaca
allows you to mark the content as favorite so you'd keep it in your home
screen as a shortcut.

[caption id="" align="alignleft" width="120" caption="Welcome view with
favorites"]![](https://projects.developer.nokia.com/butaca/raw-attachment/wiki/WikiStart/2-favorites.png "Welcome view with favorites")[/caption]

[caption id="" align="aligncenter" width="120" caption="Detailed Movie
View"]![](https://projects.developer.nokia.com/butaca/raw-attachment/wiki/WikiStart/3-mad-max.png "Detailed Movie View")[/caption]

Other available feature in Butaca is movie showtimes. Right now, I
couldn't find any world-wide open showtimes API: looks like there are
some local ones, which could serve in some countries (or areas inside
some countries) but most of these APIs need to be licensed. So what's
the solution at the moment? When the user wants to check what's on the
theaters around him, the browser is open pointing to [Google
Movies](http://www.google.com/movies). The browser is used also, if you
want to check if there are shows for a particular movie. In the future
(unless I find some good API), instead of opening the browser, a WebView
will be used.

So if at this point you're still interested, please check out [the
project](https://projects.developer.nokia.com/butaca/). You'll find
plenty of screenshots there, and instructions on how to add the [OBS
repository](https://build.pub.meego.com/)
(`deb http://repo.pub.meego.com/home:/spenap/Harmattan/ ./`) to your
device so you can install Butaca and start using it. And then, start
filing bugs :)
