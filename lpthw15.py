# tells python to use the argv function
from sys import argv
#sets filename variable to argv
script, filename = argv
#tells the program to open the txt file in the opening command
txt = open(filename)
#prints Here's your file and then the filename
print "Here's your file %r:" % filename
#prints the contents of the file
print txt.read()
#prints a prompt for you to enter the filename again
print "Type the filename again:"
#uses raw_input to pull your new answer as a variable
file_again = raw_input("> ")
#sets the variable txt_again to be the value inside the new file you just assigned
#	to the file_again variable
txt_again = open(file_again)
#prints the txt_again value (what was in the file_again file)
print txt_again.read()
