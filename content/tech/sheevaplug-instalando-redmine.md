Title: SheevaPlug: Instalando Redmine
Date: 2009-11-24 21:23
Author: Simón
Category: Tech
Tags: plug computing, Redmine, sheeva plug
Slug: sheevaplug-instalando-redmine
Status: published

Más vale tarde que nunca, espero, así que voy a comentar un par de
detalles sobre la instalación de [Redmine](http://www.redmine.org/) en
el SheevaPlug. Redmine es una estupenda herramienta de gestión y
seguimiento de proyectos, y en mi caso pretendo usarlo tanto para
prácticas realizadas durante la carrera como para pequeños proyectos en
fase de "incubación".

Para la instalación de Redmine he seguido varios documentos de
referencia: este tutorial en PDF de [instalación de Redmine en
Debian](http://www.redmine.org/attachments/2402/Redmine_Installation_on_Debian_v1.1.pdf),
obtenido del [foro de
Redmine](http://www.redmine.org/boards/1/topics/5630 "Install Redmine on Debian");
la propia documentación oficial de [instalación de
Redmine](http://www.redmine.org/wiki/1/RedmineInstall) y el apéndice de
[creación automática de repositorios
SVN](http://www.redmine.org/wiki/redmine/HowTo_to_handle_SVN_repositories_creation_and_access_control_with_Redmine).
Más reciente (noviembre de 2009) es este artículo de la documentación de
Redmine, que cubre la [instalación de Redmine en
Ubuntu](http://www.redmine.org/wiki/1/HowTo_Install_Redmine_in_Ubuntu).

Pasos previos
-------------

Redmine está desarrollado con [Ruby On Rails](http://rubyonrails.org/).
Soporta diferentes configuraciones de bases de datos, e incorpora un
servidor web propio. En mi caso, decidí emplear Apache y MySQL. En
teoría es posible utilizar [lighttpd](http://www.lighttpd.net/) como
servidor web (ver, por ejemplo,
[estos](http://howto.landure.fr/gnu-linux/debian-4-0-etch-en/install-the-redmine-project-management-application-on-debian-4-0-etch)
[tres](http://blog.josefsson.org/2008/10/17/redmine-on-debian-lenny-using-lighttpd/)
[enlaces](http://www.hiddentao.com/archives/2008/12/06/redmine-svn-mysql-5-lighttpd-15/)),
y cualquier otra base de datos (SQLite incluida) para almacenamiento.

Al crear las tablas que usaría Redmine encontré un problema: se me
denegaba el acceso como usuario root. Al parecer es un bug común entre
los usuarios del SheevaPlug, y estos dos enlaces me permitieron
solucionar el problema: [How to install mysql on a
SheevaPlug](http://plugcomputer.org/plugforum/index.php?topic=70.0) y
[MySql: Access denied for user
'root'@'localhost'](http://anojrs.blogspot.com/2007/11/access-denied-for-user-rootlocalhost.html).
Este debería ser el único problema en este proceso.

Instalación de Redmine
----------------------

A continuación, se pueden seguir los tutoriales que comentaba antes
([instalación de Redmine en
Debian](http://www.redmine.org/attachments/2402/Redmine_Installation_on_Debian_v1.1.pdf)
e [instalación de Redmine en
Ubuntu](http://www.redmine.org/wiki/1/HowTo_Install_Redmine_in_Ubuntu)),
limitándonos a copiar y pegar los comandos indicados. Es importante
escoger bien entre **entender los comandos e introducirlos manualmente**
o **copiarlos directamente sin pensar**. Ambas son opciones válidas, el
problema es (ay, como en todo) mezclar. Las dos líneas que siguen me
dieron muchísimos problemas: pensé que eran iguales, y las puse a mano.
Y claro, una cosa es el acceso y otra la autenticación.

    PerlAccessHandler Apache::Authn::Redmine::access_handler
    PerlAuthenHandler Apache::Authn::Redmine::authen_handler

Instalación y configuración de subversion
-----------------------------------------

Para integrar nuestra instalación de subversion con Redmine, volvemos a
los tutoriales que comentaba antes: [automatización de la creación de
repositorios](http://www.redmine.org/wiki/redmine/HowTo_Automate_repository_creation)
y [gestión de acceso a los repositorios mediante
apache](http://www.redmine.org/wiki/redmine/Repositories_access_control_with_apache_mod_dav_svn_and_mod_perl).
De ese modo, al crear un proyecto, se creará su repositorio
automáticamente (pasado el tiempo que indiquéis en el crontab). Los
accesos que hagáis al repositorio a través de Apache comprobarán si
estáis autorizados para verlo.

Importando contenido de un repositorio ya existente
---------------------------------------------------

En caso de que tuvierais algún repositorio funcionando previamente y
estéis migrando la instalación a Redmine, quedaría por importar el
antiguo contenido. Para eso nos guiaremos por [Moving a Subversion
Repository to Another Server](http://www.petefreitag.com/item/665.cfm).
Básicamente, para cada repositorio que queramos preservar, haremos:

    svnadmin dump /path/to/repository > repo_name.svn_dump

A continuación, si no hemos creado el repositorio automáticamente con el
mecanismo automático, lo haremos mediante

    svnadmin create /path/to/repository

Y realizaremos la importación tecleando

    svnadmin load /path/to/repository < repo_name.svn_dump
