#	@author: Vasim Bukhari
#	Analysis of Alforithms: Project 3 |
#

import sys
import os

def main():

	nMazes = 0 #Number of Maze
	nDimension = 0 # Dimentsion of the maze

	#Handling any exception for reading and writing the file or any unexpected error
	try:
		#Opening and reading input.txt file
		with open('input.txt', 'r') as inputFile:
			with open('bukhari.txt', 'w') as outFile:
				#first line in input file state number of mazes
				nMazes = int(inputFile.readline())
				for aMaze in range(nMazes):
					#Skip for blank line between every consecutive maze
					inputFile.readline()
					#This line determine dimension of the maze
					nDimension = int(inputFile.readline())


	except IOError as e:

		print "I/O error({0}): {1}".format(e.errno, e.strerror)

	except ValueError:

		print "Could not convert data to an integer."

	except:

		print "Unexptected error:", sys.exc_info()[0]
		raise



class mazeGraph(object):
	"""docstring for mazeGraph"""
	def __init__(self, arg):
		super(mazeGraph, self).__init__()
		self.arg = arg
		

if __name__ == '__main__':
	
	main()