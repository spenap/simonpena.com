Title: Hibernate common errors
Date: 2009-02-27 15:43
Author: Simón
Category: Pennybank
Tags: deleted entity passed to persist, detached entity passed to persist, errors, Hibernate, id to load is required for loading
Slug: hibernate-common-errors
Status: published

Just two days after I
[blogged]({filename}/pennybank/mind-the-cascade.md "Mind the Cascade")
[about]({filename}/pennybank/testing.md "Testing...")
the errors **deleted entity passed to persist**, **detached entity
passed to persist** and **id to load is required for loading**, some
people came here from web searches.

As I'm not sure if those explanations were clear enough, I'll try to
synthesise here:

-   **Deleted entity passed to persist**. One entity, supposed to be
    deleted, is still referenced / accessed. In my case, I had a problem
    with "*cascading*". The behavior I expected was "**on delete
    cascade**" and "**on update cascade**". I have those constraints
    well in the database, but they weren't right in the Hibernate
    annotations. After I changed that, the error stopped. While I was
    searching why I was getting this error, I've seen people whose
    problem was different. They had, let's say, a list of entities.
    Those entities were related to others, and, when deleting, they had
    to take care of deleting both the link and the persisted entity.
    This was the most common scenario of this problem, and is better
    explained
    [here](http://schuchert.wikispaces.com/Ejb3+Tutorial+3+-+Finish+Conversion "Ejb3 Tutorial 3 - Finish Conversion"),
    for example.
-   **Detached entity passed to persist**. One entity, which is supposed
    to be up to date but is not, is passed to persist. In my case, I was
    trying to create an entity (an Operation), related to another (the
    Account where that Operation was taking place). The persist action
    was failing because my version of the Account was incorrect. The
    solution was just to update the entity.
-   **Id to load is required for loading**. Trying to access an entity
    without giving an actual identifier. In my case this was the easiest
    problem: I was calling *find* passing a non initialized long.
    Passing the correct, initialized values fixed the problem.

