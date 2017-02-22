str1 = "hello world!"
str2 = "%s is the capital of '%s'" #single quotes inside double quotes
str3 = "do you smoke: %r"

print str1
print str2 % ("Delhi", "India")
print str3 % (False)
#concatenation
print str1 + str3 % (False) + str2 % ("Delhi", "India")

print "It's fleece was white as %s" % 'snow', #using , at the end will concat the output of the next line with this line
print "." * 10 #print the string 10 times