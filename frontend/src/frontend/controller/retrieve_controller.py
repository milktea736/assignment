from typing import List

from frontend.model import retrieve_model


def retrive_doc(title: str) -> str:
    # OUTPUT: key terms, summary and subtitles for that article, a list of
    # articles with the same key terms
    keywords: List[str] = retrieve_model.get_key_phrases(title)
    summary: List[str] = retrieve_model.get_summary(title)
    subtitles: List[str] = retrieve_model.get_subtitles(title)
    related_docs: List[str] = retrieve_model.get_related_docs(title)
    if keywords or summary or subtitles or related_docs:
        return (
            f'Keywords: {" | ".join(keywords)} \n\n'
            f'Summary: {" ".join(summary)} \n\n'
            f'Subtitles: {" ".join([f"({idx}, {val})" for idx, val in enumerate(subtitles)])} \n\n'
            f'Related docs: {", ".join(related_docs)}'
        )
    else:
        return 'No match doc title.'


if __name__ == '__main__':
    # simple test function
    _title = 'OuOA3'
    _c = (
        'Information overload is a major obstacle to scientific progress. The explosive '
        'growth in scientific literature and data has made it ever harder to discover useful insights '
        'in a large mass of information. Today scientific knowledge is accessed through search '
        'engines, but they are unable to organize scientific knowledge alone. In this paper we '
        'introduce Galactica: a large language model that can store, combine and reason about '
        'scientific knowledge.'
    )
    print(retrive_doc(_title))
