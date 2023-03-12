import os
from typing import Dict
from typing import List
from typing import Union

import pymysql
import sqlalchemy
from dotenv import load_dotenv
from google.cloud.sql.connector import Connector
from sqlalchemy import Engine

from backend.db.querys import CREATE_DOC_TABLE_SQL
from backend.db.querys import CREATE_KEY_TERM_TABLE_SQL
from backend.db.querys import CREATE_SUBTITLE_TABLE_SQL
from backend.db.querys import CREATE_SUMMARY_TABLE_SQL
from backend.db.querys import GET_ALL_DOC_TITLE
from backend.db.querys import GET_KEY_TERMS_SQL_TEMPLATE
from backend.db.querys import GET_RELATED_DOC_SQL_TEMPLATE
from backend.db.querys import GET_SUBTITLE_SQL_TEMPLATE
from backend.db.querys import GET_SUMMARY_SQL_TEMPLATE
from backend.db.querys import INSERT_DOC_SQL
from backend.db.querys import INSERT_KEY_TERM_SQL
from backend.db.querys import INSERT_SUBTITLE_SQL
from backend.db.querys import INSERT_SUMMARY_SQL

load_dotenv()

CONNECTION_NAME = os.getenv('DB_CONNECTION_NAME')

USER = os.getenv('DB_USER')
PASSWORD = os.getenv('DB_PASSWORD')
DB = os.getenv('DB_NAME')


class DBClient:
    def __init__(self) -> None:
        self._engine: Engine = self._create_engine()
        self.init_tables()

    def _create_engine(self) -> Engine:
        def get_conn() -> pymysql.connections.Connection:
            connector = Connector()
            return connector.connect(CONNECTION_NAME, 'pymysql', user=USER, password=PASSWORD, db=DB)

        return sqlalchemy.create_engine('mysql+pymysql://', creator=get_conn, pool_pre_ping=True)

    @property
    def engine(self):
        return self._engine

    def init_tables(self):
        with self.engine.connect() as db_conn:
            for sql in [CREATE_DOC_TABLE_SQL, CREATE_SUMMARY_TABLE_SQL, CREATE_KEY_TERM_TABLE_SQL, CREATE_SUBTITLE_TABLE_SQL]:
                db_conn.exec_driver_sql(sql)
            db_conn.commit()

    def drop_tables(self):
        with self.engine.connect() as db_conn:
            db_conn.exec_driver_sql('drop table summary')
            db_conn.exec_driver_sql('drop table subtitle')
            db_conn.exec_driver_sql('drop table key_term')
            db_conn.exec_driver_sql('drop table doc')
            db_conn.commit()

    def insert_doc(self, doc_titles: List[str]):
        values = [{'title': title} for title in doc_titles]
        with self.engine.connect() as db_conn:
            db_conn.exec_driver_sql(INSERT_DOC_SQL, values)
            db_conn.commit()

    def insert_summary(self, doc_id: int, sentences: List[str]):
        values = [{'doc_id': doc_id, 'sentence': val, 'offset': idx} for idx, val in enumerate(sentences)]
        with self.engine.connect() as db_conn:
            db_conn.exec_driver_sql(INSERT_SUMMARY_SQL, values)
            db_conn.commit()

    def insert_key_term(self, doc_id: int, key_terms: List[str]):
        values = [{'term': term, 'occur_doc_id': doc_id} for term in key_terms]
        with self.engine.connect() as db_conn:
            db_conn.exec_driver_sql(INSERT_KEY_TERM_SQL, values)
            db_conn.commit()

    def insert_subtitle(self, doc_id: int, subtitle: List[str]):
        values = [{'doc_id': doc_id, 'sentence': val, 'offset': idx} for idx, val in enumerate(subtitle)]
        with self.engine.connect() as db_conn:
            db_conn.exec_driver_sql(INSERT_SUBTITLE_SQL, values)
            db_conn.commit()

    def get_doc_id(self, doc_title: str) -> Union[None, int]:
        with self.engine.connect() as db_conn:
            res = db_conn.exec_driver_sql(f'SELECT id FROM doc WHERE title="{doc_title}"')
            return res.fetchone()[0] if res.rowcount else None

    def _fetch_data(self, doc_title: str, query_template: str) -> List[Dict]:
        doc_id: Union[None, int] = self.get_doc_id(doc_title)

        if doc_id:
            query: str = query_template.format(doc_id=doc_id)

            with self.engine.connect() as db_conn:
                res = db_conn.exec_driver_sql(query)
                return list(res.mappings()) if res.rowcount else []
        else:
            return []

    def get_related_doc(self, doc_title: str) -> List[str]:
        results = self._fetch_data(doc_title, GET_RELATED_DOC_SQL_TEMPLATE)
        return [r['title'] for r in results] if results else []

    def get_key_terms(self, doc_title: str) -> List[str]:
        results = self._fetch_data(doc_title, GET_KEY_TERMS_SQL_TEMPLATE)
        return [r['term'] for r in results] if results else []

    def get_summary(self, doc_title: str) -> List[str]:
        results = self._fetch_data(doc_title, GET_SUMMARY_SQL_TEMPLATE)
        return [r['sentence'] for r in results] if results else []

    def get_subtitle(self, doc_title: str) -> List[str]:
        results = self._fetch_data(doc_title, GET_SUBTITLE_SQL_TEMPLATE)
        return [r['sentence'] for r in results] if results else []

    def get_all_doc_title(self) -> List[str]:
        with self.engine.connect() as db_conn:
            res = db_conn.exec_driver_sql(GET_ALL_DOC_TITLE)
            return [_['title'] for _ in list(res.mappings())] if res.rowcount else []
