#	@author: Vasim Bukhari
#	Analysis of Alforithms: Project 1 
#
import sys
import os

def main():
	
	try:
		nDataSet = 0	#Number of data sets
		nTeams = 0		#Number of Teams
		nGames = 0		#Number of Games played
		#Opening and reading input.txt file 
		with open('input.txt', 'r') as inputFile:
			with open('output3.txt', 'w') as outFile:
				nDataSet = int(inputFile.readline())	#first line state number of data sets
				print "Number of DataSets: %d" % nDataSet
				#iterate over to collect all data sets from input file
				for i in range(nDataSet):				
					inputFile.readline()					#Skip second line of input file
					nTeamsNGames = inputFile.readline().split(' ')	
					nTeams = int(nTeamsNGames[0])			#Number of Teams
					nGames = int(nTeamsNGames[1]) 			#Number of Games played
					# print "Number of teams: %d" % nTeams
					# print "Number of games: %d" % nGames
					teamsDict ={}							#creating and initializing Dictionary

					#iterate over to collect name of teams from input file
					for j in range(nTeams):
						#teamsName.append(inputFile.readline().rstrip().split(' '))
						line = inputFile.readline().strip()
						obj = Fixtures(j, line)
						teamsDict[line] = obj#.__dict__

					#iterate over to collect all games results from input file
					for k in range(nGames):

						line = inputFile.readline().strip().split()  
						homeT = line[0]			#Name of home team
						homeG = int(line[1])	#Number of goals of home team
						awayG = int(line[3])	#Number of goals of away team
						awayT = line[4]			#Name of away team
						#print homeT, homeG, awayT, awayG
						teamsDict[homeT].updateFixture(homeG, awayG)
						teamsDict[awayT].updateFixture(awayG, homeG)

					# print teamsDict
					sortedFixture = sorted(teamsDict.values(), cmp=Fixtures.number_compare)
					#sortedFixture = sorted(teamsDict, key=Fixtures.number_compare)
					num=0
					outFile.write("%d\n"% nTeams)
					outFile.write("%d. %s\n" % (num+1, sortedFixture[0]))
					for x in range(1, nTeams):
						if(sortedFixture[x-1].checkRanking(sortedFixture[x])):
							num = x
							outFile.write("%d. %s\n"% (num, sortedFixture[x]))
						else:
							outFile.write("%d. %s\n"% (x+1, sortedFixture[x]))
					outFile.write('\n')

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
		self.percentPoints = 0.00

	#Method updates the number of games played, number of goals(Earn, Suffered), 
	#and number of points, num
	def updateFixture(self, homeG, awayG):
		#if win game, add 3 points 
		if (homeG > awayG):	self.numPoints += 3
		#if draw, add 1 points
		elif(homeG == awayG): self.numPoints += 1 
		#if lost, no point added
		else: pass
		#update number of games played
		self.numGames += 1
		#update number of goals earned
		self.numGoals = self.numGoals + homeG		
		#update number of goals suffered	
		self.numSuffGoals = self.numSuffGoals + awayG	
		#update number of goals difference
		self.goalDifference = self.findGoalDiff()
		#update number of percentPoints
		self.percentPoints = self.findPercentPoint()
	
	#compare according to specified criteria of classification
	# Number of Points Scored > Goal difference > Number of Scored Goals > Position in classification
	def number_compare(x, y):
		
		if(x.numPoints > y.numPoints):	
			return -1
		elif(x.numPoints < y.numPoints):
			return 1
		elif(x.goalDifference > y.goalDifference): 
			return -1
		elif(x.goalDifference < y.goalDifference):
			return 1
		elif(x.numGoals > y.numGoals):	
			return -1
		elif(x.numGoals < y.numGoals):	
			return 1
		elif(x.teamPosition > y.teamPosition):
			return -1
		elif(x.teamPosition < y.teamPosition):
			return 1
		else:
			return 0
	def checkRanking(x, y):
		if(x.numPoints == y.numPoints) and (x.goalDifference == y.goalDifference) and (x.numGoals == y.numGoals):
			return True
	def __str__(self):
		return " ".join(map(str,
		[self.teamName, self.numPoints, self.numGames,
		self.numGoals, self.numSuffGoals, self.goalDifference,
		"%.2f" % self.percentPoints]
		))
	#calculates the percent points
	def findPercentPoint(self):
		temp = 100.00
		#self.percentPoints = 100 if no game is played
		if(self.numGames == 0):	
			return temp 		
		else: 
			#number of points divide with number of games played times 3 point
			temp = 100.00*self.numPoints/(3*self.numGames)
			return temp

	#calculate goal difference
	def findGoalDiff(self):
	#def goalDifference(self):
		return (self.numGoals - self.numSuffGoals)


if __name__ == '__main__':
	main()