import pytest

from backend.services.summary import DocSummary


class TestDocSummary:
    @pytest.fixture(scope='class')
    def doc_summary(self, db_client) -> DocSummary:
        return DocSummary(db_client)

    def test_get_summary(self, doc_summary: DocSummary, doc_content: str, doc_title: str) -> None:
        ans = num_sentences = 3
        res = doc_summary.get_summary(doc_title, doc_content, num_sentences)
        assert ans == len(res)

    def test_get_summary_embeddings(self, doc_summary: DocSummary, doc_content: str) -> None:
        ans = num_sentences = 3
        res = doc_summary.get_summary_embeddings(doc_content, num_sentences)
        assert ans == len(res)
