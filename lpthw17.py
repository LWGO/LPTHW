from sys import argv; from os.path import exists; x, y, z = argv; print "Copying %s to %s" % (y, z); a = open(y); b = a.read(); print "The input file is %d bytes long." % len(b); print "Output exists? %r" % exists(z); c = open(z, 'w'); c.write(b); print "Alright, done."; c.close(); a.close()

