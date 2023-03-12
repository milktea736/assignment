from backend.db.client import DBClient

if __name__ == '__main__':
    c = DBClient()
    c.drop_tables()
