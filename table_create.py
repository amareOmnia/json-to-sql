# Handles creation of database table
import table_config as tc

def generate_table_query():
    table_name = tc.get_table_name()
    columns = tc.get_column_config()
    query = '''CREATE TABLE IF NOT EXISTS {0}
    '''.format(table_name)
    for column, data_type in columns.items():
        query += '''{0} {1}
        '''.format(column, data_type)
    return query
        
