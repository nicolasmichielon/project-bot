import json
from os import getenv
from random import randint
import requests

# set the apikey and limit
apikey = getenv("API_KEY_TENOR")
lmt = 20
ckey = "my_test_app"  # set the client_key for the integration and use the same value for all API calls


def gifSearch(search_term):
    search_term = ' '.join(search_term)

    r = requests.get(
        "https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" % (search_term, apikey, ckey,  lmt))

    if r.status_code == 200:
        gif = json.loads(r.content)
        url = gif.get('results')[randint(0, lmt)].get('media_formats').get('gif').get('url')
        return url
    else:
        return "Nenhum GIF encontrado."