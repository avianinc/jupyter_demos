# -*- coding: utf-8 -*-
# zato: ide-deploy=True

# Zato
from zato.server.commands import CommandResult
from zato.server.service import Service

class GetUserDetails(Service):
    """ Returns details of a user by the person's ID.
    """
    name = 'api.tester'

    def on_completed(self, result:CommandResult) -> None:

        # This will run when the command has finished
        self.logger.info('Received result: %s', result)

    def handle(self):

        # Number of points in the sin wave
        numbPoints = 10

        # A command that will take a longer time to complete ..
        #command = 'sleep 5'
        #command = 'scilab-cli -e "disp(rand(99));exit"'
        #command = f'scilab-cli -e "disp(sin(1:{numbPoints}));exit"' # example of how to stuff python vars into a string for exe
        command = 'docker exec -it 172.17.0.3 bash -c "/tmp/scilab-6.0.2/bin/scilab-cli -quit -noatomsautoload -e "disp\(5\);exit;"'

        # A .. invoke it, specifying a callback.
        #response = self.commands.invoke(command, callback=self.on_completed)

        # B .. or we can send the response to a pubsub :)
        response = self.commands.invoke(command, callback='/commands/results', use_pubsub=True)

        self.response.payload = {"Response":response.stdout, "Is OK?":response.is_ok}

        # Add a callback to inform the pubsub

        