import GOD
import random
import sys
import time

def startExecutionNormal():
	"""start normal execution cycle with sound and visual display

	return -->> 1

	Visual display through curses terminal control module
	Sound effectus through csound courtesy of Ernesto Illescas"""

	print "Ready for full audiovisual execution...commence primary ignition!"

	import curses#, sound
	global curses#, sound
	#curses.wrapper is the kosher way to fire up curses visual services; it
	#guarantees that the terminal will not be left stranded in an ocean of
	#insanity if the program terminates exceptionally
	curses.wrapper(main)

	return 1

def main():

	mary = GOD.Generator()
	#sound.startSoundServer()

	# setting the curses colour pairs
	#setCursesColors()

	# the following lines contain all the data to build a complete automaton
	# size = (width, height) = (int(sys.argv[-4]),int(sys.argv[-3]))
	size = (width, height) = (80,20)
	# del sys.argv[-4:-2]
	topologyData = ("GridTopology", 0)
	neighborData = ("VonNeumannNeighborhood", )
	import operator
	ruleData = ("ReductionRule", (operator.xor, 0))
	automatonData = ("SynchronousAutomaton_2D", )
	# invoke God.Generator's automaton creation method with the data given above
	doomsday = 15000
	terra = mary.generateAutomaton(size, topologyData, neighborData, ruleData, automatonData)
	magdalen = GOD.Organizer(terra)

	population = 0

	
	display = mary.generateDisplay(terra, size)
	#sound.startBackground()
	#sound.startBackgroundControl()
	# here cometh the main iteration cycle
	while population < 450:
		print "time is", magdalen.annum
		#print "biblos is", biblos
		population = magdalen.iterateAutomaton()
		print "population is", population
		populationNorm = float(population) / operator.mul(width,height)
		#magdalen.refreshDisplay(display)
		#soundControlCells = [terra.get((22,18)), terra.get((40,18)), terra.get((64,18))]
		#sound.inputDataControl(soundControlCells, populationNorm, magdalen.annum)
		#time.sleep(.1)

	#sound.stopSoundServer()
	del sys.argv[1:]

if __name__ == "__main__":
	main()

