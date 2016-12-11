Title: Some (unasked) explanations
Date: 2009-03-07 17:11
Author: Simón
Category: Pennybank
Tags: design, Java, OS X
Slug: some-unasked-explanations
Status: published

When I started  developing PennyBank, the first decision I faced was the
programming language I should use. I wanted something that looked
integrated in the system, like iTunes, Mail, iCal... The first choice
was obviously
[Objective-C](http://en.wikipedia.org/wiki/Objective-C "Objective-C"),
with the interface done in [Interface
Builder](http://developer.apple.com/tools/interfacebuilder.html "Interface Builder").
I had followed a small tutorial, and doing a trivial application (a
calculator, I think) had showed me how good its visual programming was.

In my job I work using
[C\#](http://en.wikipedia.org/wiki/C_Sharp_(programming_language) "C# Programming Language")
with [Visual Studio
2008](http://msdn.microsoft.com/en-us/vstudio/default.aspx "Visual Studio").
I can develop
[GUIs](http://en.wikipedia.org/wiki/Graphical_user_interface "Graphical user interface")
real quickly, without having to withdraw time from what it is usually
more important: the business logic. Here, I wanted more or less the
same. I wanted a language which could let me focus on the logic without
too many headaches when doing the GUI. So Objective-C seemed the right
option, as there was that Interface Builder tool. But after just some
searches in Google, I realized that I wouldn't be able to get the
application done if I chose a language I was not familiar with.

And so I chose Java. I've done many small apps in Java when I was
studying, so I feel quite familiar with it. Besides, I wanted to try
[Hibernate](http://www.hibernate.org/ "Hibernate"), so this seemed a
very good excuse. The other reason to choose Java was SWT. Some friends
and I developed an application last year using
[SWT](http://www.eclipse.org/swt/ "The Standard Widget Tool"). We were
targeting Windows, but I recall reading that SWT was "the ultimate Java
interface" in terms of native [Look &
Feel](http://en.wikipedia.org/wiki/Look_and_feel "Look and feel")
integration. As our application got to look great in Windows, I started
coding in Java with the idea that SWT would save all my problems.

I was wrong. After two weeks developing the model layer with Hibernate,
I wrote the first lines of code for the GUI. It was quite strange: I
needed several days to notice that something was going wrong. The first
days it was due to the following:

> *The special VM option **`-XstartOnFirstThread`** is also required for
> SWT applications to run properly on the Mac.*

It is stated clearly in the [Mac OS X
section](http://www.eclipse.org/swt/macosx/ "Deploying SWT Applications on Mac OS X")
of their page, but somehow I didn't read it, experiencing some real
awful exceptions until I found it. After that, I had several issues that
almost have PennyBank development stopped. First of all was the lack of
a good Visual Editor in Eclipse. OK, there was the [Visual Editor
plug-in](http://www.eclipse.org/vep/WebContent/main.php "Visual Editor plug-in")
, but I wasn't able to get it working:  its support seemed to have been
dropped off, and there was no sign of activity in its section for the
last two years (Jump [here](#veplugin) if you don't want to read the
rest and want to find which solution I found). After that, I wrote the
first example of a toolbar.

It was... weird. I was looking at the main window, knowing that
something wasn't right, but unable to tell what it was. The toolbar!
This was NOT an OS X toolbar!After that, I knew that I had no reason to
keep using SWT, as it wasn't giving me the integration I was expecting,
nor it was giving me any ease of visual programming. I found a blog
where someone built an [unified tool bar using
SWT](http://blog.laurentm.com/2008/07/making-swt-look-more-native-on-mac-os/ "Making SWT look more native on Mac OS"),
but it looked too much of a hacking for me. So I moved to
[Netbeans](http://www.netbeans.org/ "Netbeans"): I knew it had a [tool
for writing
GUIs](http://www.netbeans.org/kb/trails/matisse.html "Matisse on Netbeans")
so even if I would be coding a *not-so-nice* application, at least it
would be faster.

Using [Maven](http://maven.apache.org/ "Maven") proved here to be a very
wise decision: migrating from an IDE to the other was painless. But I
didn't stay with Netbeans too much: after an strange problem with
Subversion, I moved back to
[Eclipse](http://www.eclipse.org/ "Eclipse"). At the beginning, I even
thought about developing the interface by hand. Fortunately, I found a
better solution.

<a name="veplugin"></a>Even if the plug-in was officially unsupported,
in [this
page](http://wiki.eclipse.org/VE/Update "Visual Editor plug-in") a link
is provided to have it working under the last Eclipse build. Now that I
was able to do visual programming, the only point missing was the so
much wanted operative system integration.

So I started searching for *"Java OS X integration"*, finding lots of
resources... until I found The One. [Exploding
Pixels](http://explodingpixels.wordpress.com/ "Exploding Pixels") writer
has developed [Mac Widgets for
Java](http://code.google.com/p/macwidgets/ "Mac Widgets for Java"): some
great widgets which gives the application a native look and feel.
Another *must have* link is the [Java Development Guide for Mac OS
X](http://developer.apple.com/documentation/Java/Conceptual/Java14Development/index.html "Java Development Guide for Mac OS X").
With this one and the [Apple Human Interface
Guidelines](http://developer.apple.com/documentation/userexperience/Conceptual/AppleHIGuidelines/index.html "Apple Human Interface Guidelines")
I think I have all the technical information I need.
