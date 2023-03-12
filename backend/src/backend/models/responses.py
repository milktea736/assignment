from typing import List

from pydantic import BaseModel


class StringList(BaseModel):
    content: List[str]


class KeyPhraseResponse(StringList):
    pass


class SummaryResponse(StringList):
    pass


class SubtitleResponse(StringList):
    pass


class RelatedDocsResponse(StringList):
    pass


class DocTitleResponse(StringList):
    pass
