## Class module to make a Csound .csd2 file.

import csnd

import csd2


class CsndData(object):
	""" Gathers all the data that Csound needs in order to make a
	performance.
	"""
	def __init__(self, scoLst):
		"""	Holds the necessary data for Csound to make a performance.
		Csound options, Csound orchestra (header and instruments) and
		initial score statements should be edited in csd2.py.
		opts	---> Csound performance options as a string
		orc		---> A Csound orchestra as a string
		scoLst	---> Csound score definitions as a list of strings
		"""
		self.opts	= csd2.opts
		self.orc	= csd2.orc
		self.funcs	= csd2.funcs
		self.scoLst	= scoLst
		self.sco	= self.mkSco()


	def mkSco(self):
		""" Takes a string of function statements, and a list of
		strings representing note statements. Constructs a score
		string. 
		"""
		scoStr = '\n'.join(self.scoLst)

		sco = """%s%s""" %(self.funcs, scoStr)
		return sco


class CsndCtrl(object):
	"""Contains the methods to communicate with Csound.
	"""	
	def __init__(self, scoLst):
		"""Initializes Csound with the Csound options, orchestra and
		score inherited from Csnd_data."""
		Data = CsndData(scoLst)
		# instantiate csound
		self.csound = csnd.CppSound()

		self.csound.setPythonMessageCallback()
		self.csound.setCommand(Data.opts)
		self.csound.setOrchestra(Data.orc)
		self.csound.setScore(Data.sco)

	def render(self):
		"""Renders the score, producing an audio archive."""
		self.csound.exportForPerformance()
		self.csound.perform()
		self.csound.removeScore()

if __name__ == "__main__":
	inst = Csnd_Ctrl(['1 2 3', '213','2 2 2'])
	inst.render()
