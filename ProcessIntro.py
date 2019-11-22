## Process classes.

import random
import operator

import Data_aut as DataAut
import Note_methods as NoteMethods
import Numeric_utils as NumericUtils
import Notes
import nomenclature_dicts as nomencalutreDicts

Temper		= NoteMethods.EqTmpr(47)
Spctrm		= NoteMethods.Spctrm()
Scaling		= NumericUtils.Scaling()
dinmcDict	= nomencalutreDicts.mkDin()
Series		= NumericUtils.Series(0)
Interpol	= NumericUtils.Interpol()

class Process1(object):
	"""
	"""
	def __init__(self, initCll=(56, 24),
					strtCll=(0, 0),
					pitch1='0.00',
					distr1=.618,
					pitch2='0.00',
					distr2=.618,
					offset=0,
					instrt=1):
		"""
		"""
		# Automaton data creation
		self.noPrtls		= 996
		self.Autmt			= DataAut.RunAutmta(113, 49, initCll, strtCll,
												self.noPrtls)
		self.cllIndxDict	= self.Autmt.cllIndxDict
		self.coordVoxDict	= self.Autmt.coordVoxDict
		self.initHist		= self.Autmt.initHist
		self.ampHistDict	= self.mkEmptyDict()
		self.ampCtrlDict	= self.mkEmptyDict()
		self.iters			= self.itersToMaxAmp()
		# Start-times.
		self.offset		= offset
		self.rythmAtms	= [2, 3, .25, 5, 0.166666667, 7, 0.125, .1111, 0.1,
							11, .0833, 13]
		self.StrtTms	= NoteMethods.StrtTms(self.rythmAtms, 0.1)
		self.strtsLin	= self.mkStrtsLin()
		self.logPulse	= Series.logar(1, len(self.iters) + 1)
		self.strtsLog	= self.mkStrtsLog()
		self.strts		= self.strtsLog
		# Durations
		self.Durs		= NoteMethods.Durs()
		self.durs		= self.mkDurs()
		self.strts.pop()
		self.durs.pop(0)
		self.durs[-1]	= 2.6
		self.totDur		= self.strts[-1] + self.durs[-1]
		# Amplitude Envelopes
		self.rawAmpPeaks	= self.mkAmpPeaks()
		self.ampDists		= self.mkDistsToPeak()
		self.ampDists2		= self.mkDistsToEnd()
		self.ampPeaks		= self.scaleAmps()
		# Frequency Enelope
		self.pitchDict	= Temper.modNDict()
		self.fundFreq1	= self.pitchDict[pitch1]
		self.distr1		= distr1
		self.distr2		= distr2
		self.fundFreq2	= self.pitchDict[pitch2]
		self.ordrdFreq	= self.orderFreqs()
		self.spctrm1	= Spctrm.dSpect(self.fundFreq1, self.ordrdFreq,
										self.distr1)
		self.spctrm2	= Spctrm.dSpect(self.fundFreq2, self.ordrdFreq,
										self.distr2)

		self.freqEnvlp	= self.mkFreqEnvlp()
		# Ordered instrument decimals
		self.NoteInstr1		= Notes.NoteInstr1(instrt)
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
			empyDict[x]	= [-36]
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
					if self.ampCtrlDict.has_key(str(x)):
						if lst[-1] == -20:
							del self.ampCtrlDict[str(x)]
							lst.append(-21)
						else:
							if len(lst):
								lst.append(lst[-1] + 1)
					else:
						if len(lst):
							if lst.count(-20) == lst.count(-36):
								newVal = lst[-1] - 1
							else:
								newVal = lst[-1] + 1
							lst.append(newVal)
					

					self.ampHistDict[str(x)] = lst
					validClls.append(x)
			if len(validClls):
				iters.append(validClls)
			self.Autmt.iterAutmta()
		return iters

#### Start-time methods.

	def mkStrtsLin(self):
		"""
		"""
		strts = [self.StrtTms.nxtValASP()]

		for x in self.iters:
			strt = self.StrtTms.nxtValASP()
			if strt > 30:
				break
			strts.append(strt + 1)
		while len(self.iters) > len(strts) - 1:
			self.iters.pop()		
		return strts


	def mkStrtsLog(self):
		"""
		"""
		strtsLog = []

		for x, y in zip(self.strtsLin, self.logPulse):
			strtLog = (x * y) + random.gauss(0, .005) + 1
			strtsLog.append(strtLog + self.offset)
		return strtsLog

