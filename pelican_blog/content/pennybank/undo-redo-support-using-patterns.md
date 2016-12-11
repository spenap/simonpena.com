Title: Undo, redo support using patterns
Date: 2009-04-11 10:49
Author: Simón
Category: Pennybank
Tags: Command Pattern, Composite Pattern, design, implementation, Template method Pattern
Slug: undo-redo-support-using-patterns
Status: published

This Easter Week has been very productive. Although I didn't upload the
screenshots as I said, I've made several interesting improvements.

-   The delete menu item changes according to the current user interface
    selection. If an account is selected, it displays *delete account*.
    If an user is selected, it displays *delete user*, and if an account
    operation is selected, it displays *delete account operation*.
-   It is possible to undo/redo the actions made. The major improvement
    I pointed out on the previous post is almost done, so you can
    reverse the addition, edition and deletion of users, accounts and
    account operations.

I've made a new hierarchy in the controller layer. I created the
interface
[UIAction](http://code.google.com/p/pennybank/source/browse/trunk/src/main/java/com/googlecode/pennybank/swing/controller/actions/UIAction.java "UIAction.java"),
with methods *execute*, *undo*, *redo* and *getName*. I created an
abstract implementation,
[GenericAction](http://code.google.com/p/pennybank/source/browse/trunk/src/main/java/com/googlecode/pennybank/swing/controller/actions/GenericAction.java "GenericAction.java"),
where I made *final* those methods -to avoid the concrete classes
reimplementing them-, calling *doExecute*, *doUndo,* *doRedo* and
*doGetName* (which currently doesn't make much sense), followed by a
call to update (a private method which updates the information displayed
on the main window).

The do*Wathever* methods are *protected* and *abstract*, so the actions
extending GenericAction must override them. This way, each action
implements its own behavior for that methods, but at the same time
complying with the generic behavior without the an explicit call to
*super*. It follows the [Template method
pattern](http://en.wikipedia.org/wiki/Template_method_pattern "Template method pattern").

Besides, I made a
[CompositeAction](http://code.google.com/p/pennybank/source/browse/trunk/src/main/java/com/googlecode/pennybank/swing/controller/actions/CompositeAction.java "CompositeAction.java")
class, following the [Composite
pattern](http://en.wikipedia.org/wiki/Composite_pattern "Composite pattern"),
so several actions can be grouped into another.

This way, all the defined actions are commands, and the application
itself has the responsibility of executing them. Whenever an action is
executed, it is stored in an *undoable actions stack*, and its name is
set in the edit menu, so you can read "Undo *actionName*". If you undo
the action, the application takes it out from the stack, invokes its
*undo* method, and adds it to the *redoable actions stack*. After that,
its name will appear in the edit menu, displaying "Redo *actionName*".
Again, if you redo the action, the application takes it out from that
stack and invokes its *redo* method, adding it again to the *undoable
actions stack*. And over and over again (as far as it is well
implemented).
