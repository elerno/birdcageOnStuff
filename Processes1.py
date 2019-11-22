## Process classes.

import random

import Data_aut as DataAut
import Note_methods as NoteMethods
import Numeric_utils as NumericUtils
import Notes

Temper		= NoteMethods.EqTmpr(47)
Spctrm		= NoteMethods.Spctrm()
NoteInstr4	= Notes.NoteInstr4()

class Process1(object):
	"""
	"""
	def __init__(self):
		"""
		"""
		# Automaton data creation
		self.noPrtls		= 1000
		self.Autmt			= DataAut.RunAutmta(114, 48, (56, 24), (0, 0),
												self.noPrtls)
		self.cllIndxDict	= self.Autmt.cllIndxDict
		self.coordVoxDict	= self.Autmt.coordVoxDict
		self.initHist		= self.Autmt.initHist
		self.ampHistDict	= self.mkEmptyDict()
		self.ampCtrlDict	= self.mkEmptyDict()
		self.iters			= self.itersToMaxAmp()
		# Start-times.
		self.StrtTms	= NoteMethods.StrtTms([2, 3, 5, 7], 0.53)
		self.strts		= self.mkStrts()
		# Durations
		self.Durs	= NoteMethods.Durs()
		self.durs	= self.mkDurs()
		self.strts.pop()
		self.durs.pop(0)
		# Amplitude Envelopes
		self.ampPeaks	= self.mkAmpPeaks()
		self.ampDists	= self.mkDistsToPeak()
		self.ampDists2	= self.mkDistsToEnd()
		# Frequency Enelope
		self.pitchDict	= Temper.modNDict()
		self.fundFreq	= self.pitchDict['1.37']
		self.ordrdFreq	= self.orderFreqs()
		self.spctrm1	= Spctrm.dSpect(self.fundFreq,
													self.ordrdFreq, 0.13)
		self.frecDist	= self.strts[-1] + self.durs[-1]
		self.spctrm2	= Spctrm.dSpect(self.fundFreq,
													self.ordrdFreq, 0.01)
		self.freqEnvlp	= self.mkFreqEnvlp()
		# Ordered instrument decimals
		self.ordrdVox		= self.orderVox()
		# Make Csound instrument statements.
		self.silentSpec		= self.mkSilentSpec()
		self.prtlsStmnts	= self.mKPrtlStmnts()
		self.sco			= self.mkSco()

#### Automaton data creation methods

	def mkEmptyDict(self):
		"""
		"""
		empyDict	= {}

		for x in self.cllIndxDict.keys():
			empyDict[x]	= [1]
		return empyDict


	def itersToMaxAmp(self):
		""" 
		"""
		iters	= []

		while len(self.ampCtrlDict):
			oneIter		= self.Autmt.getLiveClls()
			validClls	= []

			for x in oneIter:
				if self.ampHistDict.has_key(str(x)):
					lst = self.ampHistDict[str(x)]

					if lst[-1] == 32768:
						lst[-1] = 32767
						del self.ampCtrlDict[str(x)]
						lst.append(32767)
					elif lst[-1] == 32767:
						lst.append(32767)
					else:
						if len(lst):
							lst.append((lst[-1] * 2))
					self.ampHistDict[str(x)] = lst
					validClls.append(x)
			if len(validClls):
				iters.append(validClls)
			self.Autmt.iterAutmta()
		return iters

#### Start-time methods.

	def mkStrts(self):
		"""
		"""
		strts = [self.StrtTms.nxtValASP()]

		for x in self.iters:
			strt = self.StrtTms.nxtValASP()
			strts.append(strt + 1)
		return strts

#### Duration methods.

	def mkDurs(self):
		"""
		"""
		durs	= []

		for x in self.strts:
			dur = self.Durs.fullDur(x)
			durs.append(dur)
		return durs

