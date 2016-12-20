# Ejercicio 1 #
Este ejercicio funciona en un servidor Arch Linux de 64 Bits, los certificados son autofirmados.	

# Ejercicio 2 #

El ejercicio se ha realizado en un Arch Linux de 64 Bits, con una instalacion de python2, junto con rabbitmq y celery. Todo instalado desde el gestor de paquetes Pacman. Celery se ha mantenido vivo mediante el comando :
```shell
celery2 -A ejercicio2 worker -l info
```
El comando de django es :
```shell
./manage.py celery --dest RUTA_DEL_FICHERO
```
