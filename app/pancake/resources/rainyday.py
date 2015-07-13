import os
import requests

from app import app
from groupmebot import GroupmeBot
from message import Message
from secrets import RAINY_DAY


class RainyDay(GroupmeBot):
    """Rainyday groupme bot"""
    def __init__(self):
        super(RainyDay, self).__init__()
        self.version = '2.0.1'
        self.id = RAINY_DAY

    def parse(self, json):
        """Reads through posts determining what to do"""
        message = Message(json)
        if not message.bot:
            if message.text != '':
                if message.isCommand():
                    self.commands(message)

            if message.contains('marcus'):
                self.post({'text': 'Jarvis*'})
            if message.contains('bears'):
                self.post({'text': 'http://scgodbold.com/static/imgs/pancake/bears.jpg'})
            if message.contains('burn'):
                self.post({'text': 'http://en.wikipedia.org/wiki/List_of_burn_centers_in_the_United_States'})
            if message.contains('harbaugh'):
                self.post({'text': 'http://scgodbold.com/static/imgs/pancake/harbaugh.jpg'})
                self.post({'text': 'LETS FUCKING DO THIS'})
            if message.contains('doms') or message.contains('dominics'):
                self.post({'text': 'I cannot condone attending doms as it is a communist establishment'})
            if message.hastag():
                self.post({'text': message.hashtagPic})

    def commands(self, message):
        if message.command == 'd':
            self.post({'text': 'But I hardly know you {}'.format(message.name)})
        elif message.command == 'g':
            self.get(message)
        elif message.command == 's':
            self.set(message)
        elif message.command == 'v':
            self.getVersion()
        elif message.command == 'h':
            self.help()
        else:
            self.post({'text': 'Out of pabst please try a new command'})

    def help(self):
        helpstr = 'Pancake Lincoln v{} commands:\n=====================\n'.format(self.version)
        helpstr += 'Formatting, short comamnd surronded by [].\n'
        helpstr += 'e.x [f]oo means .f and .foo do the same thing\n\n'
        helpstr += '.[d]ate: returns the date\n'
        helpstr += '.[g]et <name>: gets an image from the server by your name\n'
        helpstr += '\t-[-l]ist: replace name with this for get to see currently available commands'
        helpstr += '.[s]et <name>: sets an image to pull with get, must contain an image and a name\n'
        helpstr += '.[v]ersion: returns pancakes current version\n'
        helpstr += '.[h]elp: prints out this dialouge\n'
        self.post({'text': helpstr})

    def set(self, message):
        name = message.text.split(' ')
        if len(name) < 2:
            self.post({'text': 'I\'m sorry you must provide a name with the set command'})
            return
        if len(message.attachments) < 1:
            self.post({'text': 'Please provide an image to set the command to'})
            return
        if message.attachments[0]['type'] != 'image':
            self.post({'text': 'Please provide an image to set the command to'})
            return

        url = message.attachments[0]['url']
        ext = message.attachments[0]['url'].split('.')[-2]
        with open('{}/{}.{}'.format(app.config['SET_DIR'], name[1], ext), 'wb') as f:
            resp = requests.get(url, stream=True)
            if not resp.ok:
                self.post({'text': 'something went wrong please try again later'})
                return
            for block in resp.iter_content(1024):
                if not block:
                    break
                f.write(block)

    def get(self, message):
        name = message.text.split(' ')
        if len(name) < 2:
            self.post({'Im sorry I am uncertain of which image you are looking for'})
            return

        if name[1] == '--list' or name[1] == '-l':
            payload = {
                'text': 'available get commands currently\n=============================\n',
            }
            for f in os.listdir(app.config['SET_DIR']):
                if f[0] == '.':
                    continue
                file_name = f.split('.')[0]
                payload['text'] += '{}\n'.format(file_name)
            self.post(payload)
            return

        for f in os.listdir(app.config['SET_DIR']):
            if f[0] == '.':
                continue
            file_name = f.split('.')[0]

            if file_name == name[1]:
                payload = {
                    'text': 'http://scgodbold.com/static/imgs/pancake/setimgs/{}'.format(f),
                }
                self.post(payload)
                return
        self.post({'text': 'it appears the image you requested doesnt exist, perhaps try setting it, or checking --list'})

    def getVersion(self):
        self.post({'text': 'Pancake Lincoln v{}'.format(self.version)})
