## Process classes.

import random
import operator

import Data_aut as DataAut
import Note_methods as NoteMethods
import Numeric_utils as NumericUtils
import Notes
import nomenclature_dicts as nomencalutreDicts

Temper		= NoteMethods.EqTmpr(47)
Scaling		= NumericUtils.Scaling()
dinmcDict	= nomencalutreDicts.mkDin()
Series		= NumericUtils.Series(0)
Interpol	= NumericUtils.Interpol()
Spctrm		= NoteMethods.Spctrm()

Autmt	= DataAut.CtrlAutmt(113, 49, (0,0))

class OneVoice(object):
	"""
	"""
	def __init__(self, centre=(56,13), instrt= 1, spectrm=0):
		"""
		"""
		# Dont change.
		self.dur		= 0
		self.strt		= 0
		self.strtNxt	= 0
		self.walk		= []
		self.centre		= centre
		self.instrt		= instrt
		self.spectrm	= spectrm
		self.gaussMean	= 0.090145152
		self.strtchFact	= 1
		self.rythmAtms	= [1, 2, 3, 5, 7, 8]
		self.ampModify	= 0
		self.strtTms	= NoteMethods.StrtTms(self.rythmAtms, self.strtchFact)
		self.durMod		= 1
		# To set-up
		self.harmNo		= 2
		self.distrs		= [.01, .02]
		self.origin		= 211
		self.step		= 1

### Amplitude methods.

	def mkSpectBalance(self, amp):
		"""
		"""
		first = amp - self.harmNo
		bal	= [first]
		for x in xrange(self.harmNo): 
			amp = bal[-1] - 6
			bal.append(amp)
		return bal

	def mkdistsToGaussPeak(self):
		dists = []
		while len(dists) != self.harmNo:
			dist = random.gauss(self.durToNxt * 0.5,
								self.durToNxt * self.gaussMean)
			if dist < self.durToNxt and dist > 0.03:
				dists.append(dist)
		return dists


	def mkdistsToBetaPeak(self):
		dists = []
		while len(dists) != self.harmNo:
			dist = random.betavariate(self.alpha, self.beta)
			dist = Scaling.valToRng(dist, 0, 1, .015, self.durToNxt)
			dists.append(dist)
		return dists


	def mkdistsToUniformPeak(self):
		dists = []
		while len(dists) != self.harmNo:
			dist = random.uniform(0.15, self.durToNxt)
			dists.append(dist)
		return dists


	def mkAmpEnv(self, dist, amp):
		"""
		"""
		env1 = [-140, (dist, amp),
				(self.durToNxt - dist, -140)]

		env2 = [-140, (.01, amp),
				(dist - .01, amp -12),
				(self.durToNxt - dist - .01, -140)]

		env3 = [-140, ( .01, amp -12),
				(dist - .01, amp),
				(self.durToNxt - dist - .01, -140)]

		if self.instrt == 1:
			env = env1


		elif self.instrt == 2:
			env = env2

		elif self.instrt == 3:
			env = env3

#		elif self.instrt == 4:
#			env = env4

#		elif self.instrt == 5:
#			env = env5

		else:
			env = random.choice([env1, env2, env3,])

		return env

		
### Frequency methods.

	def mkFreqEnvlp(self):
		"""
		"""
		while len(self.spctrm1) > len(self.spctrm2):
			self.spctrm1.pop()
		while len(self.spctrm1) < len(self.spctrm2):
			self.spctrm2.pop()

		freqEnvls	= []
		for val1, val2 in zip(self.spctrm1, self.spctrm2):
			oneEnv	= [val1, (self.durToNxt, val2)]
			freqEnvls.append(oneEnv)
		return freqEnvls

### Fundamental Methods:

	def mkWalk(self):

		newDists	= [self.origin]
		newPitches	= []
		newStep		= self.step
		accum		= self.origin
		counter		= 0

		if self.step > 0:
			for x in xrange(len(self.rythmAtms)):
				if counter % 2 == 0:
					accum += self.step
				else:
					accum -= self.step
				newDists.append(accum)
				self.step += 1
				counter += 1
		if self.step < 0:
			for x in xrange(len(self.rythmAtms)):
				if counter % 2 == 0:
					accum -= abs(self.step)
				else:
					accum += abs(self.step)
				newDists.append(accum)
				self.step -= 1
				counter += 1
		for x in newDists:
			pitchPrts = divmod(x, 47)
			if pitchPrts[1] < 10:
				pitch	= ''.join([str(pitchPrts[0]), '.0', str(pitchPrts[1])])
			else:
				pitch	= ''.join([str(pitchPrts[0]), '.', str(pitchPrts[1])])
			newPitches.append(pitch)
		return newPitches

