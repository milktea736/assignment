from typing import List

from frontend.model import save_model


def save_doc(title: str, content: str) -> str:
    # OUTPUT: key terms, summary and subtitle lines
    keywords: List[str] = save_model.inference_key_phrases(title, content)
    summary: List[str] = save_model.inference_summary(title, content)
    subtitles: List[str] = save_model.inference_subtitles(title, content)
    return (
        f'Keywords: {" | ".join(keywords)} \n\n'
        f'Summary: {" ".join(summary)} \n\n'
        f'Subtitles: {" ".join([f"({idx}, {val})" for idx, val in enumerate(subtitles)])}'
    )


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
    print(save_doc(_title, _c))
