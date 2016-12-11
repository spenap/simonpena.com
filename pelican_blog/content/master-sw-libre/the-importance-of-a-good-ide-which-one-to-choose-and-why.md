Title: The importance of a good IDE: which one to choose (and why)?
Date: 2010-04-12 20:13
Author: Simón
Category: Máster SW Libre
Tags: ESbox, IDE War, maemo
Slug: the-importance-of-a-good-ide-which-one-to-choose-and-why
Status: published

A few months ago, when I was trying to start developing for
[maemo](http://maemo.org/), I discovered a project called
[ESbox](http://esbox.garage.maemo.org/2nd_edition/). ESbox is *"an
Eclipse Ganymede-based product that helps programmers to develop
applications for Maemo platform using Scratchbox Apophis"*. It launches
scratchbox transparently, includes wizards for different types of apps,
lets you debug step by step and on device, and also uses C/C++ or Python
plugins, so you can refactor code, jump to variable declarations,
explore types, autocomplete...

I don't know exactly when it was, but I once came to maemo IRC channel
to ask a specific (maybe too specific) question about ESbox. I was
surprised that nobody was using it: people there were using
[nano](http://www.nano-editor.org/),
[vi](http://en.wikipedia.org/wiki/Vi),
[Emacs](http://www.gnu.org/software/emacs/)... I asked them about all
the features a "full IDE" offers: what about code refactoring? what
about autocompletion? debugging? While some said that you can get emacs
to auto-complete from a given dictionary, the other questions remained
unanswered. In fact, I almost felt like we weren't talking the same
language.

Our discussion wasn't constructive at all: I don't know if it was the
language barrier, if it was me who said something inappropriate in the
beginning, or if I met people too "Taliban". The thing is that I had to
listen things like "real programmers know the name of the functions /
methods they need: autocompletion is for dumbs". And no, it wasn't a
joke like "real programmers develop their own device drivers". So I gave
up and left the channel: I assumed that programmers would choose their
IDEs according to the kind of development they were doing, so
"hobbyists" would use nano, would copy & paste and wouldn't care too
much about extras, and "professionals"  would use others, or at least
would know and use the extras I wanted. And time went by.

As I was telling you in the last post, this Friday we've got our first
session in the Desktop & Mobile development module of the master. After
its presentation, we had a brainstorming to choose which app we will be
developing during the workshops, and then... we started talking about
IDEs. More specifically, Emacs.

That gave me the opportunity to confirm that there really was a
difference between professional developers and non-professional, and
that my worries were really shared by others. It was a really
interesting chat, where we were explained the environment, from the
basics (navigation a buffer, open, close, *kill and yank*...) to more
complex things: debugger integration, syntax highlighting modules,
autocompletion, macros...

After the session, I now can understand other people not using Eclipse
or Netbeans, while still being productive. I'm not going to use Emacs,
not yet, as it looked like some of the features that "just work" in
Eclipse require some fiddling in Emacs; but at least I know that someone
using Emacs and mastering it will be as efficient as an Eclipse user -or
even more.

Still, when I think about the things I like to have working in Eclipse,
the following comes:

-   Version control: I'd like to be able to check history, undo changes
    across revisions, commit changes, check "who did what" (*blame*)
-   Debugging: Set breakpoints, set conditional breakpoints, step by
    step debugging, variable inspection
-   Syntax highlighting, code folding, autocompletion (preferable if it
    can include code I've done, not only know APIs), code refactoring
    (variable names, methods, etc), comment & uncomment.
-   Compilation management: Make integration (or other options like ant
    or maven for Java). Build automatically, "live" syntax error
    detection.
-   Bug tracking system integration
-   GUI editor

I know that I can do all of the above using Eclipse, and since this
Friday I know that some of them are also possible with Emacs, so now I'd
like to have some feedback:

What do you expect in an IDE? Is your list similar to mine? What is your
IDE of choice? Which special options of your IDE you use the most? Which
options are you most proud of?
