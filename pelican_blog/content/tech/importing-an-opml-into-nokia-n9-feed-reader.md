Title: Importing an OPML into Nokia N9 Feed Reader
Date: 2012-03-21 15:35
Author: Simón
Category: Tech
Tags: Igalia, maemo, meego, qml
Slug: importing-an-opml-into-nokia-n9-feed-reader
Status: published

As you know (and it's already reported), there's currently no
way to import an
[OPML](http://en.wikipedia.org/wiki/OPML "Outline Processor Markup Language")
into the Nokia N9 Feed Reader application (see [Harmattan Bug
\#159](https://harmattan-bugs.nokia.com/show_bug.cgi?id=159)).

However, I noticed that when you open a feed link with the built-in
browser, it launches the Feed Reader app, and asks you to subscribe to
the feed. I guessed that it was communicating with the Feed Reader using
D-Bus, so I `dbus-monitor`ed it, and that's what I found:

* First, the browser asks the application to subscribe to a given feed
  (here I'm asking the client to subscribe to my blog's feed):  
```
dbus-send --print-reply --dest=com.nokia.FeedReader   
/   
com.nokia.FeedReader.subscribeFeed array:string:"http://simonpena.com/blog/feed/"
```
* If the user accepts that, then the Feed Reader application requests
  the Engine to actually subscribe to the Feed. The nice thing is
  that, although you cannot (AFAIK) ask the client to subscribe to
  more than one feed at the time, you can ask the Engine to do it, so
  this actually works (requesting the engine to subscribe to my blog,
  [Planet Maemo](http://planet.maemo.org/ "Planet Maemo") and [Planet
  Igalia](http://planet.igalia.com "Planet Igalia")):  
```
dbus-send --print-reply --dest=com.nokia.FeedEngine   
/   
com.nokia.FeedEngine.subscribe   
array:string:"http://simonpena.com/blog/feed/","http://maemo.org/news/planet-maemo/rss.xml","http://planet.igalia.com/atom.xml"   
string:"rssatom"
```

From this point on, it should be quite straight forward to import an
OPML into the Feed Reader application. You can use a `QDomDocument` to
parse the OPML or use QML's `XmlListModel` to parse the OPML file.

```
XmlListModel {
    property string subTitle: ''

    query: subTitle ? "/opml/body/outline[@title='" + titleText + "']/outline": "/opml/body/outline"

    XmlRole { name: 'text'; query: '@text/string()' }
    XmlRole { name: 'title'; query: '@title/string()' }
    XmlRole { name: 'type'; query: '@type/string()' }
    XmlRole { name: 'xmlUrl'; query: '@xmlUrl/string()' }
    XmlRole { name: 'htmlUrl'; query: '@htmlUrl/string()' }
}
```

Then, you can use this to subscribe to the feeds using D-Bus:

```
    static const QString DBUS_IFACE("com.nokia.FeedEngine");

    void Controller::subscribeFeeds(const QStringList &feedList) const
    {
        QDBusInterface dbusInterface(DBUS_IFACE,
                                     "/",
                                     DBUS_IFACE,
                                     QDBusConnection::sessionBus());

        dbusInterface.asyncCall("subscribe",
                                QVariant::fromValue(feedList),
                                QVariant::fromValue(QString("rssatom")));
     }
```

I hope you find this useful :-)
