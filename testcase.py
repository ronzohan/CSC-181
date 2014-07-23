import unittest
from File import FileOperations
from DataFile import DataFile

class MyTest(unittest.TestCase):
	def test_01_testPasswordMatch(self):
		my = DataFile("bundesliga","mourinho","win1win2","chelsea")
		my.setPassword("samplePassword123")
		fileOperation = FileOperations()
		fileOperation.SaveFileInfo(my,"sample.p")
		my = fileOperation.LoadFileInfo("sample.p","samplePassword123")
		self.failIf(my.getPassword() != "samplePassword123","Fail")
	
	def test_02_testLoadFromFileSucceed(self):
		my = DataFile("bundesliga","mourinho","win1win2","chelsea")
		my.setPassword("samplePassword123")
		fileOperation = FileOperations()
		fileOperation.SaveFileInfo(my,"sample.p")
		my.league =  "barclays premier league"
		my = fileOperation.LoadFileInfo("sample.p","samplePassword123")
		self.failIf(my.league != "bundesliga","Fail")
		
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
