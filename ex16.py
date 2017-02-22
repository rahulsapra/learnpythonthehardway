filename = raw_input("filename: ")
target = open(filename, "r+") # + with r only creates/updates the file if it doesn't exist. We can't write to this file. for that we need to open in again with w mode
firstLine = target.readline()
txt = target.read()
print "firstLine: ", firstLine
target.close()
print "full text: ", txt