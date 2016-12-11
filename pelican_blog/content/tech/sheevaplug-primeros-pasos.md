Title: SheevaPlug: Primeros pasos
Date: 2009-10-01 20:59
Author: Simón
Category: Tech
Tags: plug computing, sheeva plug
Slug: sheevaplug-primeros-pasos
Status: published

En esta entrada comentaré los primeros pasos que se aconsejan dar con el
SheevaPlug. Están tomados del [wiki
oficial](http://plugcomputer.org/plugwiki/index.php/Main_Page "PluWiki"),
concretamente de [New Plugger How
To](http://plugcomputer.org/plugwiki/index.php/New_Plugger_How_To "New Plugger How To")
y
[QuickStart](http://plugcomputer.org/plugwiki/index.php/QuickStart "QuickStart")
(principalmente la primera fuente), y traducidos. Aunque me referiré
inicialmente a la conexión por ssh, en principio no debería haber ningún
problema en ejecutar todos estos pasos desde el puerto serie.

**ATENCIÓN**: si copiáis y pegáis algo de lo que comento que vaya entre
comillas, aseguraos de que son las adecuadas. Es muy habitual que los
blogs sustituyan las comillas dobles por comillas literarias

1.  [Conectándonos al sheeva](#connecting)
2.  [Arreglando la instalación](#fixing)<a></a>
3.  [Actualizando la instalación](#updating)

<a name="connecting"></a>

Conectándonos al Sheeva
-----------------------

El SheevaPlug trae inicialmente un sistema Ubuntu instalado: [Ubuntu
9.04 "Jaunty
Jackalope"](https://wiki.ubuntu.com/JauntyJackalope "Ubuntu 9.04"). Para
comenzar a utilizarlo nos conectaremos al sistema por *ssh*, de modo que
habrá que enchufar el Sheeva a nuestra red. Los routers más habituales
traen configurado por defecto un servidor *dhcp*, con lo que al conectar
el sheeva a la red, ya obtendrá una ip.

Para consultar la ip asignada, podemos ir al menú de "Lista de clientes"
de nuestro router, o, con una herramienta como *nmap*, consultar todas
las ips de nuestra subred.

    tu_usuario@tu_ordenador:~$ssh root@ip_asignada

El **usuario** a utilizar es *root*, y la **contraseña**, *nosoup4u*.
Una vez dentro, es interesante cambiar este valor y poner el que más nos
interese, mediante el comando *passwd*.  
<a name="fixing"></a>

Arreglando la instalación
-------------------------

Lo primero que arreglaremos es la resolución de *DNS*. El cliente *DHCP*
está configurado para ignorar los servidores que indica el servidor, y
pretende resolver nombres localmente.  
Edita el archivo ***/etc/dhcp3/dhclient.conf*** y comenta o borra la
línea *"supersede domain-name-servers 127.0.0.1;"*

Actualiza las *DNS*:

    #dhclient eth0

Comprueba que funcione

    #ping kernel.org

El directorio ***/var/cache/apt/archives/partial***, usado por el
sistema de gestión de paquetes APT, está montado en la RAM, de modo que
se limpia en cada arranque. Sin embargo, aunque el fabricante incluye un
script para crear este directorio al inicio, el script no funciona
correctamente.

Edita ***/etc/rc.local***. Los dos comandos *insmod* fallan, y puesto
que la *shell* se invoca con el *flag -e*, el fallo en un comando
provoca que el *script* aborte su ejecución. Borra o comenta todas las
líneas salvo "***mkdir -p /var/cache/apt/archives/partial"***. Tras esa
línea puedes añadir la línea ***"/usr/sbin/ntpdate-debian"*** para
sincronizar tu reloj a través de internet. Tras finalizar la edición,
ejecuta el script.

    #/etc/rc.local

La zona horaria no está establecida: ejecuta el siguiente comando, y
selecciona la más apropiada:

    #dpkg-reconfigure tzdata

<a name="updating"></a>

Actualizando la instalación
---------------------------

Al llegar a este punto, en el wiki se recomendaba precaución. Suponemos
en todo momento que tenéis una conexión activa por ssh a vuestro Sheeva.
Pues bien, al finalizar la actualización del sistema, se recomienda
intentar establecer una nueva conexión sin cerrar la anterior: si algo
falla, es más sencillo solucionarlo. Cierto problema al modificar el
nombre de la máquina (*hostname*), combinado con la actualización del
sistema, podría impedir que os conectaseis. En [este
enlace](http://plugcomputer.org/plugforum/index.php?topic=110.0 "Ubuntu: apt-get upgrade makes logins fail")
se explica el problema con más detalle, y en
[este](http://plugcomputer.org/plugforum/index.php?topic=110.msg742#msg742 "Solución #1")
[otro](http://plugcomputer.org/plugforum/index.php?topic=110.msg1552#msg1552 "Solución #2")
se comenta como solucionarlo. De todos modos, yo no tuve ninguna
complicación en los siguientes pasos.

Primero: actualizar la lista de paquetes:

    #apt-get update

A continuación: actualizar la distribución

    #apt-get dist-upgrade

Por último, eliminar aquellos paquetes que no sean necesarios

    #apt-get autoremove

Al llegar a este punto, y antes de reiniciar, es cuando conviene
comprobar que podemos establecer una nueva conexión por *ssh*. Si todo
va bien, reiniciar.

    #reboot -h now

A partir de aquí, ya podemos instalar paquetes (*wget*, por ejemplo)
como en cualquier distribución basada en debian:

    #apt-get install wget

Teniendo presente en todo momento las limitaciones de espacio que nos
encontraremos.

En la siguiente entrada hablaré de cómo se actualiza el *kernel*. No es
una tarea especialmente difícil, y tiene también su entrada en el wiki
oficial: [Install Prebuilt
Kernels](http://plugcomputer.org/plugwiki/index.php/Install_Prebuilt_Kernels_From_sheeva.with-linux.com "Install Prebuilt Kernels").
Sin embargo, hay alguna diferencia entre el proceso actual y el descrito
allí, y puedo aportar la solución a ciertos problemas por los que ya
pasé :)
