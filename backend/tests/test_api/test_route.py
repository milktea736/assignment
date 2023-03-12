from fastapi.testclient import TestClient


def test_key_phrases(test_client: TestClient, doc_title: str, doc_content: str):
    response = test_client.post(
        '/key-phrases', json={'title': doc_title, 'content': doc_content, 'min_ngram': 1, 'max_ngram': 1, 'top_n': 5}
    )
    # simple test
    assert response.status_code == 200
