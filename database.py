import psycopg2

class Database:
    def __init__(self, host, database, user, password):
        self.database = psql.connect(\
            host     = host, 
            database = database,
            user     = user,
            password = password).cursor()

    def execute_query(self, query):
        self.database.execute(query)
        return self.database.fetchall()