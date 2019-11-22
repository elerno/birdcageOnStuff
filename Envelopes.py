## Class module for envelopes.


class LnEnvlp(object):
	"""	Class to construct p-field based envelopes. For amplitude
	envelopes, use LnAmpEnvlp.
	"""
	def __init__(self, val1, durValPairs):
		"""	Envelope attributes.
		val1		--->  initial value
		durValPairs	---> list of tuples representing dur-val pairs
		"""

		self.durValList	= [str(val1)]

		for x in durValPairs:
			dur, val = x[0], x[-1]
			self.durValList.append(str(dur))
			self.durValList.append(str(val))


	def envPoints(self):
		"""	A p-field line statement: initial value, duration until
		next value, next value (optional: duration until next value,
		next value, duration until next value, next value).
		return	--> A p-field line definition string
		"""
		formatString = '%-8s '*len(self.durValList)
		pfields = formatString %tuple(self.durValList)
		return pfields


class LnAmpEnvlp(LnEnvlp):
	"""	Class to construct p-field based envelopes for amplitude. The
	difference with general purpose envelopes is that the initial value
	is hard-coded in the Csound Orchestra (0 for linseg and .001 for
	expseg). 
	"""
	def __init__(self, durValPairs):
		"""	Envelope attributes.
		valA		--->  initial value
		durValPairs	---> list of tuples representing dur-val pairs
		"""
		self.durValList	= []

		for x in durValPairs:
			dur, val = x[0], x[-1]
			self.durValList.append(str(dur))
			self.durValList.append(str(val))


	envAmpPoints = LnEnvlp.envPoints


	def durValList(self):
		""" Returns a series of duration to the next point, next point.
		The first point has to be hard wiered in the Csound orc.
		return	--> a duration, value, duration, value... list
		"""
		return self.durValList
