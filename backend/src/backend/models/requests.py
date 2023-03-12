from pydantic import BaseModel
from pydantic import ValidationError
from pydantic import validator

CONTENT_SIZE_LIMIT = 2000


class BaseDocRequest(BaseModel):
    title: str
    content: str

    @validator('content')
    def check_content_size(cls, v):
        content_size = len(v)
        if content_size > CONTENT_SIZE_LIMIT:
            raise ValidationError(f'The content length is limit to {CONTENT_SIZE_LIMIT}, but we received {content_size}.')
        return v


class KeyPhraseRequest(BaseDocRequest):
    min_ngram: int = 1
    max_ngram: int = 1
    top_n: int = 5


class SummaryRequest(BaseDocRequest):
    min_setences: int = 3


class SubtitleRequest(BaseDocRequest):
    strategy: str = 'sentence'
