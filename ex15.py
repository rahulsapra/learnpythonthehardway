filename = raw_input("File to open: ")
txt = file(filename)
print "your file as raw is %r" % txt.read()
#print "your file as string is %r" % txt.read()