import unicodedata
from typing import List

from spacy.lang.en import English
from spacy.tokens.doc import Doc

from backend.db.client import DBClient

SUBTITLE_LENGTH_LIMIT = 45


class SubtitleSegmenter:
    def __init__(self, db_client: DBClient) -> None:
        self.nlp = English()
        self.nlp.add_pipe("sentencizer")
        self.db_client = db_client

    def segement(self, doc_title: str, content: str, strategy: str = 'sentence') -> List[str]:
        """Segement content to subtitles

        Args:
            content (str): text content
            strategy 'sentence', 'compact' are avaliables. Defaults to 'sentence'.

        Returns:
            List[str]: subtittles
        """
        doc: Doc = self.nlp(self._normalize_form(content))
        sentences: List[str] = [' '.join(s.text.split()) for s in doc.sents]
        subtitles: List[str] = self._wrap_subtitles(sentences, strategy)
        self._save_to_db(doc_title, subtitles)
        return subtitles

    @staticmethod
    def _normalize_form(doc: str) -> str:
        return unicodedata.normalize('NFKC', doc)

    def _wrap_subtitles(self, sentences: List[str], strategy: str = 'sentence') -> List[str]:
        """Provide different strategy to wrap subtitles.

        Args:
            sentences (List[str]): setences
            strategy (str, optional): 'sentence', 'compact' are avaliables. Defaults to 'sentence'.

        Returns:
            List[str]: subtittles
        """
        return {'sentence': self._wrap_preserve_sentence, 'compact': self._wrap_compact}[strategy](sentences)

    @staticmethod
    def _wrap_preserve_sentence(sentences: List[str]) -> List[str]:
        """Don't combine words in different sentece into a single subtitle"""

        subtitles: List[str] = []
        current_length: int = 0
        current_subtitles: List[str] = []

        def add_subtitle(word_size: int = 0, word: str = ''):
            nonlocal current_length, current_subtitles
            subtitles.append(' '.join(current_subtitles))
            current_length = word_size
            current_subtitles = [word]

        for s in sentences:
            for w in s.split():
                # space character between words occupies 1
                word_size = len(w) + 1
                if current_length + word_size <= SUBTITLE_LENGTH_LIMIT:
                    current_subtitles.append(w)
                    current_length += word_size
                else:
                    add_subtitle(word_size, w)

            if current_subtitles:
                add_subtitle()

        return subtitles

    @staticmethod
    def _wrap_compact(sentences: List[str]) -> List[str]:
        """Combine words in different sentece into a single subtitle"""

        subtitles: List[str] = []
        current_length: int = 0
        current_subtitles: List[str] = []
        words = [w for s in sentences for w in s.split()]

        for w in words:
            # space character between words occupies 1
            word_size = len(w) + 1
            if current_length + word_size <= SUBTITLE_LENGTH_LIMIT:
                current_subtitles.append(w)
                current_length += word_size
            else:
                subtitles.append(' '.join(current_subtitles))
                current_length = word_size
                current_subtitles = [w]

        if current_subtitles:
            subtitles.append(' '.join(current_subtitles))

        return subtitles

    def _save_to_db(self, doc_title: str, subtitles: List[str]):
        self.db_client.insert_doc([doc_title])
        doc_id: int = self.db_client.get_doc_id(doc_title)
        self.db_client.insert_subtitle(doc_id, subtitles)
