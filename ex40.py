class Fruit(object):
	def __init__(self, name):
		self.name = name
	
	def printname(self):
		return self.name
		
obj = Fruit("apple")
print obj.printname()		