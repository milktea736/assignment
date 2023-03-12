from typing import List
from typing import Tuple

from keybert import KeyBERT
from transformers import AutoModelForSeq2SeqLM
from transformers import logging

from backend.db.client import DBClient


class DocKeyword:
    def __init__(self, db_client: DBClient) -> None:
        logging.set_verbosity_error()
        model = AutoModelForSeq2SeqLM.from_pretrained("bloomberg/KeyBART")
        self.kb = KeyBERT(model=model)
        self.db_client = db_client

    def get_keywords(self, doc_title: str, text: str, min_ngram=1, max_ngram=1, top_n=5) -> List[str]:
        """Get some key phrases of the given text.

        Args:
            text (str): original texts.
            min_ngram (int, optional): minimal n-gram of key pharse. Defaults to 1.
            max_ngram (int, optional): maximal n-gram of key pharse. Defaults to 1.
            top_n (int, optional): The number of returned keywords. Defaults to 5.

        Returns:
            List[str]: A list of key phrases.
        """

        keyword_embedding: List[Tuple[str, float]] = self.kb.extract_keywords(
            text, keyphrase_ngram_range=(min_ngram, max_ngram), top_n=top_n
        )
        keywords = [pair[0] for pair in keyword_embedding]
        self._save_to_db(doc_title, keywords)
        return keywords

    def _save_to_db(self, doc_title: str, keywords: List[str]):
        self.db_client.insert_doc([doc_title])
        doc_id: int = self.db_client.get_doc_id(doc_title)
        self.db_client.insert_key_term(doc_id, keywords)
