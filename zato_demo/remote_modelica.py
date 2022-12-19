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
        command = f'curl -k -X GET http://3.236.246.39:10100/scilab_xcos_model?Amp={amp}&Freq={freq}'
        #command = f'curl http://127.0.0.1:10100/scilab_xcos_model?Amp={amp}&Freq={freq}'
        #command = "curl -X GET http://www.google.com" 

        # We can send the response to a pubsub :)
        response = self.commands.invoke(command, callback='/commands/results', use_pubsub=True)

        # Write the response to the caller
        self.response.payload = {"Response":response.stdout, "Is OK?":response.is_ok}

        