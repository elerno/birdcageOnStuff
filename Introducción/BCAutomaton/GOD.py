# import all the necessary modules:
# these are the core birdcage modules:
import topology
import neighborhood
import rule
import automaton
import genome as g
# these are the modules used for display
import visual as v
#import curses as c

class Generator:
	"""This object creates a code object from a genome and appends it onto
        the list of creatures. It also performs other creation-related functions
	such as generating a fully-functioning cellular automaton"""


	def generateAutomaton(self, size, tdata, ndata, rdata, adata):
		"""Create an instance of a birdcage automaton class

		size   ---> a Python tuple of integers
		tdata  ---> a Python tuple commencing with a string
		ndata  ---> a Python tuple commencing with a string
		rdata  ---> a Python tuple commencing with a string
                adata  ---> a Python tuple commencing with a string
		return -->> an Automaton object"""

		topologyClass = getattr(topology, tdata[0])
		topologyInstance = topologyClass(size, tdata[1])

		neighborhoodClass = getattr(neighborhood, ndata[0])
		neighborhoodInstance = neighborhoodClass(topologyInstance)

		ruleClass = getattr(rule, rdata[0])
		ruleInstance = ruleClass(neighborhoodInstance, rdata[1])

		automatonClass = getattr(automaton, adata[0])
		automatonInstance = automatonClass(ruleInstance)

		return automatonInstance


	def seedAutomaton(self, earth, seed):
		"""Initialise the automaton
		earth  ---> a birdcage automaton
		seed   ---> a 2-tuple with a valid topology address"""

		earth.set(seed,1)


class Organizer:
	"""This object coordinates the iteration-per-iteration functioning of the
	automata and its agents. It calls on the Organizer and Destroyer when
	necessary."""


	def __init__(self, earth):
		"""Create an Organizer instance

		earth ---> some complete birdcage Automaton instance"""

		self.earth = earth
		self.generator = None
		self.annum = 0


	def iterateAutomaton(self):
		"""Iterate the birdcage automaton associated to the Organizer

		return -->> population"""

		self.annum = self.annum + 1
		return self.earth.update()

		
		

