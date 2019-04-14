import database
import table_create
import table_config
import argparse
import ast

parse = argparse.ArgumentParser()
parse.add_argument('filename')
args = parse.parse_args()

filename = args.filename
file = open(filename, 'r')

db = database.Database()

def handle_bad_text(dict_string):
    parsed = dict_string
    for bad, good in table_config.get_bad_text().items():
        parsed = parsed.replace(bad, good)
    return parsed

def create_dict_from_line(line_string):
    parsed_line = handle_bad_text(line_string)
    try:
        line_dict = eval(parsed_line)
    except:
        line_dict = None
    return line_dict

def refine_dict_to_spec(full_dict):
    refined_dict = {}
    # reduces dictionary to contain only the desired keys (defined in table_config.py)
    for key in table_config.get_column_config().keys():
        refined_dict[key] = full_dict[key]
    return refined_dict
        
def build_list_of_dicts(file):
    list_of_dicts = []
    i = 1
    for line in file:
        line_dict = create_dict_from_line(line)
        if line_dict == None:
            i +=1
            continue
        refined_dict = refine_dict_to_spec(line_dict)
        list_of_dicts.append(refined_dict)
        i +=1
    return list_of_dicts

data = build_list_of_dicts(file)

# table_query = table_create.generate_table_query()
# db.execute_query(table_query, False)
# exit()
for item in data:
    query = table_create.generate_insert(item)
    db.execute_query(query, False)