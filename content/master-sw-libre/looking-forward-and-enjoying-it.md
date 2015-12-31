Title: Looking forward (and enjoying it)
Date: 2010-04-09 00:40
Author: Simón
Category: Máster SW Libre
Slug: looking-forward-and-enjoying-it
Status: published

This Friday we're starting the [Desktop/Mobile
module](http://www.mastersoftwarelibre.com/?page_id=273) on the Free
Software Master. One of the reasons that brought me here was that one: I
wanted to jump into GTK and Qt development, learn new programming
languages, and, specifically, learn to develop for mobile devices. What
I think now, which really gets me motivated, is the idea that
considering how much I've enjoyed the previous modules which in advance
didn't look so great (to me), this one will be incredible.

But there's also another point: more than a half of the
[course](http://www.mastersoftwarelibre.com/?page_id=5) is over, now.
Summarizing, we've gone through Introduction to Libre Software, where we
learnt the most important people in this movement, learnt about Business
Models or Licensing stuff among other things; Dynamics of Libre Software
Communities, where we analyzed and studied several important communities
and learnt the process to apply those analysis to other ones; and now,
just before Easter Holidays, we've got [Systems Integration with Libre
Software](http://www.mastersoftwarelibre.com/?page_id=242). In this last
module, even if it almost shares the name with a [5º course
subject](http://www.tic.udc.es/is-java/) in[Ingeniería Informática at
UDC](http://www.fic.udc.es/MainPage.do), we didn't learn Web
Technologies (there's a
[module](http://www.mastersoftwarelibre.com/?page_id=268) for that!):
we've done security, systems administration, scripting, servers
configuration and management, version control with git...

And, at this point, I'd like to share with you some of the things we've
been doing here. Fortunately, my mates and I -as previous editions'
students did- are using a subversion repository hosted at [Morfeo's
Forge](https://forge.morfeo-project.org/projects/freeswmaster/), where
all the practices and assignments were developed (in the open, as the
master's philosophy would suggest), so it's very interesting to share
all of this work with anyone interested.

I'm grouping them by subject -I won't link my mates' works, but they can
do it in this post's comments-. I'll point out those mistakes I found
after I handed out the works, and also all known limitations, some
possible improvements or even things which are already outdated. Here it
goes:

**Introduction to Libre Software:**

-   [Business
    Model](https://forge.morfeo-project.org/plugins/scmsvn/viewcvs.php/trunk/spenap/isl/business-model/?root=freeswmaster):
    I presented a business model focused on service-oriented apps for
    mobile devices. Accounting numbers aren't that accurate, but sources
    and references should be very handful just in case you're
    interested. About the ideas (licensed Creative Commons Attribution
    Share-Alike unless otherwise stated), I didn't want to reinvent the
    wheel, but joining and mixing existing technologies so I would get
    something attractive.
-   [Mobile Operating Systems
    Review](https://forge.morfeo-project.org/plugins/scmsvn/viewcvs.php/trunk/spenap/isl/mobile-os/?root=freeswmaster):
    I wanted to give a look at current OSs in mobile devices world,
    around Christmas 2010. However, less than a month later, Maemo and
    Moblin merged, Symbian accelerated its transition to Libre Software,
    Samsung focused more clearly on Bada... Maybe this is the most
    outdated work, but will be funny to check out after a year time.

**Dynamics of Libre Software Communities**

-   [Eye Of Gnome
    Mini-Review](https://forge.morfeo-project.org/plugins/scmsvn/viewcvs.php/trunk/spenap/dlsc/eog_exercise/?root=freeswmaster):
    This work was intended for training us with the use of Libresoft
    Tools. Source code repository and mailing list were used, so we
    could identify the most important contributors to the project.
-   [WebKit Project
    Review](https://forge.morfeo-project.org/plugins/scmsvn/viewcvs.php/trunk/spenap/dlsc/webkit_analysis/?root=freeswmaster):
    My original idea was quite ambitious, as I wanted to compare WebKit
    and Gecko, but soon I focused on WebKit. While this work is really
    interesting, the conclusions I reached are quite biased: my main
    measure to evaluate code collaboration was the committer id, while
    WebKit project stores the real author of a commit in the ChangeLog,
    which I ignored. The good thing here is that, provided that a
    ChangeLog parser is done, my scripts, tools and procedures can be
    used to get a very nice report. Besides, being Igalia a company so
    involved in WebKit development (specially in WebKitGtk+), this work
    has a lot of potential.

**Systems Integration with Libre Software**

-   [(Bash)
    Scripting](https://forge.morfeo-project.org/plugins/scmsvn/viewcvs.php/trunk/spenap/ias/scripting/?root=freeswmaster):
    We went through some common problems in systems' administration:
    daemons, regular expressions, using find, sed...
-   [Perl
    development](https://forge.morfeo-project.org/plugins/scmsvn/viewcvs.php/trunk/spenap/ias/perl/?root=freeswmaster):
    With the "Learning by doing" moto, we got introduced to Perl. It was
    a brief and interesting tutorial which meant, at least for me,
    meeting a language with a very bad reputation, but really powerful.
    I really enjoyed the last two exercises, when we played a while with
    Last.fm's API.
-   [Networking](https://forge.morfeo-project.org/plugins/scmsvn/viewcvs.php/trunk/spenap/ias/networking/?root=freeswmaster):
    Some networking stuff. It was nice, as I already knew some things,
    but haven't heard at all of others. I'd say that, rather than
    building complex networks and all that, we had to really understand
    how they work.

Of course, I'm missing lots of things. So if you want further info, you
can browse the [full
repository](https://forge.morfeo-project.org/projects/freeswmaster/) to
get my mates' works or other years', you can [check the
moodle](http://gsyc.escet.urjc.es/moodle/course/category.php?id=17) for
the theory, [read the planet](http://planet.mswl.igalia.com/) for other
comments... Enjoy, and *Happy Hacking*!
