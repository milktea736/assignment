from faker import Faker

from backend.db.client import DBClient
from backend.services.keyword import DocKeyword
from backend.services.subtitle import SubtitleSegmenter
from backend.services.summary import DocSummary

fake = Faker()


DOC_NUMER = 10


def gen_doc():
    return ' '.join([fake.text() for _ in range(5)])


fake_titles = [fake.name() for _ in range(DOC_NUMER)]
fake_docs = [gen_doc() for _ in range(DOC_NUMER)]

duplicate_doc_title = 'Duplicated doc'
duplicate_doc = fake_docs[0]

fake_titles.append(duplicate_doc_title)
fake_docs.append(duplicate_doc)


if __name__ == '__main__':
    c = DBClient()
    c.init_tables()

    summary = DocSummary(c)
    keyword = DocKeyword(c)
    subtitle = SubtitleSegmenter(c)

    for idx in range(len(fake_docs)):
        title = fake_titles[idx]
        content = fake_docs[idx]
        print(f'Insert: {title}\n\n{content}')
        c.insert_doc([title])
        summary.get_summary(title, content)
        keyword.get_keywords(title, content)
        subtitle.segement(title, content)
