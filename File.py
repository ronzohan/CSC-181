import DataFile.py
class FileOperations:
	def SaveFileInfo(self,data):
		print "asd"
		##do serialization here

	def LoadFileInfo(self,data,filename):
		## --not yet finished 
		## --double check pickle arguments
		##  data.league = pickle(filename,)
		##
		print "asd" 
	
	def setPassword(self,password):
		self.password = password

	def getLeagueInfo(self,data):
		return data.league
	def getManagerInfo(self,data):
		return data.manager
	def getEventInfos(self,data):
		return data.events	
	
my = DataFile("barclays","mourinho","win1win2","chelsea")
my.league =  "bundesliga"
fileOperation = FileOperations()
fileOperation.SaveFileInfo(my)



