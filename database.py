import psycopg2 as psql
import table_config as tc

class Database:
    def __init__(self):
        login = tc.get_db_login()
        self.database = psql.connect(\
            host     = login['host'], 
            database = login['database'],
            user     = login['user'],
            password = login['password'])
        
        self.connection = self.database.cursor()

    def execute_query(self, query, return_result=True):
        self.connection.execute(query)
        if return_result:
            return self.database.fetchall()
        else:
            return
    
    def close_connection(self):
        self.connection.close()
        self.database.close()
        return