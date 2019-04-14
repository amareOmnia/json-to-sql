import database
import table_create
import argparse
import ast

parse = argparse.ArgumentParser()
parse.add_argument('filename')
args = parse.parse_args()

filename = args.filename
file = open(filename, 'r')

for line in file:
    line_dict = eval(line.replace('false','False').replace('true', 'True').replace('null','None'))
    print(line_dict)
    print(type(line_dict))
    break

print(table_create.generate_table_query())