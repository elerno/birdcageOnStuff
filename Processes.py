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
NoteInstr1	= Notes.NoteInstr1(1)
Scaling		= NumericUtils.Scaling()
dinmcDict	= nomencalutreDicts.mkDin()
Series		= NumericUtils.Series(0)
Interpol	= NumericUtils.Interpol()

class Process1(object):
	"""
	"""
	def __init__(self):
		"""
		"""
		# Automaton data creation
		self.noPrtls		= 996
		self.Autmt			= DataAut.RunAutmta(113, 49, (56, 24), (0, 0),
												self.noPrtls)
		self.cllIndxDict	= self.Autmt.cllIndxDict
		self.coordVoxDict	= self.Autmt.coordVoxDict
		self.initHist		= self.Autmt.initHist
		self.ampHistDict	= self.mkEmptyDict()
		self.ampCtrlDict	= self.mkEmptyDict()
		self.iters			= self.itersToMaxAmp()
		# Start-times.
		self.rythmAtms	= [2, 3, .25, 5, 0.166666667, 7, 0.125, .1111, 0.1,
							11, .0833, 13]
		self.StrtTms	= NoteMethods.StrtTms(self.rythmAtms, 0.1)
		self.strtsLin	= self.mkStrtsLin()
		self.logPulse	= Series.logar(1.5, len(self.iters) + 1)
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
		self.fundFreq	= self.pitchDict['0.00']
		self.ordrdFreq	= self.orderFreqs()
		self.spctrm1	= Spctrm.dSpect(self.fundFreq, self.ordrdFreq, 0.618)
		self.frecDist1	= self.totDur * .382
		self.spctrm2	= Spctrm.dSpect(self.fundFreq, self.ordrdFreq, 0.618)
		self.frecDist2	= (self.totDur * .618) - self.frecDist1
		self.spctrm3	= Spctrm.dSpect(self.fundFreq, self.ordrdFreq, 0.618)
		self.frecDist3	= self.totDur - (self.totDur * .618)
		self.spctrm4	= Spctrm.dSpect(self.fundFreq, self.ordrdFreq, 0.013)

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
						if lst[-1] == -25:
							del self.ampCtrlDict[str(x)]
							lst.append(-26)
						else:
							if len(lst):
								lst.append(lst[-1] + 1)
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
			strts.append(strt + 1)
		return strts


	def mkStrtsLog(self):
		"""
		"""
		strtsLog = []

		for x, y in zip(self.strtsLin, self.logPulse):
			strtLog = (x * y) + random.gauss(0, .005) + 1
			strtsLog.append(strtLog)
			if strtLog >= 60 and strtLog <120:
				self.StrtTms.spanSer = [2, 3, .25, 5, 0.166666667, 7,
										0.125, .1111, 0.1, 11, .0833,
										0.076923077]
			if strtLog >= 120 and strtLog <180:
				self.StrtTms.spanSer = [2, 3, .25, 5, 0.166666667, 7,
										0.125, .1111, 0.1, 0.090909091, .0833,
										0.076923077]
			if strtLog >= 180 and strtLog <210:
				self.StrtTms.spanSer = [2, 3, .25, 5, 0.166666667, 0.142857143,
										0.125, .1111, 0.1, 0.090909091, .0833,
										0.076923077]
			if strtLog >= 210 and strtLog <240:
				self.StrtTms.spanSer = [2, 3, .25, 0.2, 0.166666667,
										0.142857143, 0.125, .1111, 0.1,
										0.090909091, .0833, 0.076923077]
			if strtLog >= 240 and strtLog <270:
				self.StrtTms.spanSer = [2, 0.333333333, .25, 0.2, 0.166666667,
										0.142857143, 0.125, .1111, 0.1,
										0.090909091, .0833, 0.076923077]
			if strtLog >= 270 and strtLog < 300:
				self.StrtTms.spanSer = [0.5, 0.333333333, .25, 0.2,
										0.166666667, 0.142857143,
										0.125, .1111, 0.1, 0.090909091, .0833,
										0.076923077]

		return strtsLog


	def scalePrtsStrts(self):
		""" Not used
		"""
		mergedStrts	= self.strtsLog[0:142]
		toScaleLog	= self.strtsLog[142:]
		scaledPrt	= []
		for x in toScaleLog:
			scaled = Scaling.valToRng(x, toScaleLog[0], toScaleLog[-1],
										toScaleLog[0], 521)
			scaledPrt.append(scaled)
		mergedStrts.extend(scaledPrt)
		return mergedStrts


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
		allAmps		= range (-36, -19, 1)
		allAmps[-1]	= -1

		for dur, peakLst in zip(self.durs, self.rawAmpPeaks):
			hiAmp = -36
			oneIterDists = []
			for amp in peakLst:
				if amp > hiAmp:
					hiAmp = amp
				if hiAmp == -20:
					hiAmp = allAmps[-1]
			subDiv = allAmps.index(hiAmp) + 1
			for peak in peakLst:
				if peak == 1:
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
		for val1, val2, val3, val4 in zip(self.spctrm1, self.spctrm2,
											self.spctrm3, self.spctrm4):
			oneEnv	= [val1, (self.frecDist1, val2), (self.frecDist2, val3),
						(self.frecDist3, val4)]
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
			NoteInstr1.vox				= vox
			NoteInstr1.strt				= 0
			NoteInstr1.dur				= (self.totDur + 1) * -1
			NoteInstr1.ampPts			= [-96, (0, -96)]
			NoteInstr1.frecPts			= freqEnvlp
			NoteInstr1.allAttributes	= NoteInstr1.mkAttributes()
			
			oneNote	= NoteInstr1.scoLine()
			notes.append(oneNote)
		return notes


	def mKPrtlStmnts(self):
		"""
		"""
		iters = []

		for x in self.iters:
			iters.append(x)

		prtlStmnts	= []

		for oneIter, strt, dur, ampDists, ampPeaks, ampDists2 in zip(self.iters, self.strts, self.durs, self.ampDists, self.ampPeaks,
	self.ampDists2):

			for cll, ampDist, ampPeak, ampDist2 in zip(oneIter, ampDists,
														ampPeaks, ampDists2):
				NoteInstr1.vox				= self.coordVoxDict[str(cll)]

				NoteInstr1.strt		= strt

				NoteInstr1.dur		= dur * -1

				NoteInstr1.ampPts	= [-190, (ampDist, ampPeak), (ampDist2,
											-190)]
				NoteInstr1.frecPts	= [.001, (0, .001)]

				NoteInstr1.allAttributes	= NoteInstr1.mkAttributes()
				oneNote	= NoteInstr1.scoLine()
				prtlStmnts.append(oneNote)

		return prtlStmnts


	def mkSco(self):
		"""
		"""
		#sco	= self.silentSpec + ['a 0 1 67'] + self.prtlsStmnts
		sco	= self.silentSpec + self.prtlsStmnts
		return sco



