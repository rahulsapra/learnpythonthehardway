from os.path import exists
#we can use semicolon to club two statements into one line
source = open("file.txt", "r");txt = source.read()
target = open("file1.txt", "w")
target.write(txt)
#check if a file exists
print exists("file.txt")
source.close()
target.close()