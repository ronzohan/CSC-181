import unittest
from python_act1 import myClass

class MyTest(unittest.TestCase):
	def test_01_testOutput(self):
		mc = myClass()
		self.failIf(mc.index("March",13,"Blue") != "The Dark Werewolf of the Seas","Wrong output")
	def test_02_testOutput(self):
		mc = myClass()
		self.failIf(mc.index("Febuary",12,"Red") != "The Vengeful Giant of the Night","Wrong output")	



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
