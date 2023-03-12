import pytest

from backend.services.keyword import DocKeyword


class TestDocKeyword:
    @pytest.fixture(scope='class')
    def doc_keyword(self, db_client) -> DocKeyword:
        return DocKeyword(db_client)

    def test_get_keywords(self, doc_keyword: DocKeyword, doc_content: str, doc_title: str) -> None:
        min_ngram = 1
        max_ngram = 2

        ans = ['information overload', 'scientific knowledge', 'mass information', 'data harder', 'organize scientific']
        res = doc_keyword.get_keywords(doc_title, doc_content, min_ngram=min_ngram, max_ngram=max_ngram)
        assert ans == res
