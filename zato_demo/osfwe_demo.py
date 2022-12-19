# -*- coding: utf-8 -*-
# zato: ide-deploy=True

# Zato
from zato.server.commands import CommandResult
from zato.server.service import Service

class GetUserDetails(Service):
    name = 'api.osfwe_demo'

    #class SimpleIO:
        #input_required = 'hostName', 'port', 'projectId', 'commitId', 'elementId'

    def on_completed(self, result:CommandResult) -> None:

        # This will run when the command has finished
        self.logger.info('Received result: %s', result)

    def handle(self):

        # Load the working values
        #hostName = self.request.input.hostName
        #port = self.request.input.port
        #projectId = self.request.input.projectId
        #commitId = self.request.input.commitId
        #elementId = self.request.input.elementId

        # Call the API
        # command = f'curl -X GET "http://{hostName}:{port}/projects/{projectId}/commits/{commitId}/elements/{elementId}?excludeUsed=true" -H "accept: application/json"'
        # command = 'curl -X GET "http://127.0.0.1:9000/projects/27096f10-c79e-451f-acd9-5f2ec926ebfd/commits/f6a12489-f2f4-4e1e-aff5-306936862a85/elements/0dd888d1-b53a-422c-a101-ad6aa2d5230d"'
        # command = 'curl -k -X GET "http://localhost:9000/projects/27096f10-c79e-451f-acd9-5f2ec926ebfd/commits/f6a12489-f2f4-4e1e-aff5-306936862a85/elements/0dd888d1-b53a-422c-a101-ad6aa2d5230d?excludeUsed=true" -H "accept: application/json"'
        command = "curl -X GET http://localhost:9000/projects"

        # We can send the response to a pubsub :)
        response = self.commands.invoke(command, callback='/commands/results', use_pubsub=True)

        # Write the response to the caller
        self.response.payload = {"Response":response.stdout, "Is OK?":response.is_ok}


        