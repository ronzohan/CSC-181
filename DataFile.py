class DataFile:
	def __init__(self,league,manager,events,teams):
		self.league = league
		self.manager = manager
		self.events = events
		self.teams = teams
	
	#temporary password get and set, not diving into deep at the moment
	def setPassword(self,password):
		self.password = password
	#temporary password get and set, not diving into deep at the moment
	def getPassword(self):
		return self.password