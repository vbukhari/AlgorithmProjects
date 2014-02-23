#	@author: Vasim Bukhari
#	Analysis of Alforithms: Project 1 
import sys
import os

def main():
	
	try:
		nDataSet = 0
		nTeams = 0
		nGames = 0
		teamsName = []
		scoreTable = []
		#teamsDict = {}
		with open('input2.txt', 'r') as inputFile:
			nDataSet = int(inputFile.readline())
			print "Number of DataSets: %d" % nDataSet
			for i in range(nDataSet):
				inputFile.readline()
				nTeamsNGames = inputFile.readline().split(' ')
				nTeams = int(nTeamsNGames[0])
				nGames = int(nTeamsNGames[1]) 
				print "Number of teams: %d" % nTeams
				print "Number of games: %d" % nGames
				teamsDict ={}
				obj = Fixtures(0, 0, 0, 0, 0, 0, 0)
				for j in range(nTeams):
					#teamsName.append(inputFile.readline().rstrip().split(' '))
					line = inputFile.readline().rstrip().split(' ')
					#teamsDict[line[0]] =  [0, 0, 0, 0, 0, 0.0]
					#obj = Fixtures(teamsDict)
					teamsDict[line[0]] = obj.__dict__
					#dict((key, value) for key, value in team1.__dict__.iteritems())
					#teamsDict[team1.teamName]= team1
					#teamsDict['name'].append(inputFile.readline().rstrip().split(' '))
					#print inputFile.readline().strip().split()
				#print teamsDict
				for k in range(nGames):
					#scoreTable.append(inputFile.readline().strip().split(' '))
					line = inputFile.readline().strip().split()  
					homeTeam = line[0]
					homeGoal = int(line[1])
					awayGoal = int(line[3])
					awayTeam = line[4]
					#print homeTeam, homeGoal, awayTeam, awayGoal
					#print scoreTable
					for x, y in teamsDict.iteritems():
						if x == homeTeam:
							for k, v in y.iteritems():
								if k == "numGoals":
									y[k] += homeGoal
								#print homeGoal
						elif x == awayTeam:
							for k, v in y.iteritems():
							 	if k == "numGoals":
							 		y[k] += awayGoal
							#print homeTeam
						# if x == awayTeam:
						# 	for k, v in y.iteritems():
								#print awayGoal
							# for k, v in y.items():
							# 	if k == "numGoals":
							# 		y[k] = awayGoal
							#print awayTeam
				print teamsDict
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
	def __init__(self, teamPosition,numPoints,numGames, numGoals,numSuffGoals,goalDifference,percentPoin):
		self.teamPosition = teamPosition
		#self.teamName = teamName
		self.numPoints = numPoints
		self.numGames = numGames
		self.numGoals = numGoals
		self.numSuffGoals = numSuffGoals
		self.goalDifference = goalDifference
		self.percentPoints = percentPoin
		# for k, v in dictionary.items():
		# 	setattr(self, k, v)

	#update the number of goals and number of points and lost or win
	def update(self, dictionary):
		self.__dict__.update(dictionary)
	#calculate goal difference
	def goalDifference(goalScored, goalSuffered):
		return abs(goalScored - goalSuffered)
	#print team data
	def printFixture():
		pass

if __name__ == '__main__':
	main()