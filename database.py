import psycopg2 as psql
import table_config as tc

class Database:
    def __init__(self):
        login = tc.get_db_login()
        self.database = psql.connect(\
            host     = login['host'], 
            database = login['database'],
            user     = login['user'],
            password = login['password']).cursor()

    def execute_query(self, query):
        self.database.execute(query)
        return self.database.fetchall()