# -*- coding: utf-8 -*-
# zato: ide-deploy=True

from zato.server.service import Service

class GetMessages(Service):
    def handle(self):

        # Prepare input
        topic_name = '/commands/results'
        #sub_key = 'zpsk.rest.6b0b83ebea3f6e6a64e8e73f'

        # Get all messages available ..
        messages = self.pubsub.get_messages(topic_name)#, sub_key)

        # .. and log them all.
        response = self.logger.info('Messages `%s`', messages)
        self.response.payload = {"Response":response}