from sys import argv

script, filename, term = argv

f = open(filename)

def start_program():
    line_number = 0

    for word in f.read().split(): 
        line_number += 1
        if word == term:    
            print "Searching for %s in %s" % (word, filename)
            print "%s was successfully found in %s at line number %s" % (word, filename, line_number)
            
start_program()

