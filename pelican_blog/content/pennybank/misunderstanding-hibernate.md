Title: Misunderstanding Hibernate
Date: 2009-03-01 11:30
Author: Simón
Category: Pennybank
Tags: CascadeType, Hibernate, implementation, JUnit, model, test
Slug: misunderstanding-hibernate
Status: published

These last days I've been doing more **JUnit** tests. And thanks to
them, I've discovered some serious misunderstanding I had about
**Hibernate**, **Cascading** (yes, again) and **ManyToOne**,
**OneToMany** relationships.

The first mistake I have was start coding too fast. I started following
a tutorial, but I confess that I focused too much on code, an little on
the theory. Following that tutorial I set a **OneToMany** relationship
between an *user* and his *accounts*. Somehow, I thought that the
*account* list in the *user* side would get filled
[automagically](http://en.wiktionary.org/wiki/automagically "automagically - Wiktionary"),
driven by the annotations I was using. As the accounts got dropped from
the database when I deleted an user, I thought everything was alright,
and I didn't think about too much.

Yesterday, doing some tests on the *category* entity, I found that in a
child-parent relationship, the child didn't have its parent *category*
updated when I deleted that parent *category*. In the database I had set
**"ON DELETE SET NULL"**, and looking at the database while performing
the tests showed that it was working there. But **Hibernate** didn't
seem aware of that behavior, and the link to the old parent *category*
still appeared in the child. That led me, after some tries, to
understand how cascading was supposed to work and how badly I was using
it. I had several cascading annotations in the **ManyToOne** side of
some relationships, which meant that when I made a change on the *many*
side, the other side was getting affected. And that wasn't the behavior
I was expecting!

I went to the documentation to learn how should annotations work, and
what did they mean according to the context they were used in. After
that, I removed most of my annotations, and made some changes, in the
*update* and *delete* methods in my *DAOs* to spread the changes when
that was needed.

Now, an *user* has a list of *accounts*. When an *account* is created,
it sets a reference to the *user* who has it. And makes that *user* add
it to his *account* list. When an *account* is deleted, it makes the
*user* remove it from the *account* list. As the *account* *operations*
have a reference to an *account*, **Hibernate** is responsible to update
that reference.

The *categories* behavior is similar. When a root *category* is created,
it creates an empty list of child *categories*. When you add a child
*category* to a parent *category*, you add that child to his parent
list. When deleting the parent, you have to go through the list,
updating all the references in his children. When deleting a child, you
have to remove it from his parent list.

After these changes, everything is working now. I know that some of the
tests I've done are too bound to my interpretation of the behavior they
have to show, and so they may be wrong. But at least I get rid of part
of the errors I still have.
