from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver
from twisted.internet import reactor

class Answer(LineReceiver):

    answers = {'How are you?': 'Fine', None: "I don't know what you mean"}

    def lineReceived(self, line):
        line = line.decode()
        if line in self.answers:
            self.sendLine(self.answers[line].encode())
        else:
            self.sendLine(self.answers[None].encode())


class AnswerFactory(Factory):
    """
    El trabajo de esta clase, que hereda de Factory, es construir instancias de la clase `QOTD`
    Para ello, se sobre escribe el metodo `buildProtocol`
    """
    def buildProtocol(self, addr):
        return Answer()


if __name__ == '__main__':
    # Esta es otra forma de correrlo.
    # El reactor necesita de un Factory, ya que cada evento/peticion se responde con una instancia de la clase Protocol
    # En este caso la clase `LineReceiver` hereda de `Protocol` pero tiene funciones que concatenan los bytes
    # recibidos en el puerto y permite la salida con salto de linea.
    reactor.listenTCP(8000, AnswerFactory())
    reactor.run()