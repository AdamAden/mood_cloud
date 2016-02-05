import requests
from django.conf import settings

def get_woeid(text):
    if not text:
        return

    app_id = settings.WOEID_APP_ID

    if not app_id:
        raise NotImplementedError('WOEID App Id is empty.')

    url = 'http://where.yahooapis.com/v1/places.q(\'%s\')?appid=%s&format=json' % (
        text, app_id
    )

    r = requests.get(url)

    json = r.json

    places = json['places']

    if not places['count']:
        return

    place = places['place'][0]

    return {
        'woeid': place['woeid'],
        'name': place['name']
    }

    print get_woeid("London")