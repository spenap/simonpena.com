Title: Keep working hard
Date: 2009-04-05 18:02
Author: Simón
Category: Pennybank
Tags: Command Pattern, embedded database, H2 database, implementation
Slug: keep-working-hard
Status: published

It's been a while since the last post, and some improvements have been
made. I've added a context menu both to the navigation panel and the
account operation table, and it is now possible to rename, edit and
delete accounts, and edit and delete account operations. I've fixed the
account operations table filters, so you can search within the comments
and categories (or both) of the account operations. The field to be
searched is selected in a search text box just like iTunes'.

The menu bar isn't completed yet: there are several operations which
can't be accessed from there. But as the listeners and actions are made
for the context menu, the work left is reduced to bind those actions to
the main menu items.

The next major change involves re-factoring some of the actions, so the
[Command
Pattern](http://en.wikipedia.org/wiki/Command_pattern "Command pattern")
can be introduced: support for undo and redo should is the next target.

There's still another thing I have to put hours in: improving the
application installation and configuration. Right now it involves
downloading Maven, MySQL and JTA, and installing and configuring them.
Several weeks ago I found [H2
Database](http://www.h2database.com/ "H2 Database"), and how easy it was
to install and use it. I think it would be a lot easier for the final
user to have his data in an embedded database, so the task left for me
is to figure how to select the database placement, choose if that
placement is a permanent one or can be changed even on runtime, and if
it would even be possible to change between an embedded database or a
server one.

I'm not sure which option should I prioritize... We'll see. And I'll
upload some screenshots someday within this week.
