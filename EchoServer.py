from twisted.internet import reactor
from autobahn.websocket import WebSocketServerFactory, \
                               WebSocketServerProtocol, \
                               listenWS
 
 
class EchoServerProtocol(WebSocketServerProtocol):
 
    def onMessage(self, msg, binary):
        print('Got Message: ' + msg)
        self.sendMessage(msg, binary)
 
 
if __name__ == '__main__':
    factory = WebSocketServerFactory("ws://localhost:9000", debug = True)
    factory.protocol = EchoServerProtocol
    listenWS(factory)
    reactor.run()