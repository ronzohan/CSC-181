import cPickle as pickle
from DataFile import DataFile

class FileOperations:
	def SaveFileInfo(self,data,filename):
		# do serialization here
		pickle.dump(data,open(filename,"wb"))
	def LoadFileInfo(self,filename,password):
		##return the datafile loaded if password matches
		data =  pickle.load(open(filename,"rb"))
		if data.password == password:
			return data
	def setPassword(self,password):
		self.password = password
	def getLeagueInfo(self,data):
		return data.league
	def getManagerInfo(self,data):
		return data.manager
	def getEventInfos(self,data):
		return data.events	
# my = DataFile("bundesliga","mourinho","win1win2","chelsea")
# my.league =  "bundesliga"
# fileOperation = FileOperations()
# # fileOperation.SaveFileInfo(my,"sample.p")
# my = fileOperation.LoadFileInfo("sample.p")
# print my.league



