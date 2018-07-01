# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.

"""
This example demonstrates how to run a reverse proxy.

Run this example with:
    $ python reverse-proxy.py

Then visit http://localhost:8080/ in your web browser.
"""

from twisted.internet import reactor, protocol
from twisted.web import proxy


class ProxyFactory(protocol.ServerFactory):

    protocol = proxy.ReverseProxy

    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port

    def log(self, *args, **kwargs):
        pass



factory = ProxyFactory(b'www.asdf.com', 80)
reactor.listenTCP(8080, factory)
reactor.run()
