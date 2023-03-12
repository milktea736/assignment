from typing import List

import requests

from frontend.configs import HOST


def inference_key_phrases(title: str, content: str) -> List[str]:
    _json = {'title': title, 'content': content, 'min_ngram': 1, 'max_ngram': 1, 'top_n': 5}
    response = requests.post(f'{HOST}/key-phrases', json=_json)
    if len(response.content):
        return [_ for _ in response.json()['content']]
    else:
        return []


def inference_summary(title: str, content: str) -> List[str]:
    _json = {
        'title': title,
        'content': content,
        'min_setences': 3,
    }
    response = requests.post(f'{HOST}/summary', json=_json)
    if len(response.content):
        return [_ for _ in response.json()['content']]
    else:
        return []


def inference_subtitles(title: str, content: str):
    _json = {
        'title': title,
        'content': content,
        'min_setences': 3,
    }
    response = requests.post(f'{HOST}/subtitles', json=_json)
    if len(response.content):
        return [_ for _ in response.json()['content']]
    else:
        return []
