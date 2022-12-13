# -*- coding: utf-8 -*-
# zato: ide-deploy=True

# Zato
from zato.server.commands import CommandResult
from zato.server.service import Service

class GetUserDetails(Service):
    """ Returns a local api hit...
    """
    name = 'api.cameo_value_editor'

    class SimpleIO:
        input_required = 'value', 'elementId', 'resourceId'

    def on_completed(self, result:CommandResult) -> None:

        # This will run when the command has finished
        self.logger.info('Received result: %s', result)

    def handle(self):

        # Number of points in the sin wave
        value = self.request.input.value
        elementId = self.request.input.elementId
        resourceId = self.request.input.resourceId
        dataValue = {"kerml:esiData":{"value":"0.0"}}
        dataValue["kerml:esiData"]["value"] = value

        # A command
        #command = f'curl -k -X PATCH "https://18.205.77.131:8111/osmc/resources/272e28f2-45b7-45cb-a016-800ba747e716/elements/{elementId}" -H "accept: application/ld+json" -H "authorization: Basic amRlaGFydDpqa2QyMjE0" -H "Content-Type: application/ld+json" -d "{dataValue}"'
        command = f'curl -k -X PATCH "https://18.205.77.131:8111/osmc/resources/{resourceId}/elements/{elementId}" -H "accept: application/ld+json" -H "authorization: Basic amRlaGFydDpqa2QyMjE0" -H "Content-Type: application/ld+json" -d "{dataValue}"'


        # We can send the response to a pubsub :)
        response = self.commands.invoke(command, callback='/commands/results', use_pubsub=True)

        # Write the response to the caller
        #self.response.payload = {"Response":response.stdout,"Is OK?":response.is_ok,"Value":value,"Element ID":id}


        