#### Amplitude Envelope methods.

	def mkAmpPeaks(self):
		"""
		"""
		ampPeaks = []

		for cllLst in self.iters:
			oneIterAmps = []
			for oneCll in cllLst:
				ampsCell = self.ampHistDict[str(oneCll)]
				amp = ampsCell.pop(0)
				self.ampHistDict[str(oneCll)] = ampsCell
				oneIterAmps.append(amp)

			ampPeaks.append(oneIterAmps)
		return ampPeaks


	def mkDistsToPeak(self):
		"""
		"""
		dists 	= []
		Series	= NumericUtils.Series(0)
		allAmps	= Series.geometr(2, 15)

		for dur, peakLst in zip(self.durs, self.ampPeaks):
			hiAmp = 1
			oneIterDists = []
			for amp in peakLst:
				if amp > hiAmp:
					hiAmp = amp
				if hiAmp == 32767:
					hiAmp = allAmps[-1]
			subDiv = allAmps.index(hiAmp) + 1
			for peak in peakLst:
				if peak == 32767:
					oneDist = random.uniform(0, dur)
				else:
					reltvPeak = ((allAmps.index(peak) + 1) / float(subDiv))
					oneDist = reltvPeak * dur
				oneIterDists.append(oneDist)
			dists.append(oneIterDists)
		return dists


	def mkDistsToEnd(self):
		"""
		"""
		dists 	= []
		Series	= NumericUtils.Series(0)
		allAmps	= Series.geometr(2, 15)

		for dur, ampDists in zip(self.durs, self.ampDists):
			oneIterDists = []
			for oneDist in ampDists:
				oneDist2 = dur - oneDist
				oneIterDists.append(oneDist2)
			dists.append(oneIterDists)
		return dists


#### Frequencies methods.

	def orderFreqs(self):
		"""
		"""
		ordrdFreq	= []
		for oneIter in self.iters:
			for cll in oneIter:
				freq = self.cllIndxDict[str(cll)]
				if ordrdFreq.count(self.cllIndxDict[str(cll)]) == 0:
					ordrdFreq.append(freq)
		return ordrdFreq


	def mkFreqEnvlp(self):
		"""
		"""
		freqEnvls	= []
		for val1, val2 in zip(self.spctrm1, self.spctrm2):
			oneEnv	= [val1, (self.frecDist, val2)]
			freqEnvls.append(oneEnv)
		return freqEnvls

#### Voices methods

	def orderVox(self):
		"""
		"""
		ordrdVox	= []
		for oneIter in self.iters:
			for cll in oneIter:
				vox = self.coordVoxDict[str(cll)]
				if ordrdVox.count(self.coordVoxDict[str(cll)]) == 0:
					ordrdVox.append(vox)
		return ordrdVox

#### Instrument statement methods

	def mkSilentSpec(self):
		"""
		"""
		notes	= []

		for vox, freqEnvlp in zip(self.ordrdVox, self.freqEnvlp):
			NoteInstr4.vox				= vox
			NoteInstr4.strt				= 0
			NoteInstr4.dur				= (self.frecDist + 1) * -1
			NoteInstr4.ampPts			= [0, (0, 0)]
			NoteInstr4.frecPts			= freqEnvlp
			NoteInstr4.allAttributes	= NoteInstr4.mkAttributes()
			
			oneNote	= NoteInstr4.scoLine()
			notes.append(oneNote)
		return notes


	def mKPrtlStmnts(self):
		"""
		"""
		iters = []

		for x in self.iters:
			iters.append(x)

		prtlStmnts	= []

		for oneIter, ampDists, ampPeaks, ampDists2 in zip(self.iters,
															self.ampDists,
															self.ampPeaks,
															self.ampDists2):
			for cll, strt, dur, ampDist, ampPeak, ampDist2 in zip(oneIter,
																self.strts,
																self.durs,
																ampDists,
																ampPeaks,
																ampDists2):
				NoteInstr4.vox				= self.coordVoxDict[str(cll)]
				NoteInstr4.strt				= strt + 1
				NoteInstr4.dur				= dur * -1
				NoteInstr4.ampPts			= [0, (ampDist, ampPeak * .01),
												(ampDist2, 0)]
				NoteInstr4.frecPts			= [0, (0, 0)]
				NoteInstr4.allAttributes	= NoteInstr4.mkAttributes()
				
				oneNote	= NoteInstr4.scoLine()
				prtlStmnts.append(oneNote)
		return prtlStmnts


	def mkSco(self):
		"""
		"""
		sco	= self.silentSpec + self.prtlsStmnts
		return sco
