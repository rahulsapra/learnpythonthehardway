from nose.tools import *
from ex47 import Room

def test_room():
	gold = Room("gold", "this is gold")
	assert_equal(gold.name, "goldsd")
	
#running the test
test_room()	
	