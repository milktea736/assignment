from typing import List

from frontend.model import doc_title_model


def get_title() -> str:
    # OUTPUT: key terms, summary and subtitles for that article, a list of
    # articles with the same key terms
    titles: List[str] = doc_title_model.get_all_doc_title()
    if titles:
        return f'Doc titles: {" | ".join(titles)}\n\n'
    else:
        return 'No match doc title.'


if __name__ == '__main__':
    # simple test function
    print(get_title())
