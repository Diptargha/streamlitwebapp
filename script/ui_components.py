import json
import requests


def load_lottieurl(url: str):
    if url.startswith('http'):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    else:
        with open(url, 'r') as file:
            return json.loads(file.read())