### New Note Methods.

	def updateConfig(self):
		"""
		"""
		self.srtsMemo	= []
		self.cllVoxDict	= Autmt.mkVoxDict(self.centre, self.harmNo)
		self.pitchDict	= Temper.modNDict()
		self.prtls		= Spctrm.mkPartls(self.spectrm, self.harmNo)
		self.NoteInstr1	= Notes.NoteInstr1(self.instrt)
		if self.gaussMean < .618:
			self.gaussMean /= .618


	def updateStrtDur(self):
		"""
		"""
		self.strt		= self.strtNxt
		if self.strtNxt - self.strt > 5:
			self.shrink = .8
		else:
			self.shrink = 1
		self.dur		= self.strtTms.inPlaceRotation() * self.durMod
		self.durToNxt	= self.dur  * self.shrink
		self.strtNxt	= self.strt	+ self.dur

		if not len(self.walk):
			self.walk		= self.mkWalk()
			self.newPitch	= self.walk.pop(0)
#			self.walkStrt	= tuple(self.newPitch)
			self.fundFreq1		= self.pitchDict[self.newPitch]
			self.fundFreq2		= self.pitchDict[self.newPitch]
		else:
			self.oldPitch	= self.newPitch
			self.newPitch	= self.walk.pop(0)
			pitches = [float(self.oldPitch), float(self.newPitch)]
			pitches.sort()

			if pitches[1] - pitches[0] < 7:
				self.fundFreq2		= self.pitchDict[self.oldPitch]
				self.fundFreq1		= self.pitchDict[self.newPitch]

			elif abs (self.walkStrt - self.newPitch) < 7:
				coinToss = random.randint(0, 1)
				if coinToss:
					self.fundFreq2		= self.pitchDict[self.walk[0]]
					self.fundFreq1		= self.pitchDict[self.newPitch]
				elif not coinToss:
					self.fundFreq2		= self.pitchDict[self.newPitch]
					self.fundFreq1		= self.pitchDict[self.walk[0]]

			else:
				self.fundFreq2		= self.pitchDict[self.newPitch]
				self.fundFreq1		= self.pitchDict[self.newPitch]



		random.shuffle(self.distrs)
		self.spctrm1	= Spctrm.dSpect(self.fundFreq1, self.prtls,
										self.distrs[0])
		self.spctrm2	= Spctrm.dSpect(self.fundFreq2, self.prtls,
										self.distrs[1])
		self.freqEnvlp		= self.mkFreqEnvlp()
		self.amps			= self.mkSpectBalance(-20 + self.ampModify)
		self.diststoPeak	= self.mkdistsToGaussPeak()


	def mkNote(self):
		"""
		"""
		self.updateStrtDur()

		notes	= []
		vox		= 1

		for freqEnv, amp, dist in zip(self.freqEnvlp, self.amps, self.diststoPeak):

			self.NoteInstr1.vox				= vox * .01
			self.NoteInstr1.strt			= self.strt
			self.NoteInstr1.dur				= self.durToNxt
			self.NoteInstr1.ampPts			= self.mkAmpEnv(dist, amp)
			self.NoteInstr1.frecPts			= freqEnv
			self.NoteInstr1.allAttributes	= self.NoteInstr1.mkAttributes()
			
			oneNote	= self.NoteInstr1.scoLine()
			notes.append(oneNote)

			vox += 1
		self.srtsMemo.append(self.strt)

		return notes



	def updateStrtDur2(self):
		"""
		"""
		self.strt		= self.strtNxt
		self.dur		= self.durMod
		if self.dur < .05:
			self.dur = .05
		self.durToNxt	= self.dur
		self.strtNxt	= self.strt	+ self.dur

		pitchPrts = divmod(self.origin, 47)
		if pitchPrts[1] < 10:
			self.newPitch	= ''.join([str(pitchPrts[0]), '.0',
										str(pitchPrts[1])])
		else:
			self.newPitch	= ''.join([str(pitchPrts[0]), '.',
										str(pitchPrts[1])])

		self.fundFreq1		= self.pitchDict[self.newPitch]
		self.fundFreq2		= self.pitchDict[self.newPitch]

		random.shuffle(self.distrs)
		self.spctrm1	= Spctrm.dSpect(self.fundFreq1, self.prtls,
										self.distrs[0])
		self.spctrm2	= Spctrm.dSpect(self.fundFreq2, self.prtls,
										self.distrs[1])
		self.freqEnvlp		= self.mkFreqEnvlp()
		self.amps			= self.mkSpectBalance(-20 + self.ampModify)
		self.diststoPeak	= self.mkdistsToGaussPeak()


	def mkNote2(self):
		"""
		"""
		self.updateStrtDur2()

		notes	= []
		vox		= 1

		for freqEnv, amp, dist in zip(self.freqEnvlp, self.amps, self.diststoPeak):

			self.NoteInstr1.vox				= vox * .01
			self.NoteInstr1.strt			= self.strt
			self.NoteInstr1.dur				= self.durToNxt
			self.NoteInstr1.ampPts			= [-140,
												(.02, amp),
												(self.durToNxt - .02, -140)]
			self.NoteInstr1.frecPts			= freqEnv
			self.NoteInstr1.allAttributes	= self.NoteInstr1.mkAttributes()
			
			oneNote	= self.NoteInstr1.scoLine()
			notes.append(oneNote)

			vox += 1
		self.srtsMemo.append(self.strt)

		return notes
		
