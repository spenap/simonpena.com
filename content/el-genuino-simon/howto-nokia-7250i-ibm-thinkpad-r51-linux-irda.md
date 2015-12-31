Title: HOWTO: Nokia 7250i, IBM Thinkpad R51, Linux, IRDA
Date: 2006-10-15 16:05
Author: Simón
Category: El Genuino Simón
Tags: Informática
Slug: howto-nokia-7250i-ibm-thinkpad-r51-linux-irda
Status: published

Ya llevaba un tiempo pensando en conectar mi Nokia 7250i al portátil
desde linux. El motivo era que cada vez me funciona peor Windows: tarda
más en arrancar, se cuelga, y es un verdadero coñazo. El problema es que
no existe ninguna versión de la PC Suite de Nokia para Linux: si quieres
algo semejante, tienes que currártelo.

En mis primeras instalaciones de Debian y Ubuntu, nunca me preocupé por
los infrarrojos. Estaban ahí, y listo, pero como no me hacían falta, ni
probé que funcionaran. Este viernes estábamos en el laboratorio Edu,
Jorge y yo, y me acordé de pronto del móvil, y de lo interesante que
sería tenerlo en Linux.

Primeras aproximaciones: lo primero que hice fue

`$apt-cache search nokia`

Y apareció el famoso [gnokii](http://www.gnokii.org/), y el - para mí -
desconocido [kmobiletools](http://www.kmobiletools.org/). Siguiendo los
consejos de [Gervasio](http://www.picandocodigo.com), descarté este
último, y me lancé hacia gnokii. Pero el primer - y sencillo - paso,

`$gnokii --identify`

ya no me funcionaba: no encontraba nada. Resulta que era porque buscaba
en el puerto equivocado: tenía que indicarle que mirase en el de
infrarrojos. Y hala, a ver qué dispositivo es el de los infrarrojos.

En ese momento me di cuenta de que *igual no tenía instalado nada que
manejara los infrarrojos en mi sistema*. Y hala, a preguntar a google:
ibm thinkpad r51 irda. Apareció [este
señor](http://www.dw-itsecurity.de/r51/details/infrared.html),
comentando sus pasos para conseguirlo. Siguiéndolos no tuve ningún
problema: al cabo de un rato, y tras instalar *irda-utils*, y modificar
los archivos de configuración como él indica, **irdadump** mostraba los
siguientes resultados:

```
23:25:49.923195 xid:cmd 1f072b67 ffffffff S=6 s=0 (14)
23:25:50.006723 xid:cmd 1f072b67 ffffffff S=6 s=1 (14)
23:25:50.096708 xid:cmd 1f072b67 ffffffff S=6 s=2 (14)
23:25:50.186694 xid:cmd 1f072b67 ffffffff S=6 s=3 (14)
23:25:50.268933 xid:rsp 1f072b67 000020f7 S=6 s=3 Nokia 7250i hint=b125 [ PnP Modem Fax Telephony IrCOMM IrOBEX ] (28)
23:25:50.276682 xid:cmd 1f072b67 ffffffff S=6 s=4 (14)
23:25:50.366669 xid:cmd 1f072b67 ffffffff S=6 s=5 (14)
23:25:50.456654 xid:cmd 1f072b67 ffffffff S=6 s=* eireann hint=0400 [ Computer ] (23)
```

*¡Estupendo!* - me dije. Ya parecía que estaba todo listo. Y todo
confiado, ejecuté

`$gnokii --identify`  

Pero faltaba indicarle a gnokii que usara el puerto de infrarrojos: no
se iba a dar cuenta por sí sólo :P. Y hala, miré en internet un archivo
*.gnokiirc* de ejemplo, y ...

Decepción: tras un par de mensajillos interesantes, donde se detectaba
el móvil y una serie de datos relacionados, el programa se
*auto-abortaba*, indicando que mi modelo se le había congelado a otras
personas. (No mi modelo, sino otros que empleaban el mismo driver de
acceso). En fin, la cosa se ponía negra de nuevo.

El fin de semana me volví a poner a ello: miré un poco más en google, y
en vez de buscar por gnokii + 7250i, busqué mobile phone + linux. Y a lo
tonto, apareció [gammu](http://www.gammu.org). Inicialmente un fork de
gnokii, ahora un proyecto asentado y bastante serio. Estuve leyendo un
poco, y decían que soportaban mi móvil, aunque no ponían nada
específico. No hice nada el finde: aunque las fuentes ocupaban tan sólo
un mega, las posibles dependencias que habría que instalar me
desanimaron a intentarlo con mi conexión de **56kbps**.

Domingo de noche: descargo gammu, ejecuto
`$fakeroot make deb`, instalo dos de los *.deb* resultantes, ejecuto
`gammu --identify`, y ... plaf, el programa se cierra tras pocos
segundos. Hala, a google otra vez a buscar un
*[.gammurc](http://tuxmobil.org/nokia7250i_mobile_linux.html)*, que
resulta ser casi idéntico al *.gnokiirc* (lógico, habida cuenta que
gammu es un fork del primer proyecto). Lo cubro adecuadamente, ejecuto
de nuevo, y (censuro algunas cosas porque soy un paranoico :P):

```
Manufacturer  : Nokia
Model         : 7250i (NHL-4JX)
Firmware      : 3.22 C (23-06-03)
Hardware      : 1040
IMEI          : --
IMEI original : --
Fabricado     : 10/2003
Producto code : --
UEM           : 8
```

Los demás comandos los fui mirando poco a poco. Muy interesantes son
```
$gammu --getfilesystem  
$gammu --getfiles fileID [file2ID] [...]  
```

Y unos cuantos más que están bastante bien documentados ( pudiéndose
incluso recuperar el PIN a través de los infrarrojos ;) )

EDIT: La distro e incluso el portátil no son importantes a la hora de
conseguir que todo funcione. En una distro *tipo fedora*, sólo cambiaría
la manera de instalar los paquetes. Y en último caso, con bajarse los
correspondientes *tarball*... Lo mismo pasa con el hecho de que mi
portátil sea un Thinkpad: sólo influye a la hora de localizar el puerto
de infrarrojos, en la zona inferior izquierda.  
</span>
