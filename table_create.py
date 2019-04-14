# Handles creation of database table
import table_config as tc

def generate_table_query():
    table_name = tc.get_table_name()
    columns = tc.get_column_config()
    query = '''CREATE TABLE IF NOT EXISTS {0} (
    '''.format(table_name)
    i = 1
    for column, data_type in columns.items():
        if i >= len(columns):
            query += '''{0} {1})
            '''.format(column, data_type)
        else:
            query += '''{0} {1},
            '''.format(column, data_type) 
            i += 1 
    return query

def generate_insert(dict):
    column_list = '('
    i = 1
    for key in tc.get_column_config().keys():
        column_list += key
        if i >= len(tc.get_column_config()):
            column_list+=')'
        else:
            column_list+=', '
        i+=1
    query = "INSERT INTO {0} {1} VALUES (".format(tc.get_table_name(), column_list)
    i = 1
    for key, val in dict.items():
        if type(val) is str:
            query+="'{}'".format(val.replace("'", ''))
        else:
            query+= str(val)
        if i >= len(dict):
            query += ')'
        else:
            query += ', '
        i += 1
    return query