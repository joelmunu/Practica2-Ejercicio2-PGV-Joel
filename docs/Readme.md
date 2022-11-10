# UD1-2 Generación de procesos en Python
## **Ejercicio 2**

Este programa permite realizar ping a una dirección IP o a un dominio indicado por el usuario.

El programa se encarga de identificar el sistema operativo en el que se está ejecutando utilizando **platform.system()**.

Si se está ejecutando en Linux o en MacOS (Darwin), ejecutará el comando ping de la siguiente forma: **ping -c 4 [host]**, de manera que sólo se envíen 4 paquetes como realizan los S.O. Windows por defecto.

> *Este programa es compatible con sistemas **Windows**, **MacOS** y **Linux***