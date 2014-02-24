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
					line = inputFile.readline().rstrip().split(' ')
					obj = Fixtures(j, line[0])
					teamsDict[line[0]] = obj.__dict__
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
		if (homeG > awayG):	self.numPoints = self.numPoints + 3
		#if draw, add 1 points
		elif(homeG == awayG): self.numPoints = self.numPoints + 1
		#if lost, no point added
		else: pass

		self.numGoals = self.numGoals + homeG			#update number of goals earned
		self.numSuffGoals = self.numSuffGoals + awayG	#update number of goals suffered

		#self.__dict__.update(dictionary)
	#calculate goal difference
	def goalDifference(goalScored, goalSuffered):
		return abs(goalScored - goalSuffered)
	#print team data
	def printFixture():
		pass

if __name__ == '__main__':
	main()