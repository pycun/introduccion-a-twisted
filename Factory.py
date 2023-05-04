from twisted.internet.protocol import Protocol, Factory
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet import reactor

# class Echo(Protocol):
#
#     def dataReceived(self, data):
#         self.transport.write(data)

class QOTD(Protocol):
    """
    Un protocolo Twisted maneja los datos de manera asíncrona. El protocolo responde a los eventos a medida que
    llegan desde la red y los eventos llegan como llamadas a métodos en el protocolo.
    """
    def connectionMade(self):
        """
        Cuando se lleve a cabo una conexión, mandaremos un mensaje
        :return:
        """
        self.transport.write("Welcome to TCP Server \n\n".encode())

    def connectionLost(self, reason):
        self.factory.numProtocols = self.factory.numProtocols - 1

    def dataReceived(self, data: bytes):
        """
        En este apartado es donde se maneja la información de forma asincrona. Puede devolverse informacion
        a partir del atributo `transport`

        :param data:
        :return:
        """
        print(data.decode())
        self.transport.write(F"Te reenviare lo que escribiste: {data.decode()}".encode())
        super().dataReceived(data)


class QOTDFactory(Factory):
    """
    El trabajo de esta clase, que hereda de Factory, es construir instancias de la clase `QOTD`
    Para ello, se sobre escribe el metodo `buildProtocol`
    """
    def buildProtocol(self, addr):
        return QOTD()


if __name__ == '__main__':
    # Implementa un servidor TCP con una configuración IPv4 en el puerto 8007
    # Podemos hacer la prueba desde ubuntu mandando informacion:
    #
    # telnet 127.0.0.1 8007 -> Esto generara una conexion
    endpoint = TCP4ServerEndpoint(reactor, 8007)

    # El codigo es orientado a Eventos, asi que cada que reciba un mensaje, se generará una instancia de la clase
    # `QOTD` debido al factory
    endpoint.listen(QOTDFactory())

    # Solo se debe ejecutar el run una sola vez dentro del codigo.
    # El reactor es el núcleo del bucle de eventos en Twisted, el cual, impulsa las aplicaciones que usan Twisted.
    # Es una construcción de programación que espera y despacha eventos o mensajes en un programa.
    # Funciona llamando a un "proveedor de eventos" (El factory), que generalmente se bloquea hasta que llega un evento
    # El reactor proporciona interfaces básicas a una serie de servicios, incluidas las comunicaciones en red,
    # el enhebrado y la despacho de eventos.
    reactor.run()
