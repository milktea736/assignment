from typing import List

from fastapi import APIRouter

from backend.db.client import DBClient
from backend.models.requests import KeyPhraseRequest
from backend.models.requests import SubtitleRequest
from backend.models.requests import SummaryRequest
from backend.models.responses import DocTitleResponse
from backend.models.responses import KeyPhraseResponse
from backend.models.responses import RelatedDocsResponse
from backend.models.responses import SubtitleResponse
from backend.models.responses import SummaryResponse
from backend.services.keyword import DocKeyword
from backend.services.subtitle import SubtitleSegmenter
from backend.services.summary import DocSummary

db_client = DBClient()
keyword: DocKeyword = DocKeyword(db_client)
summary: DocSummary = DocSummary(db_client)
subtitle: SubtitleSegmenter = SubtitleSegmenter(db_client)

router = APIRouter()


@router.post('/key-phrases', tags=['Key Phrases'])
def inference_key_phrases(json: KeyPhraseRequest) -> KeyPhraseResponse:
    _text: str = f'{json.title} {json.content}'
    result: List[str] = keyword.get_keywords(
        doc_title=json.title, text=_text, min_ngram=json.min_ngram, max_ngram=json.max_ngram, top_n=json.top_n
    )
    return KeyPhraseResponse(content=result)


@router.post('/summary', tags=['Summary'])
def inference_summary(json: SummaryRequest) -> SummaryResponse:
    _text: str = f'{json.title} {json.content}'
    result: List[str] = summary.get_summary(doc_title=json.title, text=_text, min_setences=json.min_setences)
    return SummaryResponse(content=result)


@router.post('/subtitles', tags=['Subtitles'])
def inference_subtitles(json: SubtitleRequest) -> SubtitleResponse:
    _text: str = f'{json.content}'
    result: List[str] = subtitle.segement(doc_title=json.title, content=_text, strategy=json.strategy)
    return SubtitleResponse(content=result)


@router.get('/key-phrases/{doc_title}', tags=['Key Phrases'])
def get_key_phrases(doc_title: str) -> KeyPhraseResponse:
    result = db_client.get_key_terms(doc_title)
    return KeyPhraseResponse(content=result)


@router.get('/summary/{doc_title}', tags=['Summary'])
def get_summary(doc_title: str) -> SummaryResponse:
    result = db_client.get_summary(doc_title)
    return SummaryResponse(content=result)


@router.get('/subtitles/{doc_title}', tags=['Subtitles'])
def get_subtitles(doc_title: str) -> SubtitleResponse:
    result = db_client.get_subtitle(doc_title)
    return SubtitleResponse(content=result)


@router.get('/related_docs/{doc_title}', tags=['Related Docs'])
def get_related_docs(doc_title: str) -> RelatedDocsResponse:
    result = db_client.get_related_doc(doc_title)
    return RelatedDocsResponse(content=result)


@router.get('/doc_titles', tags=['Get All Doc Titles'])
def get_doc_titles() -> DocTitleResponse:
    result = db_client.get_all_doc_title()
    return DocTitleResponse(content=result)
