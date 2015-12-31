Title: "Hacking" Blogger
Date: 2006-07-26 11:20
Author: Simón
Category: El Genuino Simón
Tags: Blogger, Informática
Slug: hacking-blogger
Status: published

Ya empiezo a tener el blog a mi gusto :). Empecé cambiando simplemente
el idioma en la plantilla, actualizando los enlaces a otros blogs,
poniendo el contador de visitas (que por ahora muestra un número de
visitas exagerado, y a todas luces provocado por mis ediciones y
previsualizaciones :P), y la sección de *artistas favoritos*, una imagen
generada en [Last.fm](http://www.last.fm) con mis artistas más
escuchados a lo largo de la semana.

Luego vi que quedaban algunas cosillas por hacer: el bloque de mi perfil
se veía todavía en inglés, con un *About Me* de lo más fuera de sitio. Y
se me ocurrió que quizás hubiera alguna manera de cambiarlo. Así que me
puse a mirar un poquillo, y llegué aquí: [Hacking
Blogger](http://help.blogger.com/bin/topic.py?topic=8932) (o *Los Pirateos de Blogger*, como reza la
traducción).

**Cambiando la cabecera "*About Me*" **

Resultó ser muy sencillo. Añadir una línea a la sección de las
<abbr title="Cascading Style Sheets">CSS</abbr>:

`#profile-container h2.sidebar-title {display:none;}`

De ese modo, la cabecera por defecto ya no se muestra. Y añadiendo
ahora  
`<!-- Begin #profile-container --><h2 class="sidebar-title">Acerca de mí</h2><$BlogMemberProfile$>`

conseguía poner una cabecera personalizada.

Luego seguí mirando, a ver si había algún otro *hack* sencillito que aplicar al blog,
y que aportase alguna funcionalidad interesante. Pensé en emplear
categorías, como explican en [Anything
Else](http://nerdierthanthou.nfshost.com/2006/01/introducing-labelr.html),
pero al ser beta, y haberse que registrar mediante un mail, o un
comentario en su blog, me pareció complicarme demasiado la vida, *por ahora*. Buscando un poco más,
apareció esto: [How can I create expandable post
summaries?](http://help.blogger.com/bin/answer.py?answer=42215&topic=8932),
para crear entradas relativamente largas, pero mostrar sólo un pequeño
avance en el blog.

**Probando *"expandable post summaries"* **

Intenté aplicar primero la técnica que comentaban en la página de ayuda
oficial, pero el enlace *leer más* aparecía en todas las entradas, no sólo en las que fuesen
grandes. En la página de ayuda decían, muy simpáticos, que modificar ese
comportamiento quedaba como ejercicio para el usuario. Pero vamos, no
debía ser trivial porque aparecía en más de una duda de los [grupos de
correo](http://groups.google.com/group/blogger-help?lnk=gschg). Mirando
algo más, apareció la página de un español que afirmaba haberlo
logrado,[Resumen Expandible
Inteligente](http://mentoliptus.blogspot.com/2005/02/resumen-expandible-inteligente_04.html).
Sin embargo, yo no conseguí que funcionara, y varios comentarios
presentes en esa misma entrada parecían apuntar a que a bastante gente
tampoco. Y tampoco se le veía emplearlo a él en su propio blog :P.

¿De dónde lo saqué al final? De la misma página de las categorías: [I
did it!](http://nerdierthanthou.nfshost.com/2004/10/i-did-it.html),
dice, y la verdad es que tiene motivos para alegrarse: acaba de
conseguir algo muy útil.

Bueno, espero que cualquiera que vaya a personalizar su blog y busque
modificar estas cosillas lo tenga algo más fácil ahora. No es que haya
descubierto nada nuevo, pero sí lo he recopilado, y también puede
resultar útil ;).
