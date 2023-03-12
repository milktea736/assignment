from typing import List

import requests

from frontend.configs import HOST


def get_all_doc_title() -> List[str]:
    response = requests.get(f'{HOST}/doc_titles')
    if len(response.content):
        return [_ for _ in response.json()['content']]
    else:
        return []