def durModify(strt):
	
	mod = 1
	if strt >= 29 and strt < 38.4:
		mod = random.uniform(0.9, 1)
	if strt >= 38.4 and strt < 47.8:
		mod = random.uniform(0.8, 1)
	if strt >= 47.8 and strt < 57.2:
		mod = random.uniform(0.7, 1)
	if strt >= 57.2 and strt < 66.6:
		mod = random.uniform(0.6, 1)
	if strt >= 66.6 and strt < 76:
		mod = random.uniform(0.5, 1)
	if strt >= 76 and strt < 85.4:
		mod = random.uniform(0.4, .9)
	if strt >= 85.4 and strt < 94.8:
		mod = random.uniform(0.3, .8)
	if strt >= 94.8 and strt < 104.2:
		mod = random.uniform(0.2, .7)
	if strt >= 104.2 and strt < 113.6:
		mod = random.uniform(0.3, .6)
	if strt >= 113.6 and strt < 104.2:
		mod = random.uniform(0.2, 0.5)
	if strt >= 123 and strt < 130:
		mod = random.uniform(0.1, 0.4)
	if strt >= 130 and strt < 140:
		mod = random.uniform(0.2, 0.5)
	if strt >= 140 and strt < 150:
		mod = random.uniform(0.3, 0.6)
	if strt >= 150 and strt < 160:
		mod = random.uniform(0.4, 0.7)
	if strt >= 160 and strt < 170:
		mod = random.uniform(0.5, 0.8)
	if strt >= 170 and strt < 180:
		mod = random.uniform(0.6, 0.9)
	if strt >= 180 and strt < 190:
		mod = random.uniform(0.7, 1)
	if strt >= 190 and strt < 200:
		mod = random.uniform(0.9, 1)
	if strt >= 200:
		mod = 1

	return mod


