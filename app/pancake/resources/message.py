import requests

from config import INSTA_TAG_URL
from random import choice
from secrets import INSTA_ID


class Message(object):
    """This is a message recieved by the groupme bot"""
    def __init__(self, json):
        super(Message, self).__init__()
        self.json = json
        self.uid = json['user_id']
        self.guid = json['group_id']
        self.text = json['text']
        self.name = json['name']
        self.attachments = json['attachments']
        self.bot = json['sender_type'] == 'bot'

    def isCommand(self):
        """Checks if this is a .command"""
        if self.text[0] == '.':
            command = self.text.split(' ')[0][1:]
            if command == 'date' or command == 'd':
                self.command = 'd'
            elif command == 'help' or command == 'h':
                self.command = 'h'
            elif command == 'get' or command == 'g':
                self.command = 'g'
            elif command == 'set' or command == 's':
                self.command = 's'
            elif command == 'version' or command == 'v':
                self.command = 'v'
            else:
                self.command = None
            return True
        return False

    def contains(self, string):
        """checks if message contains given string"""
        if string.lower() in self.text.lower():
            return True
        return False

    def hastag(self):
        """Finds hashtags and returns a random picture for it if there is one"""
        words = self.text.split(' ')
        hashtags = []
        for word in words:
            if word[0] == "#":
                hashtags.append(word[1:])

        if len(hashtags) == 0:
            return False

        picArray = requests.get(INSTA_TAG_URL % (choice(hashtags), INSTA_ID)).json()['data']
        self.hashtagPic = choice(picArray)['images']['low_resolution']['url']
        return True
