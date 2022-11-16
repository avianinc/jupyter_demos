# -*- coding: utf-8 -*-
# zato: ide-deploy=True

# Zato
from zato.server.commands import CommandResult
from zato.server.service import Service

class GetUserDetails(Service):
    """ Returns a local api hit...
    """
    name = 'api.convert_r2d'

    class SimpleIO:
        input_required = 'angle'

    def on_completed(self, result:CommandResult) -> None:

        # This will run when the command has finished
        self.logger.info('Received result: %s', result)

    def handle(self):

        # Number of points in the sin wave
        angle = self.request.input.angle

        # A command
        #command = f'curl http://172.17.0.3:10100/convert_r2d?angle={angle} -w ", %{http_code}"'
        command = f'curl http://172.17.0.2:10100/convert_r2d?angle={angle}'

        # We can send the response to a pubsub :)
        response = self.commands.invoke(command, callback='/commands/results', use_pubsub=True)

        # Write the response to the caller
        self.response.payload = {"Response":response.stdout, "Is OK?":response.is_ok, "Angle":angle}
        #self.response.payload = {"angle":angle}

        