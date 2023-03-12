from typing import List

from numpy import ndarray
from summarizer.sbert import SBertSummarizer

from backend.db.client import DBClient


class DocSummary:
    def __init__(self, db_client: DBClient) -> None:
        self.summarizer = SBertSummarizer('sentence-transformers/paraphrase-MiniLM-L3-v2')
        self.db_client = db_client

    def get_summary(self, doc_title: str, text: str, min_setences: int = 3) -> List[str]:
        """Get some sentences to summarize the given text.

        Args:
            text (str): original texts.
            min_setences (int, optional): The minimal number of sentences to summarize. Defaults to 3.

        Returns:
            List[str]: A list of sentences.
        """

        # implement steps:
        # Preprocesses the sentences, runs the clusters to find the centroids, then combines the sentences.
        result: List[str] = self.summarizer(text, num_sentences=min_setences, return_as_list=True)
        summary: List[str] = [' '.join(line.split()) for line in result]
        self._save_to_db(doc_title, summary)
        return summary

    def get_summary_embeddings(self, text: str, min_setences: int = 3) -> List[List[float]]:
        """Get the embeddings of summary sentences.

        Args:
            text (str): original texts.
            min_setences (int, optional): The minimal number of sentences to summarize. Defaults to 3.

        Returns:
            List[List[float]]: A list containing a list of sentence embeddings
        """

        result: ndarray = self.summarizer.run_embeddings(text, num_sentences=min_setences)
        return result.tolist()

    def _save_to_db(self, doc_title: str, summary: List[str]):
        self.db_client.insert_doc([doc_title])
        doc_id: int = self.db_client.get_doc_id(doc_title)
        self.db_client.insert_summary(doc_id, summary)
