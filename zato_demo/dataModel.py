# -*- coding: utf-8 -*-
# zato: ide-deploy=True

# stdlib
from dataclasses import dataclass

# Zato
from zato.server.service import Model, Service

# ###########################################################################

@dataclass(init=False)
class GetClientRequest(Model):
    client_id: int

@dataclass(init=False)
class GetClientResponse(Model):
    name:    str
    email:   str
    segment: str

# ###########################################################################

class GetClient(Service):

    class SimpleIO:
        input  = GetClientRequest
        output = GetClientResponse

    def handle(self):

        # Enable type checking and type completion
        request = self.request.input # type: GetClientRequest

        # Log details of our request
        self.logger.info('Processing client `%s`', request.client_id)

        # Produce our response - in a full service this information
        # will be obtained from one or more databases or systems.
        response = GetClientResponse()
        response.name    = 'Jane Doe'
        response.email   = 'hello@example.com'
        response.segment = 'RNZ'

        # Return the response to our caller
        self.response.payload = response

# ###########################################################################