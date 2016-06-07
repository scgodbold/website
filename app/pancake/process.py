import requests

from datetime import datetime
from random import choice

from app import app


def imgur_tag_search(tag):
    tag_url = '{imgur_base}/gallery/t/{tag}'.format(imgur_base=app.config['IMGUR_URL'],
                                                    tag=tag)
    auth_header = {'Authorization': 'Client-ID {client_id}'.format(client_id=app.config['IMGUR_CLIENT_ID'])}
    results = requests.get(tag_url, headers=auth_header)
    if results.status_code != 200:
        return None
    safe_images = []
    for item in results.json()['data']['items']:
        if not item['nsfw'] and not item['is_album']:
            # only safe images, so not - not safe for work
            # Wrote that out to make sure I had that right in my head
            safe_images.append(item)
    if len(safe_images) == 0:
        return None
    img = choice(safe_images)['link']
    return img


def process_triggers(text):
    resp_text = []
    words = filter(str.isalnum, text.lower()).split(' ')
    for word in words:
        if word == 'marcus':
            resp_text.append('Jarvis*')
        elif word == 'burn':
            resp_text.append('http://en.wikipedia.org/wiki/List_of_burn_centers_in_the_United_States')
        elif word == 'doms' or word == 'dominics':
            resp_text.append('Im sorry I cannot tolerate communist establishments')
        elif word == 'pancake':
            resp_text.append('Good day sir')
        elif word == 'bears':
            days = (datetime(2021, 1, 1) - datetime.now()).days
            resp_text.append('There are roughly {days} days left on Jay Cutlers contract.'.format(days=days))
        elif word == 'harbaugh':
            harbaugh_img = imgur_tag_search('harbaugh')
            if harbaugh_img is not None:
                resp_text.append(harbaugh_img)

    if 'go blue' in text:
        img = imgur_tag_search('goblue')
        if img is not None:
            resp_text.append(img)

    if len(resp_text) == 0:
        return []
    return resp_text


def proccess_hashtags(text):
    tags = []
    words = text.lower().split(' ')
    for word in words:
        try:
            if word[0] == '#':
                img = imgur_tag_search(word[1:])
                if img is not None:
                    tags.append(img)
        except:
            continue
    return tags


def rainy_day(json):
    trigger_resp = process_triggers(json['text'])
    tags_resp = proccess_hashtags(json['text'])
    resps = trigger_resp + tags_resp
    if len(resps) == 0:
        return None
    return {'text': choice(resps)}