#### Duration methods.

	def mkDurs(self):
		"""
		"""
		durs	= []

		for x in self.strts:
			dur = self.Durs.fullDur(x)
			if dur:
				durs.append(dur)
		return durs

#### Amplitude Envelope methods.

	def mkAmpPeaks(self):
		"""
		"""
		rawAmpPeaks = []

		for cllLst in self.iters:
			oneIterAmps = []
			for oneCll in cllLst:
				ampsCell = self.ampHistDict[str(oneCll)]
				amp = ampsCell.pop(0)
				self.ampHistDict[str(oneCll)] = ampsCell
				oneIterAmps.append(amp)

			rawAmpPeaks.append(oneIterAmps)
		return rawAmpPeaks


	def mkDistsToPeak(self):
		"""
		"""
		dists 		= []
		Series		= NumericUtils.Series(0)

		for dur, peakLst in zip(self.durs, self.rawAmpPeaks):
			hiAmp = -36
			oneIterDists = []
			for amp in peakLst:
				if amp > hiAmp:
					hiAmp = amp
				if hiAmp == -20:
					hiAmp = allAmps[-1]
			allAmps		= range (-36, hiAmp + 1, 1)
			subDiv = allAmps.index(hiAmp) + 1
			for peak in peakLst:
				if peak == allAmps[-1]:
					oneDist = random.uniform(0.001, dur)
				else:
					reltvPeak = random.randint(1, subDiv)
					oneDist = dur / float(reltvPeak)
				oneIterDists.append(oneDist)
			dists.append(oneIterDists)
		return dists


	def mkDistsToEnd(self):
		"""
		"""
		dists 	= []

		for dur, ampDists in zip(self.durs, self.ampDists):
			oneIterDists = []
			for oneDist in ampDists:
				oneDist2 = dur - oneDist
				oneIterDists.append(oneDist2)
			dists.append(oneIterDists)
		return dists


	def scaleAmps(self):
		"""
		"""
		ampPeaks	= []

		for x in self.rawAmpPeaks:
			scaledAmps = Scaling.lstToTotl(x, dinmcDict['mf'])
			ampPeaks.append(scaledAmps)
		return ampPeaks


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
			oneEnv	= [val1, (self.totDur, val2)]
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
			self.NoteInstr1.vox				= vox
			self.NoteInstr1.strt			= self.offset
			self.NoteInstr1.dur				= (self.totDur + 1) * -1
			self.NoteInstr1.ampPts			= [-96, (0, -96)]
			self.NoteInstr1.frecPts			= freqEnvlp
			self.NoteInstr1.allAttributes	= self.NoteInstr1.mkAttributes()
			
			oneNote	= self.NoteInstr1.scoLine()
			notes.append(oneNote)
		return notes


	def mKPrtlStmnts(self):
		"""
		"""
		iters = []

#		for x in self.iters:
#			iters.append(x)

		prtlStmnts	= []

		for oneIter, strt, dur, ampDists, ampPeaks, ampDists2 in zip(self.iters, self.strts, self.durs, self.ampDists, self.ampPeaks,
	self.ampDists2):

			for cll, ampDist, ampPeak, ampDist2 in zip(oneIter, ampDists,
														ampPeaks, ampDists2):
				self.NoteInstr1.vox				= self.coordVoxDict[str(cll)]

				self.NoteInstr1.strt		= strt

				self.NoteInstr1.dur		= dur * -1

				self.NoteInstr1.ampPts	= [-960, (ampDist, ampPeak), (ampDist2,
											-960)]
				self.NoteInstr1.frecPts	= [.001, (0, .001)]

				self.NoteInstr1.allAttributes = self.NoteInstr1.mkAttributes()
				oneNote	= self.NoteInstr1.scoLine()
				prtlStmnts.append(oneNote)

		return prtlStmnts


	def mkSco(self):
		"""
		"""
		#sco	= self.silentSpec + ['a 0 1 67'] + self.prtlsStmnts
		sco	= self.silentSpec + self.prtlsStmnts
		return sco
