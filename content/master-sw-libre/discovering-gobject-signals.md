Title: Discovering GObject signals
Date: 2010-05-01 17:25
Author: Simón
Category: Máster SW Libre
Tags: Custom signals, Events, GObject, Jamp, Signals, signals creation
Slug: discovering-gobject-signals
Status: published

My first idea about this entry was to write down some things I learnt
about GObject signals, while comparing them to what I feel is a close
relative: C\# events. However, after the first draft I think it's better
to focus on GObject now, and leave the comparison for another day.
Credit should go to [Víctor Jáquez](http://blogs.igalia.com/vjaquez/),
from [Igalia](http://www.igalia.com/), who explained me those things
needed to start off. Don't blame him, however, for the mistakes or
misconceptions I may have ;)

There's a design pattern, the [Observer
pattern](http://en.wikipedia.org/wiki/Observer_pattern), used to allow
"subscribers" to track or follow state changes happening on an object,
the "subject". In C\#, this is implemented via Events, in Java you have
the Listeners, and in C, with GObject, you have signals. Going to the
GObject implementation details:

    enum {
            END_OF_STREAM,
            LAST_SIGNAL
    };

    static guint
    jmp_mplayer_signals[LAST_SIGNAL] = { 0 };

The enum "tags" our signals. In this case, we just have one:
END\_OF\_STREAM. LAST\_SIGNAL is a convention: as it is in the last
place, it will be always "our last real signal" + 1. And that's used in
the next line, when we declare an array storing those signals: it will
have "LAST\_SIGNAL" size. It doesn't store the signal itself, but its
identifier, but we'll see that later.

    jmp_mplayer_signals[END_OF_STREAM] =
                    g_signal_newv ("end-of-stream",
                                    G_TYPE_FROM_CLASS (klass),
                                    G_SIGNAL_RUN_LAST | G_SIGNAL_NO_RECURSE | G_SIGNAL_NO_HOOKS,
                                    NULL,
                                    NULL,
                                    NULL,
                                    g_cclosure_marshal_VOID__VOID,
                                    G_TYPE_NONE,
                                    0,
                                    NULL);

That is how the signal is created. It calls the gobject function
[g\_signal\_newv](http://library.gnome.org/devel/gobject/stable/gobject-Signals.html#g-signal-newv)
which creates the signal, and stores its identifier in the array
position given. But, what means each of the params? Well, to be honest,
I don't know too much:

The first one is easy: "end-of-stream" is the signal name. The
documentation sets some limitations to the characters it can contain,
but that's all.  
The second one is "the type this signal pertains to". The macro
[G\_TYPE\_FROM\_CLASS](http://library.gnome.org/devel/gobject/stable/gobject-Type-Information.html#G-TYPE-FROM-CLASS:CAPS)
gets the type from the class structure (klass).  
The third one is composed by signal flags. They "specify detail of when
the default handler is to be invoked".  
I don't know about the next three params: documentation says
*class\_closure*, *accumulator*, and *accu\_data*. As soon as I learn
what they do, I'll update this. Setting them to NULL worked fine for my
needs.  
The fourth one, called *c\_marshaller*, sets the interface for the
callbacks listening for our signals. So, in our example,
g\_cclosure\_marshal\_VOID\_\_VOID means that we won't require our
callback functions to receive arguments. You can find more closures
[here](http://library.gnome.org/devel/gobject/stable/gobject-Closures.html#g-cclosure-marshal-VOID--VOID).  
G\_TYPE\_NONE defines the return type for our callback, so our callback
(closure) signature would have this form:

    void end_of_stream_callback (JmpMPlayer *self, gpointer user_data);

Our last two params are the length of param types, and an array of param
types.

So, what is left? Well, our "subject" still has to notify ("emit", in
GObject) his subscribers. And those subscribers need to actually
"subscribe" to the signal. Here we go:

    switch (GST_MESSAGE_TYPE (message)) {
            case GST_MESSAGE_EOS:
                    g_signal_emit (self, jmp_mplayer_signals[END_OF_STREAM], 0);
                    break;

[g\_signal\_emit](http://library.gnome.org/devel/gobject/stable/gobject-Signals.html#g-signal-emit)
receives an instance the signal is being emitted on, the signal id
(which we had previously stored in that array), and a *detail*. Quoting
the
[documentation](http://library.gnome.org/devel/gobject/stable/signal.html),

> detail identifies the specific detail of the signal to invoke. A
> detail is a kind of magic token/argument which is passed around during
> signal emission and which is used by closures connected to the signal
> to filter out unwanted signal emissions. In most cases, you can safely
> set this value to zero. See [the section called "The detail
> argument"](http://library.gnome.org/devel/gobject/stable/signal.html#signal-detail)
> for more details about this parameter.

And this closes the circle: subscribing to the signal.

    g_signal_connect (jmplayer, "end-of-stream",
                              G_CALLBACK (end_of_stream_callback), loop);

[g\_signal\_connect](http://library.gnome.org/devel/gobject/stable/gobject-Signals.html#g-signal-connect)
connects a given callback (G\_CALLBACK (end\_of\_stream\_callback),
whose signature we saw before), with a signal in an instance (jmplayer),
passing arguments (loop)

To write this entry, I've relied on two documents: [API Reference's
Signals](http://library.gnome.org/devel/gobject/stable/gobject-Signals.html)
and [The GObject messaging system's
Signals](http://library.gnome.org/devel/gobject/stable/signal.html), and
the (yet little) knowledge I acquired during this stage of
[Jamp](http://gitorious.org/mswl2010/jamp) implementation (which,
itself, required [Víctor](http://blogs.igalia.com/vjaquez/)'s help and
said documentation). Full code for this example is available at
Gitorius, for both the
["subject"](http://gitorious.org/mswl2010/jamp/blobs/master/src/jmp-mplayer.c)
and the
["subscriber"](http://gitorious.org/mswl2010/jamp/blobs/master/test/jmplayer-test.c).
