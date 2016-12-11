Title: Respuestas a los lectores: Capítulo 1
Date: 2007-06-01 05:51
Author: Simón
Category: El Genuino Simón
Tags: Peticiones de Lectores, Sinsentidos
Slug: respuestas-a-los-lectores-capitulo-1
Status: published

Si os fijasteis alguna vez, en la parte inferior de mi blog hay un
contador de visitas. Quizás las cifras parezcan algo exageradas, pero os
prometo que no soy yo (tengo puesta tanto una cookie para identificarme
como webmaster, como bloqueadas las ips desde las que me conecto).
Entonces, ¿de dónde salen esas casi 7000 visitas en 10 meses?
Básicamente tengo unas 6 visitas diarias de cuota fija, de **returning
visitors**, siendo las otras 20 visitas diarias gente que se pierde por
google.  
Claro: decir que se pierden, y no poner nada más quedaría muy soso, y
ahí entra la utilidad de las herramientas de
[StatCounter](http://www.statcounter.com). Donde mejor
me lo paso es con *Recent Keyword Activity*, que me permite ver qué
términos de búsqueda traen a la gente a mi blog. El *ganador* de hoy, y
al que le dedicaré lo que queda de entrada, es el siguiente:


*algo sencillo pasos para vender mi alma al diablo*

Tal y como lo piden, parece imposible negarse a dar un pseudocódigo que
pueda conseguir que uno venda, con éxito, su alma al diablo.

-   Lo primero, una serie de comprobaciones rutinarias: debe existir el
    alma, y no debe estar vendida todavía.
-   Si superamos estas comprobaciones habrá que ponerse en contacto con
    el diablo, y nos surge la primera decisión importante: ¿TCP o UDP?
    Con TCP nos aseguramos que le lleguen nuestros mensajes, pero UDP
    nos permitiría una mayor velocidad en la comunicación, al no saturar
    la conexión con el control de errores y demás. Yo sugiero que
    empleemos UDP, y en caso de tener problemas de pérdida de mensajes,
    adaptar el algoritmo y emplear TCP.
-   Una vez seleccionado el protocolo, tendremos que conectarnos con el
    diablo. Un alias conocido para realizar esta conexión , y que ya se
    encarga el compilador de traducir convenientemente, es
    &lt;satan@hell:666\&gt; ( Satan at Hell ). A continuación, se establece
    la comunicación ( su especificación viene muy bien detallada en el
    [RFC 666](http://www.faqs.org/rfcs/rfc666.html)) Recuerdo que es
    necesario cubrir una serie de campos obligatorios: qué se pide a
    cambio del alma y cuándo se entregará ésta. El diablo debería
    contestar confirmando esas peticiones, y, en un campo de tamaño
    variable, con su propia letra pequeña. Llegado a este punto de la
    conexión, un ACK será suficiente para dar por finalizado el
    acuerdo.&lt;/666&gt;
-   Una vez establecido el acuerdo por el alma, debemos marcar esta como
    vendida ( con un simple flag será suficiente), y comenzar a
    disfrutar de las nuevas oportunidades que nos han sido dadas.

**NOTA:** una vez entregada el alma (cuando se hace efectiva la parte
del diablo), es necesario dejar el puntero dirigido a NULL, para que
cualquier otro subprograma que haga uso de ella no acceda a direcciones
entonces prohibidas.

Queda como ejercicio para el lector adaptar este pseudocódigo de modo
que se pueda vender el alma a cualquier otro ente, o no necesariamente
el alma, sino quizás algún otro órgano. Para ello, simplemente es
necesario modificar la parte dependiente del protocolo de venta con el
diablo (RFC 666), que, si hemos sido cuidadosos, habremos diseñado en un
pequeño módulo aparte.

Por cierto, este software no ha sido probado, y se distribuye *AS IS*,
no haciéndose responsable *el menda* de los efectos no deseados que
pudiera tener su uso.
