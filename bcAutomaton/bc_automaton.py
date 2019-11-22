import GOD
import random
import sys
import time
import operator

def birdcageIteration():

	mary = GOD.Generator()

	# the following lines contain all the data to build a complete automaton
	size = (width, height) = (80,20)
	topologyData = ("GridTopology", 0)
	neighborData = ("VonNeumannNeighborhood", )
	ruleData = ("ReductionRule", (operator.xor, 0))
	automatonData = ("SynchronousAutomaton_2D", )
	seed = (0,0)

	# invoke God.Generator's automaton creation method with the data given above
	terra = mary.generateAutomaton(size, topologyData, neighborData, ruleData, automatonData)
	mary.seedAutomaton(terra, seed)

	magdalen = GOD.Organizer(terra)
	doomsday = 1000000
	populationMax = 462

	# here cometh the main iteration cycle
	while magdalen.annum < doomsday:
		print "time is", magdalen.annum
		population = magdalen.iterateAutomaton()
		print "population is", population
		if population > populationMax:
			break

	print populationMax
#	for x in range(width):#		for y in range(height):
#			print terra.get((x,y))
	


if __name__ == "__main__":
	birdcageIteration()

