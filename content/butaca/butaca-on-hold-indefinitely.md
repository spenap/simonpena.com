Title: Butaca: on hold indefinitely
Date: 2013-08-19 19:35
Author: Simón
Category: Butaca
Tags: harmattan, maemo, meego, qml
Slug: butaca-on-hold-indefinitely
Status: published

A year and a half ago I [published some
pictures](http://www.flickr.com/photos/bulfaiter/sets/72157629460867862/)
with the new changes that I was preparing in Butaca, hopefully "to be
released soon". Unfortunately, there were some stability issues that I
never had the time to investigate and fix properly, so all the new
features have been sitting in [GitHub](https://github.com/spenap/butaca)
for some time already.

As time went on, I had less and less time and motivation to do MeeGo
development, and eventually I just assumed that only the brave people
having Butaca built from upstream would benefit from the latest changes.
This year, back in May, I received an email from [The Movie
Database](https://www.themoviedb.org) announcing that the 2.1 API (the
one used in Butaca) was reaching its [End Of Life in 15th
September](http://api.themoviedb.org/2.1/), a bit less than a month from
now.

I always thought I would just sit during a weekend, fix these stability
changes and replace the API, but the truth is that [after I moved to the
UK]({filename}/tech/living-in-the-uk-three-months-at-samsung.md),
the kind of "relaxed weekend" needed for that doesn't seem to come too
often. In short, I don't plan to update Butaca before this deadline, so
it will stop working.

So what are your chances as an user? You can use [Pop
Flix](http://store.ovi.com/content/326670 "Pop Flix"): since they use
[Rotten Tomatoes](http://www.rottentomatoes.com/), they shouldn't have
any issues with deprecated APIs. Regarding your favourite movies and
artists, they are saved in a very simple Sqlite database, so you can
manually retrieve the values from there. Of course, since it is Open
Source, you can go to [the
repository](https://github.com/spenap/butaca), fork it and do the
changes yourself.

I really enjoyed developing Butaca. Although it didn't get to be
extremely popular, it achieved more than 10000 downloads, and a really
nice 5-star average of 74 reviews. Thanks to everyone who used it and
enjoyed it, and specially to those who sent me an email with feedback...
and even patches!
