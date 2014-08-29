#imports argv parameter from python system library
from sys import argv
#sets input_file variable to argv
script, input_file = argv
#defines the print_all function to read
def print_all(f):
	print f.read()
#defines the rewind function to reset the line count to 0	
def rewind(f):
	f.seek(0)
#defines the print_a_line function to print lines based on the current linecount	
def print_a_line(line_count, f):
	print line_count, f.readline()

#sets the current_file variable to be the contents of the input file specified in argv	
current_file = open(input_file)

#prints text
print "First, let's print the whole file:"
#uses the print_all function to print the entire input file
print_all(current_file)

#prints text
print "Now let's rewind, kind of like a tape:"
#uses the rewind function to reset the line count to 0
rewind(current_file)

#prints more text
print "Let's print three lines:"
#sets the current line to 1, then uses the print_a_line function to print current line
current_line = 1
print_a_line(current_line, current_file)
#adds 1 to the current line count, then uses the print_a_line function to print current line
current_line += 1
print_a_line(current_line, current_file)
#adds 1 to the current line count, then uses the print_a_line function to print current line
current_line += 1
print_a_line(current_line, current_file)
