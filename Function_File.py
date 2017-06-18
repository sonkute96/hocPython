
from sys import argv

script, input_file = argv

def print_all(f):

    print f.read()

def rewind(f):

    f.seek(0)

def print_a_line(line_count, f):
    
    print line_count, f.readline()
# f.readline() doc theo dong thu tu tu 1 -> n dong <khong theo line_count>

current_file = open(input_file)

#print_all(current_file)

rewind(current_file)

current_line = 1
print_a_line(current_line,current_file)

current_line = 9
print_a_line(current_line,current_file)
