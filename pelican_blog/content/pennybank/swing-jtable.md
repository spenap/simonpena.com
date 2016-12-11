Title: Swing JTable
Date: 2009-03-15 01:15
Author: Simón
Category: Pennybank
Tags: implementation, Java, OS X, UI
Slug: swing-jtable
Status: published

I've been working hard these days, and I almost have an usable version
of PennyBank. Right now, users are able to create and delete users and
accounts, operate with those accounts (deposit, withdraw and transfer),
displaying account operations, and importing movements from
[Cashbox](http://www.fadingred.com/cashbox/ "Cashbox") PList files.

I will provide with some screen-shots as soon as possible, but today I
wanted to talk about Swing
[JTables](http://java.sun.com/docs/books/tutorial/uiswing/components/table.html "How to Use JTables")
and their
[TableModel](http://java.sun.com/docs/books/tutorial/uiswing/components/table.html#data "Creating a Table Model")
property. Tables are great tools when you need to display a collection
of data, so you can arrange it in rows (one row per element in the
collection) and columns (one column per attribute in the element).

JTables are quite easy to use. You need to declare the table itself,
give it a model, and display it in your panel. Depending on the model
you choose, you can edit the table's cells, you can display the elements
according to their type...

Even when Sun's tutorial is nice enough to have the basic necessities
solved, these three articles I found on
[InformIT](http://www.informit.com/ "InformIT") are very good pointing
at the changes you may probably want to do with your tables:

-   [Creating a Custom Java Swing
    TableModel](http://www.informit.com/articles/article.aspx?p=332278 "Creating a Custom Java Swing TableModel")
-   [Building a Professional Swing
    JTable](http://www.informit.com/articles/article.aspx?p=333472 "Building a Profesional Swing JTable")
-   [Sortable Swing
    JTable](http://www.informit.com/articles/article.aspx?p=337310 "Sortable Swing JTable")

Now, I still have to give my table the OS X standard Look & Feel,
painting even and odd rows with different colors each one. [This
link](http://nadeausoftware.com/articles/2008/01/java_tip_how_add_zebra_background_stripes_jtable "How to add zebra background stripes to a JTable")
provides some good steps to accomplish that task.
