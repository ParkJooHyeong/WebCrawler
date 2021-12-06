import psycopg2


class Databases:
    def __init__(self):
        self.db = psycopg2.connect(
            host='localhost',
            dbname='test',
            user='test',
            password='pwd',
            port=3001)
        self.cursor = self.db.cursor()

    def __del__(self):
        self.db.close()
        self.cursor.close()

    def execute(self,query,args={}):
        self.cursor.execute(query,args)
        return self.cursor.fetchall()

    def commit(self):
        self.cursor.commit()