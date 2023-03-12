CREATE_DOC_TABLE_SQL = 'CREATE TABLE IF NOT EXISTS doc( \
    id INT AUTO_INCREMENT, \
    title VARCHAR(200) NOT NULL, \
    PRIMARY KEY(id), \
    UNIQUE INDEX (title))'

CREATE_SUMMARY_TABLE_SQL = 'CREATE TABLE IF NOT EXISTS summary( \
    id INT AUTO_INCREMENT, \
    doc_id INT NOT NULL, \
    sentence VARCHAR(200) NOT NULL, \
    offset INT NOT NULL, \
    PRIMARY KEY(id), \
    UNIQUE INDEX (doc_id, offset), \
    FOREIGN KEY (doc_id) REFERENCES doc(id))'

CREATE_KEY_TERM_TABLE_SQL = 'CREATE TABLE IF NOT EXISTS key_term( \
    id INT AUTO_INCREMENT, \
    term VARCHAR(200) NOT NULL, \
    occur_doc_id INT NOT NULL, \
    PRIMARY KEY(id), \
    UNIQUE INDEX (term, occur_doc_id), \
    FOREIGN KEY (occur_doc_id) REFERENCES doc(id))'

CREATE_SUBTITLE_TABLE_SQL = 'CREATE TABLE IF NOT EXISTS subtitle( \
    doc_id INT NOT NULL, \
    sentence VARCHAR(200) NOT NULL, \
    offset INT NOT NULL, \
    UNIQUE INDEX (doc_id, offset), \
    FOREIGN KEY (doc_id) REFERENCES doc(id))'

INSERT_DOC_SQL = 'INSERT IGNORE INTO doc (title) values (%(title)s)'
INSERT_SUMMARY_SQL = 'INSERT IGNORE INTO summary (doc_id, sentence, offset) values (%(doc_id)s, %(sentence)s, %(offset)s)'
INSERT_KEY_TERM_SQL = 'INSERT IGNORE INTO key_term (term, occur_doc_id) values (%(term)s, %(occur_doc_id)s)'
INSERT_SUBTITLE_SQL = 'INSERT IGNORE INTO subtitle (doc_id, sentence, offset) values (%(doc_id)s, %(sentence)s, %(offset)s)'


GET_RELATED_DOC_SQL_TEMPLATE = (
    'SELECT doc.title FROM doc JOIN '
    '(select DISTINCT t2.occur_doc_id from key_term t1 '
    'JOIN key_term t2 ON t1.term=t2.term WHERE t1.occur_doc_id={doc_id}) occur '
    'ON doc.id = occur.occur_doc_id WHERE occur.occur_doc_id !={doc_id}'
)


GET_KEY_TERMS_SQL_TEMPLATE = 'SELECT term FROM key_term ' 'WHERE occur_doc_id={doc_id}'

GET_SUMMARY_SQL_TEMPLATE = 'SELECT sentence, offset, doc_id FROM summary ' 'WHERE doc_id={doc_id} ' 'GROUP BY offset'

GET_SUBTITLE_SQL_TEMPLATE = 'SELECT sentence, offset, doc_id FROM subtitle ' 'WHERE doc_id={doc_id} ' 'GROUP BY offset'

GET_ALL_DOC_TITLE = 'SELECT title FROM doc'
