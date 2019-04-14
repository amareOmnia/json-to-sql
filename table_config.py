# Configure the pSQL table name, columns, and data types
# Currently configured to import reddit comment data
# Change values here to setup a different kind of table

# Login options for database connection
def get_db_login():
    return{
        'host'      : 'localhost',
        'database'  : 'reddit',
        'user'      : 'postgres',
        'password'  : ''
    }


# Name of table within database
def get_table_name():
    return 'comments'

# Each key is a column name, its value is the pSQL data type
def get_column_config():
    return{
        'comment_id': 'text',
        'parent_id' : 'text',
        'score'     : 'integer',
        'subreddit' : 'text',
        'body'      : 'text'
    }

# Grabbed by handle_bad_text to replace unquoted text in JSON that python doesn't like
def get_bad_text():
    return{
        'false' : 'False',
        'true'  : 'True',
        'null'  : 'None',
        '"id"'  : '"comment_id"',
        '\\"'   : "'",
        '\\'    : ' '
    }