# Configure the pSQL table name, columns, and data types
# Currently configured to import reddit comment data
# Change values here to setup a different kind of table

def get_table_name():
    return 'comments'

def get_column_config():
    return{
        'id'        : 'charvar(8)',
        'parent_id' : 'charvar(8)',
        'score'     : 'integer',
        'subreddit' : 'text',
        'body'      : 'text'
    }