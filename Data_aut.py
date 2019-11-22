## Automaton instantiation and data extraction classes.

import automata as aut

class MkData(object):
	"""Make a Birdcage cellular automaton, and construct a series of
	dictionaries related to it.
	"""
	def __init__(self, width=114, height=48, initCel=(0,0), noCels= 1000):
		""" Holds the initialization parameters, and instantiates a
		birdcage cellular automaton, its organizer, and a control automaton.
		width	---> width of the automaton's grid
		height	---> height of the automaton's grid
		initCel	---> first live cell
		noCels	---> number of cells to live at least once
		"""
		#Initialization parameters.
		self.width		= width
		self.height		= height
		self.initCel	= initCel
		self.noCels		= noCels
		self.size		= (self.width, self.height)
		#Instantiate the automaton, its organizer and an (empty)
		#control automaton.
		self.autmta		= aut.crearAutomata(self.size, self.initCel)
		self.autmtaOrg 	= aut.organizadorAutomata(self.autmta)
		self.ctrlAutmta = aut.crearAutomata(self.size, self.initCel)
		#Atributes derived from the class's methods.
		self.cllLstNItrNo	= self.iterToOrderdPartls()
		self.cllLst			= self.rmvIterNo()
		self.cllIndxDict	= self.mkCllIndx()
		self.coordVoxDict	= self.mkCllVox()

	def iterToOrderdPartls(self):
		""" Iterates the automaton until the number of cells needed -
		which will represent spectral partials - live once. Returns a
		list of tuples representing the cells' coordenates.
		"""
		livedOnceMin		= 1
		counter			= 1
		stop				= 0
		cellList	= ['iter0', self.initCel]

		#One iteration in order to initialize the automaton.
		self.autmtaOrg.iterateAutomaton()

		# Iterates the automaton until noCels have lived, and returns
		# a list with iteration numbers, and the order in which the
		# cells lived.
		while 1:
			if stop:
				break
			cellList.append('iter' + str(counter))
			for x in range(self.width):
				if stop:
					break				for y in range(self.height):
					if stop:
						break
					onOff = self.autmta.get((x, y))
					if onOff:
						if self.ctrlAutmta.get((x, y)) == 0:
							cellList.append((x, y))
							livedOnceMin += 1
						self.ctrlAutmta.set((x, y), 1)
						if livedOnceMin == self.noCels:
							stop = 1
							break
			self.autmtaOrg.iterateAutomaton()
			counter += 1
		return cellList


	def rmvIterNo(self):
		""" Removes the iteration number from the cllLstNItrNo.
		"""
		cllLst	= []

		for x in self.cllLstNItrNo:
			if isinstance(x, tuple):
				cllLst.append(x)
		return cllLst


	def mkCllIndx(self):
		""" Makes a dictionary with index : cell-coordinate pairs.
		"""
		coordIndx	= []
		indx		= 0

		for x in self.cllLst:
			newTuple = (str(x), indx)
			coordIndx.append(newTuple)
			indx += 1

		coordIndxDict = dict(coordIndx)
		return coordIndxDict


	def mkCllVox(self):
		""" Makes a dictionary with cell-coordinate : voice-number pairs.
		The voices work as instrument decimals.
		"""
		coordVox	= []
		counter	= 1

		for x in self.cllLst:
			vox = counter * .0001
			newTuple = (str(x), vox)
			coordVox.append(newTuple)
			counter += 1

		coordVoxDict = dict(coordVox)
		return coordVoxDict


class RunAutmta(MkData):
	"""Iterates the automaton in order to use it as spectral material.
	"""
	def __init__(self, width=114, height=48, initCel=(0, 0), strtCel=(0, 0),
					noCels= 500):
		""" Holds the initialization parameters, and instantiates a
		birdcage cellular automaton, its organizer, and a control automaton.
		width	---> width of the automaton's grid
		height	---> height of the automaton's grid
		initCel	---> first live cell for the dictionaries' construction
		strtCel	---> first live cell of the running automaton.
		noCels	---> number of cells to live at least once
		"""
		#Initialization parameters.
		MkData.__init__(self, width, height, initCel, noCels)
		self.strtCel = strtCel
		#Instantiate the automaton and its organizer.
		self.autmta		= aut.crearAutomata(self.size, self.strtCel)
		self.autmtaOrg 	= aut.organizadorAutomata(self.autmta)
		#Instantiate MkData, and get its initialization history and 
		#dictionaries.
		self.MkData			= MkData(self.width, self.height, self.initCel,
										self.noCels)
		self.initHist		= MkData.rmvIterNo(self.MkData)
		self.cllIndxDict	= MkData.mkCllIndx(self.MkData)
		self.coordVoxDict	= MkData.mkCllVox(self.MkData)


	def iterAutmta(self):
		""" Iterate the automaton.
		"""
		self.autmtaOrg.iterateAutomaton()


	def getLiveClls(self):
		""" Return the current live cells.
		"""
		liveCells = []
		for x in range(self.width):			for y in range(self.height):
				onOff = self.autmta.get((x, y))
				if onOff:
					liveCells.append((x, y))
		return liveCells



class CtrlAutmt(MkData):
	"""Iterates the automaton in order to use it as spectral material.
	"""
	def __init__(self, width=114, height=48, initCel=(0, 0)):
		""" Holds the initialization parameters, and instantiates a
		birdcage cellular automaton, its organizer, and a control automaton.
		width	---> width of the automaton's grid
		height	---> height of the automaton's grid
		initCel	---> first live cell for the dictionaries' construction
		strtCel	---> first live cell of the running automaton.
		noCels	---> number of cells to live at least once
		"""
		#Initialization parameters.
		MkData.__init__(self, width, height, initCel)
		#Instantiate the automaton and its organizer.
		self.autmta		= aut.crearAutomata(self.size, self.initCel)
		self.autmtaOrg 	= aut.organizadorAutomata(self.autmta)


	def iterAutmta(self):
		""" Iterate the automaton.
		"""
		self.autmtaOrg.iterateAutomaton()


	def getLiveClls(self):
		""" Return the current live cells.
		"""
		liveCells = []
		for x in range(self.width):			for y in range(self.height):
				onOff = self.autmta.get((x, y))
				if onOff:
					liveCells.append((x, y))
		return liveCells


	def mkHarmDict(self, fundCll, noPrtls):
		"""
		"""
		coordIndx	= []
		indx		= 0
		valEven		= 0
		valOdd		= 1

		for x in xrange(noPrtls):
			if float(indx) % 2 or not indx:
				newTuple = (str((fundCll[0], fundCll[1] + valEven)), indx)
				valEven += 1
			else:
				newTuple = (str((fundCll[0], fundCll[1] - valOdd)), indx)
				valOdd += 1
			coordIndx.append(newTuple)
			indx += 1
		coordIndxDict = dict(coordIndx)

		return coordIndxDict


	def mkVoxDict(self, fundCll, noPrtls):
		"""
		"""
		coordVox	= []
		vox			= 1
		valEven		= 0
		valOdd		= 1

		for x in xrange(noPrtls):
			if float(vox) % 2 or not vox:
				newTuple = (str((fundCll[0], fundCll[1] + valEven)), vox * .01)
				valEven += 1
			else:
				newTuple = (str((fundCll[0], fundCll[1] - valOdd)), vox * .01)
				valOdd += 1
			coordVox.append(newTuple)
			vox += 1
		coordVoxDict = dict(coordVox)

		return coordVoxDict
