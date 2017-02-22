class Person(object):
	def __init__(self, name):
		self.name = name
		
class Employee(Person):
	def __init__(self, name, salary):
		super(Employee, self).__init__(name)
		self.salary = salary
		
emp = Employee("John", 2000)
print emp.name
print emp.salary		