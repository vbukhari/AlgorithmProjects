#	@author: Vasim Bukhari
#	Analysis of Alforithms: Project 1 
import sys
import os

def main():
	
	try:
		nDataSet = 0
		nTeams = 0
		nGames = 0
		teams = []
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
				for j in range(nTeams):
					teams.append(inputFile.readline().rstrip().split(' '))
				print teams
				for k in range(nGames):
					pass

				break
			# for x in range(nDataSet):
			# 	print(inputFile.readline())

			# for line in inputFile:
			# 	print line
		# 		data = [line.rstrip().split(',') for line in inputFile]
		# nDataSet= int(data[0].strip())
		# print nDataSet
	except IOError as e:
		print "I/O error({0}): {1}".format(e.errno, e.strerror)
	except ValueError:
		print "Could not convert data to an integer."
	except:
		print "Unexptected error:", sys.exc_info()[0]
		raise

	# print data
	# print len(data)
	# nDataSet = 0
	# for x in data:
	# 	for i in x:
	# 		print i#x.index(i)
	# 		#if(i.index(x)==0):
	# 		#	nDataSet= int(i)

	# for nDataSet in data[0].:
	# 	pass

	#print nDataSet

	# nDataSet = data[0]
	# nTeams = data[2:]
	# print nTeams
	# for x in data[2]:
	# 	print x
	



	# for x in data:
	# 	print data
		# for i in x:
		#  	print i 
	#inputFile = open("input2.txt", "r")
	#lines = inputFile.readlines()
	# allItems = []
	# for line in inputFile:
	# 	data = line.rstrip().split(',')
	# 	allItems.append(data)
		# data = data.split(',')
		# data = data.sort(key=lamda item: item[4]) 
		# print data
	#print lines
	#print len(lines)
	inputFile.close()

def sortList():
	pass

def readFile():
	pass

if __name__ == '__main__':
	main()