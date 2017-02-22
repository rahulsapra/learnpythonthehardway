current_file = open("file.txt")

def printline(f):
	print f.readline()
	
printline(current_file)
printline(current_file)
printline(current_file)
printline(current_file) #prints nothing

#resetting the cursor to beginning of file
current_file.seek(0)
print "cursor reset complete"

printline(current_file)
printline(current_file)
printline(current_file)
printline(current_file)

current_file.seek(0)
print current_file.read()