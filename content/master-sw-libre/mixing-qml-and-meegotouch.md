Title: Mixing QML and MeeGoTouch
Date: 2011-10-10 22:07
Author: Simón
Category: Máster SW Libre
Tags: harmattan, Igalia, maemo, meego, meegotouch, qml
Slug: mixing-qml-and-meegotouch
Status: published

When trying to invoke a MeeGoTouch application's MSheet from a QML app,
I was getting the following error:

>     There is no instance of MDeviceProfile. Please create MComponentData first.

Using `MApplication` instead of `QApplication` would solve that, but
still a `MApplicationWindow` would be needed to make the `MSheet`
appear.

After searching on Google for a while (see after the snippet for the
sources) and [talking to gri in
\#harmattan](http://mg.pov.lt/harmattan-irclog/%23harmattan.2011-10-10.log.html#t2011-10-10T22:54:39 "IRC logs"),
I've come up with the following solution:

>     #include <MApplication>
>     #include <MApplicationWindow>
>     #include <MApplicationPage>
>     #include <QDeclarativeEngine>
>     #include <QGraphicsObject>
>     #include <QDeclarativeComponent>
>     #include <QDeclarativeContext>
>
>     int main(int argc, char *argv[])
>     {
>         MApplication app(argc, argv);
>         QDeclarativeEngine engine;
>
>         // The context is unused in this example
>     //    QDeclarativeContext *context = engine.rootContext();
>
>         MApplicationWindow window;
>         window.showFullScreen();
>
>         MApplicationPage page;
>         page.setPannable(false);
>         page.appear(MApplication::instance()->activeWindow());
>
>         QDeclarativeComponent component(&engine, QUrl("qrc:/qml/main.qml"));
>         QGraphicsObject *content = qobject_cast<QGraphicsObject*>(component.create());
>         MWidget *centralWidget = new MWidget;
>         content->setParentItem(centralWidget);
>         page.setCentralWidget(centralWidget);
>
>         int result = app.exec();
>
>         delete centralWidget;
>
>         return result;
>     }

From [QML support in Meego touch
Framework](http://permalink.gmane.org/gmane.comp.handhelds.meego.touch.devel/110 "QML support in Meego touch Framework")
I learnt that I had to load the QML into a MeeGoTouch widget, so I
followed [Loading QML components from
C++](http://doc.qt.nokia.com/4.7-snapshot/qtbinding.html#loading-qml-components-from-c "Loading QML components from C++")
to replace the `loadQmlComponent` non-existing method with the
`QDeclarativeComponent::create` approach.

Also, note that I use `MApplicationWindow::showFullScreen` instead of
`MApplicationWindow::show` and `MWidget::setMinimumSize`
