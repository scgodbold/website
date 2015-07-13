import requests
from config import GROUPME_URL


class GroupmeBot(object):
    """docstring for GroupmeBot"""
    def __init__(self):
        self.groupme = GROUPME_URL

    def post(self, payload):
        """Adds a message to the groupme"""
        payload['bot_id'] = self.id
        print payload
        requests.post(self.groupme, payload)
        try:
            pass
        except:
            print 'fuck'
