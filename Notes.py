## Class module for note score statements.

import Envelopes

import Note_methods


class Note(object):
	"""	Super class to construct a Csound note statements.
	"""
	def __init__(self, instrNo, strt, dur):
		"""	Minimum attributes that a Csound score statement may have.
		instrNo	---> an instrument number
		strt	---> as start time (in seconds)
		dur		---> a duration (in seconds)
		"""
		self.instrNo 		= 'i%s' %(instrNo)
		self.strt			= strt
		self.dur			= dur
		self.allAttributes	= [self.instrNo, self.strt, self.dur]	


	def scoLine(self):
		"""	The most basic score statement: instrument number,
		start time and duration.
		return	--> An 'instr strt dur' string
		"""
		formatList	= '%-8s '*len(self.allAttributes)
		pfields = formatList %tuple(self.allAttributes)
		return pfields


class AmpFreq(Note):
	"""	Construct a note statement with amplitude and frequency as p4
	and p5, respectively
	"""
	def __init__(self, instrNo, strt, dur, amp, freq):
		""" Initializes the attributes. instrNo, strt and dur are
		inherited
		instrNo	---> an instrument number
		strt	---> as start time (in seconds)
		dur		---> a duration (in seconds)
		amp		---> an amplitude
		freq	---> a frequency
		"""
		Note.__init__(self, instrNo, strt, dur)
		self.amp	= amp
		self.freq	= freq
		self.allAttributes	= [self.instrNo, self.strt, self.dur, self.amp,
								self.freq]


	scoLine = Note.scoLine


class withAmpEnv(Note):
	"""	Construct a note statement with amplitude and frequency as p4
	and p5, respectively
	"""
	def __init__(self, instrNo, strt, dur, freq, durValPairs):
		""" Initializes the attributes. instrNo, strt and dur are
		inherited.
		instrNo		---> an instrument number
		strt		---> as start time (in seconds)
		dur			---> a duration (in seconds)
		freq		---> a frequency
		durValPairs	---> list of tuples representing dur-val pairs
		"""
		Note.__init__(self, instrNo, strt, dur)
		self.freq	= freq

		self.Envelope = Envelopes.LnAmpEnvlp(durValPairs)
		self.durValList = Envelopes.LnAmpEnvlp.durValList(self.Envelope)
		self.allAttributes	= [self.instrNo, self.strt, self.dur,
								self.freq]
		self.allAttributes.extend(self.durValList)


	scoLine = Note.scoLine


class NoteInstr1(Note):
	"""	Construct a note statement with amplitude and frequency as p4
	and p5, respectively.
	"""
	def __init__(self, instr):
		""" Initializes the attributes. instrNo, strt and dur are
		inherited.
		instrNo		---> an instrument number
		strt		---> as start time (in seconds)
		dur			---> a duration (in seconds)
		freq		---> a frequency
		durValPairs	---> list of tuples representing dur-val pairs
		"""
		self.instr			= instr
		self.vox			= 0.0
		self.strt			= 0
		self.dur			= -1
		self.ampPts			= [-96, (0,-96)]
		self.frecPts		= [0.001, (0,0.001)]
		self.formEnv		= [(0,0)] * 5
		self.allAttributes	= self.mkAttributes()



	def mkEnvelope(self, points):
		""" Convert a list of 2-tuples (dur, val) into a plain list. If
		the list is shorter than what i4 needs, the list is extended
		with zeros. If it is too long, it is truncated.
		points	---> a list of 2-tuples
		return	--> a plain list
		"""
		val1	= points.pop(0)

		while len(points) > len(self.formEnv):
			points.pop()
			print 'Warning: removing points from envelope'
		while len(points) < len(self.formEnv):
			if val1 < 0:
				points.append((0, -96))
			if val1 >= 0:
				points.append((0, .001))


		self.Envelope = Envelopes.LnAmpEnvlp(points)
		durValList = Envelopes.LnAmpEnvlp.durValList(self.Envelope)
		durValList.insert(0, val1)
		return durValList


	def mkAttributes(self):
		""" Make updated atributes. Use this function to update all
		attributes. Run this before sco.Line!!!
		"""
		self.instrNo	= 'i' + str(self.instr + self.vox)
		self.amps	= self.mkEnvelope(self.ampPts)
		self.frecs	= self.mkEnvelope(self.frecPts)
		allAttributes = [self.instrNo, self.strt, self.dur]
		allAttributes.extend(self.amps)
		allAttributes.extend(self.frecs)
		return allAttributes


	scoLine = Note.scoLine
