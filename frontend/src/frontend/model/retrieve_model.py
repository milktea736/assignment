from typing import List

import requests

from frontend.configs import HOST


def get_key_phrases(doc_title: str) -> List[str]:
    response = requests.get(f'{HOST}/key-phrases/{doc_title}')
    if len(response.content):
        return [_ for _ in response.json()['content']]
    else:
        return []


def get_summary(doc_title: str) -> List[str]:
    response = requests.get(f'{HOST}/summary/{doc_title}')
    if len(response.content):
        return [_ for _ in response.json()['content']]
    else:
        return []


def get_subtitles(doc_title: str) -> List[str]:
    response = requests.get(f'{HOST}/subtitles/{doc_title}')
    if len(response.content):
        return [_ for _ in response.json()['content']]
    else:
        return []


def get_related_docs(doc_title: str) -> List[str]:
    response = requests.get(f'{HOST}/related_docs/{doc_title}')
    if len(response.content):
        return [_ for _ in response.json()['content']]
    else:
        return []
