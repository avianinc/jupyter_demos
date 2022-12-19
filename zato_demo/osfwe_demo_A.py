# -*- coding: utf-8 -*-
# zato: ide-deploy=True

# Zato
from zato.server.commands import CommandResult
from zato.server.service import Service

class osfwe(Service):
    """ Returns a local api hit...
    """
    name = 'osfew_demo'

    #class SimpleIO:
    #    input_required = 'Freq', 'Amp'

    def on_completed(self, result:CommandResult) -> None:

        # This will run when the command has finished
        self.logger.info('Received result: %s', result)

    def handle(self):

        # Number of points in the sin wave
        #amp = self.request.input.Amp
        #freq = self.request.input.Freq

        # A command
        #command = 'curl -X GET http://localhost:9000/projects'
        command = 'curl -X GET http://www.google.com'

        # We can send the response to a pubsub :)
        #response = self.commands.invoke(command, callback='/commands/freq', use_pubsub=True)
        response = self.commands.invoke(command, callback=self.on_completed)

        # Write the response to the caller
        self.response.payload = {"Response":response.stdout, "Is OK?":response.is_ok, "URL":command}

        