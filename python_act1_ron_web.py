def getMonthEqui(month):
	names = ('January','Febuary','March','April','May','June','July','August','September','October','November','December')
	equiName = ('The Black','The Vengeful','The Dark','The Red','The Cursed','The Savage','The White','The ugly','The Treacherous','The Blue','The Wicked','The Green')
	x = 1
	theName = ""
	for x in xrange(len(names)):
		if names[x] == month:
			theName =  equiName[x] 
	return theName

	
def getDayEqui(day):
	equiName = ('Gargoyle','Goblin','Creature','King/Queen','Witch/Warlock','Guardian','Fairy','Knight','Elf','Assassin','Sorcerer/Sorceress','Giant','Werewolf','Wizard','Ogre','Beast','Dragon','Ghost','Dwarf','Unicorn','Warrior','Spirit','Thief','Mermaid/Merman','Cyclops','Troll','Orc','Pirate','Vampire','Prince/Princess','Serpent')
	return equiName[day-1]
		

def getColorEqui(color):
	colorName = ('Red','Blue','Green','White','Black','Yellow','Purple','Orange','Brown','Cyan','Pink')
	equiColor = ('of the Night','of the Seas','of the Forest','of the North','of the Shadows','of the Dead','of the East','of the West','of the Desert','of the South','of the Mountains')
	x = 1
	theName = ""
	for x in xrange(len(colorName)):
		if colorName[x] == color:
			theName =  equiColor[x] 
	return theName


def index(month,day,color):
	return getMonthEqui(month) + " " + getDayEqui(day) + " " +getColorEqui(color)


 
print index("March",13,"Blue")

