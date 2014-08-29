# -- coding: utf-8 --

name = 'Lars Österberg'
age = 25
height = 72 #inches
weight = 173 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Blond'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on how much coffee he's had." % teeth

print " -- "
print "If I add %d, %d and %d I get %d." % ( age, height, weight, age + height + weight )
