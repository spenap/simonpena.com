Title: Mind the Cascade
Date: 2009-02-24 20:33
Author: Simón
Category: Pennybank
Tags: CascadeType, deleted entity passed to persist, detached entity passed to persist, implementation, JUnit, model, test
Slug: mind-the-cascade
Status: published

Today I decided to go through the model layer, implementing as many
[JUnit](http://www.junit.org/ "JUnit.org") tests as I could, and
completing all the actions I hadn't implemented yet. As I said
[before]({filename}/pennybank/classifying-account-operations.md "Classifying account operations"),
I had just decided to stick to *one-category-at-a-time* scheme, having a
hierarchical relationship between categories.

I thought it would be easy: change the Category entity, check the *on
delete* and *on update* constraints in the database creation script,
refactor and go on.I also had in mind some refactor in my JUnit tests: I
have just two cases, one for each Facade, and several methods inside,
for each of the actions in that facade. But as the application was
getting larger and larger, I decided to have one JUnit case for each
Facade Method, with several test methods for each of the possible
scenarios I can think of.

So I was there, refactoring tests, moving some code to the
[*setUpBeforeClass*](http://junit.org/apidocs/org/junit/BeforeClass.html "@BeforeClass annotation")
and
[*tearDownAfterClass*](http://junit.org/apidocs/org/junit/AfterClass.html "@AfterClass annotation")
methods, when everything started to break:

**deleted entity passed to persist** and **detached entity passed to
persist**. After some research in Google, I understood what could be
causing the second error, so I solved it:

I was using an entity in a call to persist which had been "left"
unchecked by the entity manager (detached is the word, but I didn't know
it). I got the entity again by invoking *find*, and passed it fresh, and
it worked out.

But the first problem was harder. Google didn't shed any light on me
(apparently), as everything was about deleted entities which were still
referenced by others related to them. I didn't have any entity left:
this was happening in the *tearDownAfterClass* method, and I was
removing the entities left after the test. And then I realized that most
of the clean up was supposed to be done by cascading. So, maybe
[cascading](http://java.sun.com/javaee/5/docs/api/javax/persistence/CascadeType.html "CascadeType (JAVA EE 5)")
tags were incorrect. I checked out my classes, and I changed some of
them: putting the explicit ones instead of **CascadeType.ALL**. I still
have to test some of the *Update* methods, but for today, it's fixed.
