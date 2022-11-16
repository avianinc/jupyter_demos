# -*- coding: utf-8 -*-
# zato: ide-deploy=True

# Zato
from zato.server.service import Service

class LogInputData(Service):
    """ Logs input data.
    """
    name = 'api.input'

    class SimpleIO:
        input_required = 'user_id', 'user_name'

    def handle(self):

        # Read input received
        user_id = self.request.input.user_id
        user_name = self.request.input.user_name

        # Store input in logs
        self.logger.info('uid:%s; username:%s', user_id, user_name)

        # Return
        self.response.payload = {"user_id":user_id, "username":user_name}