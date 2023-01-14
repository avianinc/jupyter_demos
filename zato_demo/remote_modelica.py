# -*- coding: utf-8 -*-
# zato: ide-deploy=True

# Zato
from zato.server.commands import CommandResult
from zato.server.service import Service

class GetUserDetails(Service):
    """ Returns a local api hit...
    """
    name = 'api.remote.modelica'

    class SimpleIO:
        input_required = 'Freq', 'Amp'

    def on_completed(self, result:CommandResult) -> None:

        # This will run when the command has finished
        self.logger.info('Received result: %s', result)

    def handle(self):

        # Input data
        amp = self.request.input.Amp
        freq = self.request.input.Freq

        # A command
        command = f'curl -k -X GET http://54.208.197.217:10100/scilab_xcos_model?Amp={amp}&Freq={freq}'

            # Here is what a generic service might look like
            #command = f'curl -k -X GET http://{hostIp}:{port}}/{scriptName}?args={args}'

        
        # We can send the response to a pubsub :)
        response = self.commands.invoke(command, callback='/commands/results', use_pubsub=True)

            # Here is a generic topic that can be pushed along with the command data
            #response = f'self.commands.invoke(command, callback="{topicName}", use_pubsub=True)'

        # Write the response to the caller
        self.response.payload = {"Response":response.stdout, "Is OK?":response.is_ok}

        