Title: Testing...
Date: 2009-02-25 22:12
Author: Simón
Category: Pennybank
Tags: id to load is required for loading, implementation, JUnit, model, test
Slug: testing
Status: published

Today I spent all the afternoon testing. It may seem a tedious task, but
after a while it gets quite challenging: you know there are errors in
your code, so the objective is finding them. And while doing those
tests, correcting the actions which showed wrong, I implemented some new
ones.

The application is getting closer and closer to an usable state, and I
expect it to be running in about two or three weeks.

Today's odd error was a lot easier than the others: **id to load is
required for loading**. Maybe not the most complete description, before
you find the place it is failing, but good enough once you go to the
correct line number. I was using some fields in an Action which I
haven't initialized yet. D'oh!
