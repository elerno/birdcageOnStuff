import GOD
import random
import sys
import time

def startExecutionNormal():
	"""start verbose execution cycle with no visual display or sound

	return -->> 1"""

	mary = GOD.Generator()

	# the following lines contain all the data to build a complete cellular automaton
	size = (width, height) = (80,20)
	topologyData = ("GridTopology", 0)
	neighborData = ("VonNeumannNeighborhood", )
	import operator
	ruleData = ("ReductionRule", (operator.xor, 0))
	automatonData = ("SynchronousAutomaton_2D", )
	doomsday = 1500
	
	# invoke GOD.Generator's automaton creation method with the data given above
	terra = mary.generateAutomaton(size, topologyData, neighborData, ruleData, automatonData)
	print "mary has created terra"
	mary.seedAutomaton(terra)

	# now call a GOD.Organizer to oversee this automaton
	magdalen = GOD.Organizer(terra)
	magdalen.generator = mary

	
	# here cometh the main iteration cycle
	while magdalen.annum < doomsday:
		print "the time now is \t", magdalen.annum
		# GOD.Organizer iterates the c.a. and makes sure the world keeps revolving
		print "the time now is \t", int(terra.tellAgents())
		magdalen.iterateAutomaton()
		

	del sys.argv[1:]
	print "Done"
	return 1

if __name__ == "__main__":
	startExecutionNormal()

