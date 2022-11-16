# -*- coding: utf-8 -*-
# zato: ide-deploy=True

from zato.server.service import Service

class simTest(Service):
    """ Returns results of a simulation test.
    """
    name = 'api.pymath.tester'

    def handle(self):

        # Python dict representing the payload we want to send across
        import random

        # Create two random numbers
        num1 = random.random()
        num2 = random.random()

        # Build the payload
        payload = {'result-1':num1, 'result-2':num2, 'result-3':(num2*num1)}

        # Assign the returned dict to our response - Zato will serialise it to JSON
        # and our caller will get a JSON message from us.
        self.response.payload = payload