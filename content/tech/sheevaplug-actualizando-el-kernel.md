Title: SheevaPlug: Actualizando el Kernel
Date: 2009-10-04 21:00
Author: Simón
Category: Tech
Tags: plug computing, sheeva plug
Slug: sheevaplug-actualizando-el-kernel
Status: published

Actualizando el kernel
----------------------

Para actualizar el kernel, los pasos a seguir también están
perfectamente detallados en el wiki: [Install Prebuilt Kernels From
sheeva.with-linux.com](http://plugcomputer.org/plugwiki/index.php/Install_Prebuilt_Kernels_From_sheeva.with-linux.com "Install Prebuilt Kernels From sheeva.with-linux.com").
En primer lugar, deberemos conectarnos al SheevaPlug mediante puerto
serie. En esta página se indican diferentes posibilidades [Serial
terminal
program](http://plugcomputer.org/plugwiki/index.php/Serial_terminal_program "Serial terminal program").
Por mi parte utilicé *screen* del siguiente modo (el primer parámetro es
el dispositivo reconocido como puerto serie, y el segundo, la velocidad
de la conexión):

    tu_usuario@tu_maquina:~$screen  /dev/ttyUSB0 115200

Al pulsar una tecla, debería aparecer un *prompt*

    login:

Introducimos ahí el usuario *root* y su *contraseña*, y entramos.
Instalamos *wget* si no lo habíamos hecho ya:

    #apt-get install wget

Guardamos el archivo
[README](http://sheeva.with-linux.com/sheeva/README-2.6.31) desde
[sheeva.with-linux.com](http://sheeva.with-linux.com/sheeva/).
(Posiblemente haya kernels más recientes cuando leas este post).

    #wget http://sheeva.with-linux.com/sheeva/README-2.6.31

Según la entrada en el wiki, se debe modificar el archivo
***/etc/sysctl.d/10-process-security.conf***, y ***vm.mmap\_min\_addr***
debe valer ***32768***. Según la página, no realizar ese cambio
inhabilitaría cualquier acceso distinto del puerto serie.

    #vi /etc/sysctl.d/10-process-security.conf

Añade la siguiente línea

    vm.mmap_min_addr = 32768

Dale permisos de ejecución al archivo descargado:

    #chmod +x README-2.6.30.6

Ejecútalo para descargar y escribir los módulos e imagen del kernel.

    # ./README-2.6.31
    Use --nandkernel to write kernel to NAND
    Or  --rootkernel to write kernel to /boot

En este punto, los nuevos *scripts* README no permiten la ejecución sin
argumentos: debe especificarse *--nandkernel* para escribir en la NAND,
o *--rootkernel* para escribir en la partición */boot*. Si escoges la
primera opción, se sobreescribirá el kernel que trae el Sheeva por
defecto. Si escoges la segunda, deberás referenciar la ubicación del
nuevo kernel en los parámetros de arranque. Yo empleé la primera opción,
así que desconozco como indicar la ruta requerida por la segunda: si vas
a seguir ese camino, consulta en el [foro
oficial](http://plugcomputer.org/plugforum/index.php?action=forum "PlugForum")

    #./README-2.6.31 --nandkernel

Reinicia

    #shutdown -r now

Ahora, cuando el SheevaPlug comience a cargar, debes pulsar alguna tecla
para interrumpir el proceso. Entrarás en un prompt interactivo (la
consola de *uBoot*), donde podrás modificar los parámetros de la carga.

Lo primero:

    set mainlineLinux yes

A continuación

    set arcNumber 2097

Ahora debes obtener los parámetros de arranque actuales y anotarlos,
para su posterior modificación

    printenv bootargs

A la ristra de información que te devolverá, deberás añadirle
***rootfstype=jffs2***. También deberás sustituir ***nand\_mtd*** por
***orion\_nand***. El resto debe permanecer igual. Es decir, si tenías

    parametro1=valor1,valor2 parametro2=valor1,valor2 parametro3=nand_mtd

Tu nuevo bootargs deberá ser

    rootfstype=jffs2 parametro1=valor1,valor2 parametro2=valor1,valor2 parametro3=orion_nand

(Y deberás establecerlo mediante)

    set bootargs la ristra de parámetros modificada

Una vez hayas acabado de modificar los valores, teclea

    saveenv

Y reinicia:

    resest

En el siguiente arranque, el nuevo Kernel debería utilizarse.

¿Qué hacer si algo falla?
-------------------------

Lo primero, mantener la calma. Si utilizas --rootkernel por error,
modificas los parámetros en uBoot pero no configuras la dirección de tu
imagen en la variable boot\_cmd, el mecanismo de arranque no será capaz
de arrancar la imagen antigua con la nueva configuración.

Lo más sencillo es restaurar estas variables a sus valores anteriores,
reiniciar usando la imagen antigua, e instalar el kernel en la *NAND*.

En [Factory Default u-Boot
Environment](http://plugcomputer.org/plugwiki/index.php/Factory_Default_u-Boot_Environment)
se indica el valor de las variables de *uBoot* en un sistema original,
de fábrica: si solo habéis modificado esas dos variables, id a la
segunda sección. Si habéis metido mano de un modo más general, en la
primera sección se explica cómo resetear por completo la configuración.
