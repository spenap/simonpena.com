Title: Administrando sistemas, Firefox mobile y otras cuestiones
Date: 2010-02-01 01:51
Author: Simón
Category: Máster SW Libre
Slug: administrando-sistemas-firefox-mobile-y-otras-cuestiones
Status: published

El fin de semana tuvimos nuestras primeras clases de [Administración e
Integración de
Sistemas](http://www.mastersoftwarelibre.com/?page_id=242). Comenzamos
con una introducción a los [runlevels](http://wiki.debian.org/RunLevel),
a la manera en la que se organizan los servicios en sistemas tipo
[Debian](http://www.debian.org), a ver en qué orden se ejecutan, o qué
deberíamos hacer para añadir nuestros propios demonios. Algunas cosas ya
las sabía por haber trasteado en su día, otras me sonaban y de algunas
no tenía ni idea, pero desde luego, una de las cosas que definitivamente
agradecí fue la visión "didáctica", en vez de los clásicos tutoriales "a
lo bestia" que se suelen encontrar por Internet. Si a eso le añadimos
que nos pusieron deberes para entregar en 15 días (la semana que viene
es el
[FOSDEM]({filename}/master-sw-libre/fosdem-2010-there-we-go.md)),
ya tenemos una buena combinación que debería permitirme defenderme mejor
con el *bash scripting* :)

Además de los ejercicios que nos ponen, tengo un par de "picores" que me
apetecía solucionar: en mi
[Sheeva](/tag/sheeva-plug), si conecto un
disco duro por USB, tras un período de inactividad, éste se desmonta.
Hasta ahí todo normal, se supone que es un mecanismo de ahorro de
energía. Sin embargo, el problema viene cuando tras esos períodos de
actividad se intenta volver a acceder al disco: se produce un error de
entrada/salida. Entonces, el sistema vuelve a montar el disco en el
siguiente punto de montaje (de *sda1* pasamos a 2, 3 y así
sucesivamente) y se hace una comprobación del sistema de ficheros: se
suelen encontrar incoherencias, se corrigen, y listo. La solución que
tengo, que simplemente inhibe mediante una actividad periódica la
entrada en reposo del disco, es totalmente *"quick & dirty"*. Con lo que
nos enseñaron, debería poder hacer un demonio que realizase las debidas
comprobaciones, se ejecutase al inicio, e incluso estuviera atento a
eventos de conexión y desconexión del disco (esto todavía no sé cómo,
pero calculo que nos lo dirán :P)

En otro orden de cosas (siempre he querido decir esto), el sábado nos
entregaron en préstamo unas [Nokia
N810](http://www.nokia.es/productos/moviles/n810). Son el penúltimo
modelo de tablet de Nokia, corren Maemo4 - Diablo, y tienen teclado
integrado y GPS. Aunque el módulo de desarrollo para escritorio y
dispositivos móviles empieza todavía en unas semanas (podéis informaros
[aquí](http://www.mastersoftwarelibre.com/?page_id=273), además la
matrícula está todavía abierta), imagino que lo adelantaron para que
pudiésemos llevarlo al FOSDEM (tenemos que confirmar esto) y usarlo como
callejero inteligente (con los mapas del Benelux) y miniordenador
portátil, evitando cargar con cosas más pesadas e innecesarias.

Un detalle de las tablet que no sé si comenté es el soporte de la
fundación Mozilla. Ahora, en
[mozilla.com/m](http://www.mozilla.com/es-ES/m/), se puede descargar la
versión para Maemo de Firefox, compatible tanto con Maemo 4, como con
Maemo 5, en las nokia N900. ¿Ventajas sobre el navegador incluido por
defecto? La sincronización :). Un estupendo plugin, [Mozilla
weave](https://mozillalabs.com/weave/), que permite sincronizar los
marcadores, preferencias, pestañas, configuración… entre tu Firefox del
escritorio y el Firefox del tablet. Si no lo conocéis y tenéis la
posibilidad, ¡probadlo!
