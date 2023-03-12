from typing import List

from pydantic import BaseModel

from backend.db.client import DBClient


class Doc(BaseModel):
    title: str
    content: str
    sentences: List[str]
    key_terms: List[str]
    subtitle: List[str]


# d1 and d2 have same "d1_term1"
d1 = Doc(
    title='d1_title',
    content='d1_content',
    sentences=['d1_sen1', 'd1_sen2', 'd1_sen3'],
    key_terms=['d1_term1', 'd1_term2', 'd1_term3'],
    subtitle=['d1_sub1', 'd1_sub2', 'd1_sub3'],
)
d2 = Doc(
    title='d2_title',
    content='d2_content',
    sentences=['d2_sen1', 'd2_sen2', 'd2_sen3'],
    key_terms=['d1_term1', 'd2_term2', 'd2_term3'],
    subtitle=['d2_sub1', 'd2_sub2', 'd2_sub3'],
)
d3 = Doc(
    title='d3_title',
    content='d3_content',
    sentences=['d3_sen1', 'd3_sen2', 'd3_sen3'],
    key_terms=['d3_term1', 'd3_term2', 'd3_term3'],
    subtitle=['d3_sub1', 'd3_sub2', 'd3_sub3'],
)


if __name__ == '__main__':
    c = DBClient()
    c.init_tables()

    doc_list = [d1, d2, d3]
    c.insert_doc([d.title] for d in doc_list)
    for d in doc_list:
        doc_id = c.get_doc_id(doc_title=d.title)
        if doc_id:
            c.insert_summary(doc_id, d.sentences)
            c.insert_key_term(doc_id, d.key_terms)
            c.insert_subtitle(doc_id, d.subtitle)
