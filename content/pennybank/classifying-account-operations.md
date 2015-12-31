Title: Classifying account operations
Date: 2009-02-23 16:06
Author: Simón
Category: Pennybank
Tags: classifying, design, model, operations
Slug: classifying-account-operations
Status: published

One of the things that made me start coding PennyBank was the idea of
classifying account operations in various ways. I first thought about
using categories, and letting the user add several ones to an account
operation. That could be quite flexible, but after some time thinking, I
realized that an account operation is most times classified in just one
category: another question is if that category is a subcategory of
another one more general.(If I buy a video game, this could be
classified in the *"video games"* category, in the *electronic* category
or even in a more general *"spare time"*. But it appears to me that
there is a hierarchy relationship between those categories )

Having just one category  looked enough for me, until I realized that
sometimes you may want to highlight, someway, an operation. And that
could be done using *tags*. They should be different from categories,
being a more specific way to filter operations, but making easier to
develop the application core.

So, right now, this is the selected choice. One operation could be
categorized or not, but should be classified in just one category.
Categories, themselves, can be arranged hierarchically. And finally,
operations can be tagged with multiple tags.
