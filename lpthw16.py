from sys import argv

script, filename = argv

print "We are going to erase %r." % filename
print "If you don't want that hit CTRL-C."
print "If you do want that hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I am going to ask you for 3 lines."

line1 = raw_input("line1 : ")
line2 = raw_input("line2 : ")
line3 = raw_input("line3 : ")

print "I'm going to write these to the file."

target.write(line1, "\n", line2, "\n", line3, "\n")

print "And finally we close it."
target.close()