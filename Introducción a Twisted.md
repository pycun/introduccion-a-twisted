# Introducción a Twisted

> Mas información: https://twisted.org/

---


### ¿Que es concurrencia?

Se refiere a la capacidad de un sistema para realizar varias tareas simultáneamente, pero no necesariamente en el mismo momento.

![image](https://user-images.githubusercontent.com/56737987/234992126-fd4f9209-ea92-4d8d-bfe3-1cb5b78749cc.png)

- El sistema puede alternar entre las diferentes tareas para lograr un efecto de paralelismo. 
- Se puede lograr a través del uso de  (threads) o (multiprocessing).

---

## ¿Que es asincronismo?

Es una **técnica de programación** que permite que un programa realice varias tareas al mismo tiempo, **sin tener que esperar a que una tarea se complete** antes de pasar a la siguiente.

![image](https://user-images.githubusercontent.com/56737987/234993407-232f8e30-6030-41e4-937c-5d2014c85c3f.png)

> "PAUSAR CODIGO PARA EJECUTAR OTRO"

La programación asíncrona es muy útil en situaciones en las que el tiempo de espera de una tarea puede ser desconocido o variable, como:

- Comunicación con bases de datos
- Servicios web (API)
- Servicios de Red (TCP/UDP/FTP/SSL)
- Operaciones de entrada/salida (Leer y escribir archivos)


## ¿Que es asyncio?

**Biblioteca para programación asíncrona** que fue agregada a Python en la versión 3.4

- Utiliza un bucle de eventos (asyncio.run())
- Utiliza corutinas para pausar y continuar las ejecuciones
- Uso de API para hacer mas facil la implementacion de codigo

Para entender cómo funciona asyncio, debemos entender qué son los **corutinas**. Las corutinas son una forma de estructurar nuestro código para que pueda ser **pausado y reanudado** en un momento posterior. Esto nos permite ejecutar varias corutinas al mismo tiempo en un solo hilo de ejecución. ¿Como?

### async

![image](https://static.wikia.nocookie.net/simpsons/images/e/e0/Mapple_Lisa.png/revision/latest?cb=20160518003943)

La palabra clave async def se utiliza para definir una función asíncrona que puede ser suspendida y reanudada en cualquier momento durante su ejecución. 

### await

![image](https://media.tenor.com/sP7QDKkRQ7kAAAAC/wait-for-it-simpsons.gif)

Se utiliza para suspender temporalmente la ejecución de la función hasta que se complete una operación de entrada/salida


## ¿Que es Twisted?

![image](https://imagenes.20minutos.es/files/og_thumbnail/uploads/imagenes/2021/09/02/meme-de-la-caida-de-instagram.jpeg)

Es una biblioteca de Python para **escribir código asíncrono en red**.Podemos escribir programas que se comuniquen con otros dispositivos o servicios a través de la red de forma asíncrona, sin tener que esperar a que una operación de entrada o salida se complete antes de procesar otra.

- Utiliza un bucle de eventos (reactor.run())
- Monitorea "file descriptors" para detectar eventos de entrada y salida  (identificador numérico utilizado por el sistema operativo)
- Cuando el evento ocurre, se llama a la funcion que responda al evento.


### Patron de diseño REACTOR

Patrón de diseño de software utilizado para manejar la concurrencia en aplicaciones de red. Su objetivo principal es permitir que una aplicación de red maneje múltiples solicitudes simultáneamente de manera eficiente y escalable.

### Patron de diseño FACTORY

patrón de diseño creacional que permite crear objetos sin especificar su clase concreta y delegando la creación a subclases

## ¿Que podemos implementar?

Proporciona una amplia variedad de herramientas y servicios para el desarrollo de aplicaciones de red en Python, como:

- Servidores TCP/UDP
- Clientes TCP/UDP
- aplicaciones web, 
- aplicaciones de correo electrónico, 
- aplicaciones de transferencia de archivos, entre otros.