def strtModify(strt):
	
	newStrt = strt
	oldIter = 0
	newIter = 1
	if strt >= 67 and strt < 85:
		newstrt = strt + random.betavariate(1, 3)

	if strt >= 85 and strt < 104:
		distribs = random.choice([random.betavariate(1,
					3)] * 1 + [random.betavariate(2, 5)] * 2)
		newstrt = strt + distribs
		newStrt = Scaling.valToRng(newStrt, 0, 1, 0, 1.5)

	if strt >= 104 and strt < 123:
		distribs = random.choice([random.betavariate(1,
									3)] * 1 + [random.betavariate(2,
									5)] * 2 + [random.betavariate(5, 5)] * 3)
		newstrt = strt + distribs
		scaleRng = random.choice([(0, 1.5)] * 1 + [(0, 2)] * 2)
		newStrt = Scaling.valToRng(newStrt, 0, 1, scaleRng[0], scaleRng[1])

	if strt >= 123 and strt < 156:
		distribs = random.choice([random.betavariate(1,
									3)] * 1 + [random.betavariate(2,
									5)] * 2 + [random.betavariate(5,
									5)] * 3 + [random.betavariate(.5, .5)] * 4)
		newstrt = strt + distribs
		scaleRng = random.choice([(0, 1.5)] * 1 + [(0, 2)] * 2 + [(0,
									2.5)] * 3)
		newStrt = Scaling.valToRng(newStrt, 0, 1, scaleRng[0], scaleRng[1])

	if strt >= 156 and strt < 174:
		distribs = random.choice([random.betavariate(2,
									5)] * 1 + [random.betavariate(5,
									5)] * 2 + [random.betavariate(.5, .5)] * 4)
		newstrt = strt + distribs
		scaleRng = random.choice([(0, 1.5)] * 1 + [(0, 2)] * 2 + [(0,
									2.5)] * 3 + [(0, 2.9)] * 4)
		newStrt = Scaling.valToRng(newStrt, 0, 1, scaleRng[0], scaleRng[1])

	if strt >= 174 and strt < 185:
		distribs = random.choice([random.betavariate(5,
									5)] * 1 + [random.betavariate(.5, .5)] * 4)
		newstrt = strt + distribs
		scaleRng = random.choice([(0, 2)] * 1 + [(0, 2.5)] * 2 + [(0,
									2.9)] * 3 + [(0, 1.8)] * 5)
		newStrt = Scaling.valToRng(newStrt, 0, 1, scaleRng[0], scaleRng[1])

	if strt >= 185 and strt < 192:
		newStrt = strt + random.betavariate(.5, .5)
		scaleRng = random.choice([(0, 2.5)] * 1 + [(0, 2.9)] * 2 + [(0,
									1.8)] * 3 + [(0, 1.1)] * 6)
		newStrt = Scaling.valToRng(newStrt, 0, 1, scaleRng[0], scaleRng[1])

	if strt >= 192 and strt < 199:
		newStrt = strt + random.betavariate(.5, .5)
		scaleRng = random.choice([(0, 2.9)] * 1 + [(0, 1.8)] * 2 + [(0,
									1.1)] * 3 + [(0, .7)] * 7)
		newStrt = Scaling.valToRng(newStrt, 0, 1, scaleRng[0], scaleRng[1])

	if strt >= 196 and strt < 199:
		newStrt = strt + random.betavariate(.5, .5)
		scaleRng = random.choice([(0, 1.8)] * 1 + [(0, 1.1)] * 2 + [(0,
									.7)] * 3 + [(0, .4)] * 8)
		newStrt = Scaling.valToRng(newStrt, 0, 1, scaleRng[0], scaleRng[1])

	if strt >= 199:
		newStrt = strt + random.betavariate(.5, .5)
		scaleRng = random.choice([(0, 1.1)] * 1 + [(0, .7)] * 2 + [(0,
									.4)] * 3 + [(0, .1)] * 9)
		newStrt = Scaling.valToRng(newStrt, 0, 1, scaleRng[0], scaleRng[1])

	return newStrt	
