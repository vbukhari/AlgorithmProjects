#	@author: Vasim Bukhari
#	Analysis of Algorithms: Project 1 
#

import sys
import os
from operator import itemgetter, attrgetter

def main():
	#catch any exception or error reading or writing file or value eror or any unexpected error
	try:

		nDataSet = 0	#Number of data sets
		nTeams = 0		#Number of Teams
		nGames = 0		#Number of Games played

		#Opening and reading input.txt file 
		with open('input.txt', 'r') as inputFile:

			with open('bukhari.txt', 'w') as outFile:

				nDataSet = int(inputFile.readline())	#first line state number of data sets
				
				print "Number of DataSets: %d" % nDataSet
				
				#iterate over to collect all data sets from input file
				for aSet in range(nDataSet):				
					
					inputFile.readline()					#Skip second line of input file
					nTeamsNGames = inputFile.readline().split(' ')	
					
					nTeams = int(nTeamsNGames[0])			#Number of Teams
					nGames = int(nTeamsNGames[1]) 			#Number of Games played
					# print "Number of teams: %d" % nTeams
					# print "Number of games: %d" % nGames
					fixturesDict ={}							#creating and initializing Dictionary

					#iterate over to collect name of teams from input file
					for nTeam in range(nTeams):

						line = inputFile.readline().strip()
						obj = Fixtures(nTeam, line)
						fixturesDict[line] = obj

					#iterate over to collect all games results from input file
					for match in range(nGames):

						line = inputFile.readline().strip().split() 
						homeT, homeG, awayG, awayT = line[:2] + line[3:]
						
						#print homeT, homeG, awayT, awayG
						processGame(fixturesDict[awayT], int(awayG), int(homeG))
						processGame(fixturesDict[homeT], int(homeG), int(awayG))


					# print teamsDict
					#sortedFixture = sorted(teamsDict.values(), cmp=Fixtures.number_compare)
					sortedFixture = sorted(teamsDict, key=attrgetter('numPoints', 'goalDifference', 'numGoals', 'teamPosition'))
					num=0

					# print fixturesDict
					listFixtures = fixturesDict.values()
					sortedFixture = sorted(listFixtures, cmp = fixtureComparison)
					#sortedFixture = sorted(fixturesDict, key)
					
					outFile.write("%d\n"% nTeams)
					outFile.write("%d. %s\n"%(1, sortedFixture[0].toString()))
					
					num=1

					for x in range(1, nTeams):

						if(sortedFixture[x].checkRanking(sortedFixture[x-1]) == True):
							pass
						else:
							num = x + 1

						outFile.write("%d. %s\n"%(num, sortedFixture[x].toString()))

					outFile.write('\n')

	except IOError as e:

		print "I/O error({0}): {1}".format(e.errno, e.strerror)

	except ValueError:

		print "Could not convert data to an integer."

	except:

		print "Unexptected error:", sys.exc_info()[0]
		raise

	inputFile.close()

#Class fixture for handing all values 
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
		self.percentPoints = 0.00
		self.number = 0
	
	#This method check number of points, goal differences and number goals 
	#tunr out to be same. IF they are this function return True
	#This method use to set same ranking if conditions come out to be True
	def checkRanking(x, y):

		temp = False
		
		if(x.numPoints != y.numPoints):
			temp = True
		if(x.goalDifference != y.goalDifference):
			temp = True
		if(x.numGoals != y.numGoals):
			temp = True
<<<<<<< HEAD
		return temp
	def __str__(self):
		return " ".join(map(str,
		[self.teamName, self.numPoints, self.numGames,
		self.numGoals, self.numSuffGoals, self.goalDifference,
		"%.2f" % self.percentPoints]
		))	
=======
		
		return not temp

	def toString(self):
		
		return ( 
		str(self.teamName) + " " +
		str(self.numPoints) + " " +
		str(self.numGames) + " " +
		str(self.numGoals) + " " +
		str(self.numSuffGoals) + " " +
		str(self.goalDifference) + " " +
		"%.2f"%self.percentPoints)

>>>>>>> f387451d687b60c329150ff7da44c0d3e1499465
	#calculates the percent points
	def findPercentPoint(self):
		
		temp = 100.00
		
		#self.percentPoints = 100 if no game is played
		if(self.numGames == 0):	
			return temp 		
		
		else: 
			#number of points divide with number of games played times 3 point
			temp = self.numPoints * 100.0 /(3*self.numGames)
			return temp

#Method updates the number of games played, number of goals(Earn, Suffered), 
#and number of points, num
def processGame(fixture, homeG, awayG):
	
	#if win game, add 3 points 
	if (homeG > awayG):	fixture.numPoints += 3
	
	#if draw, add 1 points
	elif(homeG == awayG): fixture.numPoints += 1 
	
	#if lost, no point added
	else: pass
	
	#update number of games played
	fixture.numGames += 1
	#update number of goals earned
	fixture.numGoals = fixture.numGoals + homeG		
	#update number of goals suffered	
	fixture.numSuffGoals = fixture.numSuffGoals + awayG	
	#update number of goals difference
	fixture.goalDifference = fixture.numGoals - fixture.numSuffGoals
	#update number of percentPoints
	fixture.percentPoints = fixture.findPercentPoint()

<<<<<<< HEAD
=======
#compare according to specified criteria of classification
# Number of Points Scored > Goal difference > Number of Scored Goals > Position in classification
def fixtureComparison(x, y):
	
	if(x.numPoints < y.numPoints): return 1
	elif(x.numPoints > y.numPoints): return -1
	elif(x.goalDifference > y.goalDifference): return -1
	elif(x.goalDifference < y.goalDifference): return 1
	elif(x.numGoals < y.numGoals): return 1
	elif(x.numGoals > y.numGoals): return -1
	elif(x.teamPosition > y.teamPosition): return 1
	elif(x.teamPosition < y.teamPosition): return -1
	else: return 0

>>>>>>> f387451d687b60c329150ff7da44c0d3e1499465
if __name__ == '__main__':
	
	main()
