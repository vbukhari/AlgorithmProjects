#	@author: Vasim Bukhari
#	Analysis of Alforithms: Project 3 |
#

import sys
import os
import networkx as nx

def validNode(location, dimension):
	row, column = location
	if (row>= dimension or column >= dimension or row < 0 or column < 0):
		return False
	else:
		return True

def checkColor(col_actual, col_original):
	if col_actual == col_original:
		return False
	else:
		return True

def moveTo(location, direction):
	row, column = location
	if direction == "N":
		row -= 1
	elif direction == "S":
		row += 1
	elif direction == "E":
		column += 1
	elif direction == "W":
		column -= 1
	elif direction == "NE":
		row -= 1
		column += 1
	elif direction == "NW":
		row -= 1
		column -= 1
	elif direction == "SE":
		row += 1
		column += 1
	elif direction == "SW":
		row += 1
		column -= 1
	elif direction == "0":
		row = 99999999
		column = 99999999
	return (row, column)


def addEdges(G, location, dimension):
	original_color, original_direction = G.node[location]['col'], G.node[location]['dir']
	original_location = location
	location = moveTo(original_location, original_direction)
	weight = 1
	while validNode(location, dimension):
		if checkColor(G.node[location]['col'], original_color):
			G.add_edge(original_location, location, {'dir':original_direction, 'weight':weight})
		location = moveTo(location, original_direction)
		weight += 1

def printPath(G, path):
	for n in range(len(path)-1):
		todo =  G.edge[path[n]][path[n+1]]
		print todo['dir'] + '-' + str(todo['weight']),

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
				# print "Number of Mazes: %d"% nMazes
				# outFile.write("%d\n"%nMazes)
				#iterate over all mazes

				for aMaze in range(nMazes):
					#Skip for blank line between every consecutive maze
					inputFile.readline()
					# outFile.write('\n')
					#This line determine dimension of the maze
					nDimension = int(inputFile.readline())
					# print "Dimentsion of Maze %d"% nDimension
					# outFile.write("%d\n"%nDimension)
					#iterate over a Maze
					nlist = []
					
					for mazeLine in range(nDimension):
						# outFile.write("%s"%inputFile.readline())
						row = inputFile.readline().strip().split(' ')
						nlist.append([])
						for x in row:
							nlist[mazeLine].append(x)
					nlist[nDimension-1][nDimension-1] = '0-0'
					# print nlist[0][0]
					# print nlist[nDimension-1][nDimension-1] 
					# print "nlist:\n", nlist
					dirList, colorList = [], []
					dictList = []
					allList = []
					locList= []
					for i in range(nDimension):
						dirList.append([])
						colorList.append([])
						dictList.append([])
						locList.append([])
						for j in range(nDimension):
							direction, color = nlist[i][j].split('-')
							dirList[i].append(direction)
							colorList[i].append(color)
							d = {'dir': direction, 'col':color}
							dictList[i].append(d)
							location = tuple([i, j])
							allList.append(tuple([location, d]))
							locList[i].append(location)
					# print "dirlist:\n", dirList
					# print "color list:\n", colorList
					# print "dictionary: \n", dictList
					# print "location: \n", locList
					# print "allList: \n", allList
					G = nx.DiGraph()
					G.add_nodes_from(allList)
					# print "Nodes: \n", sorted(G.nodes(data=True))

					for node in sorted(G.nodes()):
						addEdges(G, node, nDimension)
					# print "Edges: \n", G.edges()

					path = nx.shortest_path(G, (0, 0), (nDimension-1, nDimension-1))
					
					for n in range(len(path)-1):
						todo = G.edge[path[n]][path[n+1]]
						outFile.write(todo['dir'] + '-' + str(todo['weight'])+ ' ')
					outFile.write('\n')
					outFile.write('\n')
					# printPath(G, path)
					# print "\n"

					# def printPath(G, path):
					# 	for n in range(len(path)-1):
					# 		todo =  G.edge[path[n]][path[n+1]]
					# 		print todo['dir'] + '-' + str(todo['weight']),


	except IOError as e:

		print "I/O error({0}): {1}".format(e.errno, e.strerror)

	except ValueError:

		print "Could not convert data to an integer."

	except:

		print "Unexptected error:", sys.exc_info()[0]
		raise



# class mazeGraph(object):
# 	"""docstring for mazeGraph"""
# 	def __init__(self, arg):
# 		super(mazeGraph, self).__init__()
# 		self.arg = arg
		

if __name__ == '__main__':
	
	main()