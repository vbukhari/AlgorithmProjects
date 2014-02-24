#	@author: Vasim Bukhari
#	Analysis of Alforithms: Project 1 
import sys
import os

def main():
	
	try:
		nDataSet = 0	#Number of data sets
		nTeams = 0		#Number of Teams
		nGames = 0		#Number of Games played
		#Opening and reading input.txt file 
		with open('input2.txt', 'r') as inputFile:
			nDataSet = int(inputFile.readline())		#first line state number of data sets
			print "Number of DataSets: %d" % nDataSet
			#iterate over to collect all data sets from input file
			for i in range(nDataSet):				
				inputFile.readline()					#Skip second line of input file
				nTeamsNGames = inputFile.readline().split(' ')	
				nTeams = int(nTeamsNGames[0])			#Number of Teams
				nGames = int(nTeamsNGames[1]) 			#Number of Games played
				print "Number of teams: %d" % nTeams
				print "Number of games: %d" % nGames
				teamsDict ={}							#creating and initializing Dictionary
				#obj = Fixtures(0, "")
				#iterate over to collect name of teams from input file
				for j in range(nTeams):
					#teamsName.append(inputFile.readline().rstrip().split(' '))
					line = inputFile.readline().strip()
					obj = Fixtures(j, line[0])
					teamsDict[line] = obj#.__dict__
					#dict((key, value) for key, value in team1.__dict__.iteritems())
					#teamsDict[team1.teamName]= team1
					#teamsDict['name'].append(inputFile.readline().rstrip().split(' '))
				#print teamsDict
				#iterate over to collect all games results from input file
				for k in range(nGames):
					#scoreTable.append(inputFile.readline().strip().split(' '))
					line = inputFile.readline().strip().split()  
					homeT = line[0]			#Name of home team
					homeG = int(line[1])	#Number of goals of home team
					awayG = int(line[3])	#Number of goals of away team
					awayT = line[4]			#Name of away team
					#print homeT, homeG, awayT, awayG
					teamsDict[homeT].updateTeam(homeG, awayG)
					teamsDict[awayT].updateTeam(awayG, homeG)
					#obj.__dict__.update(teamsDict)

				sortedFixture = sorted(teamsDict, key=cmp_to_key(num_compare))
				#sortedFixture = sorted(teamsDict.values(), cmp=Fixtures.cmp_to_key)
				# for key, value in teamsDict.iteritems():
				# 	#for x in value:
				# 	print value
				
	except IOError as e:
		print "I/O error({0}): {1}".format(e.errno, e.strerror)
	except ValueError:
		print "Could not convert data to an integer."
	except:
		print "Unexptected error:", sys.exc_info()[0]
		raise
	inputFile.close()

class Fixtures(object):
	"""docstring for Fixtures"""
	def __init__(self, teamPosition, teamName):
		self.teamPosition = teamPosition
		self.teamName = teamName
		self.numPoints = 0
		self.numGames = 0
		self.numGoals = 0
		self.numSuffGoals = 0
		self.goalDifference = 0
		self.percentPoints = 0
		# for k, v in dictionary.items():
		# 	setattr(self, k, v)

	#Method updates the number of games played, number of goals(Earn, Suffered), 
	#and number of points, num
	def updateTeam(self, homeG, awayG):
		#if win game, add 3 points 
		if (homeG > awayG):	self.numPoints += 3
		#if draw, add 1 points
		elif(homeG == awayG): self.numPoints += 1 
		#if lost, no point added
		else: pass
		#update number of goals earned
		self.numGoals = self.numGoals + homeG		
		#update number of goals suffered	
		self.numSuffGoals = self.numSuffGoals + awayG	
		#update number of goals difference
		self.goalDifference = self.numGoals - self.numSuffGoals	
		#update number of percentPoints
		if(self.numGames == 0):	self.percentPoints = 100
		else: self.percentPoints = 100*(self.numPoints/(3*self.numGames))

		#self.__dict__.update(dictionary)

	def num_compare(x, y):
		return x - y

	def cmp_to_key(mycmp):

		class K(object):
			"""docstring for K"""
			def __init__(self, obj, *args):
				self.obj = obj
			def __lt__(self, other):
				return mycmp(self.obj, other.obj) < 0
	        def __gt__(self, other):
	            return mycmp(self.obj, other.obj) > 0
	        def __eq__(self, other):
	            return mycmp(self.obj, other.obj) == 0
	        def __le__(self, other):
	            return mycmp(self.obj, other.obj) <= 0
	        def __ge__(self, other):
	            return mycmp(self.obj, other.obj) >= 0
	        def __ne__(self, other):
	        	return mycmp(self.obj, other.obj) != 0

	    return K
				

	#calculate goal difference
	def goalDifference(goalScored, goalSuffered):
		return abs(goalScored - goalSuffered)
	#print team data
	def printFixture():
		pass

if __name__ == '__main__':
	main()