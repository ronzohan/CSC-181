import unittest
from python_act2 import *

class MyTest(unittest.TestCase):
    def test_01_testOutput(self):
        self.failIf(index(object,"January",1,"Blue") != "The Black Gargoyle of the Seas","Wrong output")
    def test_02_testOutput(self):
        self.failIf(index(object,"Febuary",2,"Blue") != "The Vengeful Goblin of the Seas","Wrong output")
    def test_03_testOutput(self):
        self.failIf(index(object,"March",4,"Red") != "The Dark King/Queen of the Night","Wrong output")

# def suite():
	# suite_ = unittest.TestSuite()
	# suite_.addTest(MyTest())
	# return suite_
	
# runner = unittest.TextTestRunner()
# test_suite = suite()
# runner.run(test_suite)

# enables to run all the tests defined above at once
if __name__ == '__main__':
	unittest.main()
