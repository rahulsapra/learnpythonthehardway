def convert_num(num):
	try:
		return int(num)
	except ValueError:
		return None
		
print convert_num(10)
print convert_num('hello')		