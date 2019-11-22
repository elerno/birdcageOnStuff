## Holds the Csound options, orchestra and (initial) functions.

import time


opts		= 'csound -o %sBirdCageExtrapolation.wav -W -N -Z -d -R -t0 temp.orc temp.sco' %(time.strftime('%d-%m_%H.%M'))


orchHead	= """
sr		= 44100	; sample rate
kr		= 4410	; control rate
ksmps	= 10	; sr/kr
nchnls	= 1	; # of channels
0dbfs	= 1.0


"""


instr1		= """

    instr 1

idur		= abs(p3)
ivalamp1	= p4
iduramp1	= p5
ivalamp2	= p6
iduramp2	= p7
ivalamp3	= p8
iduramp3	= p9
ivalamp4	= p10
iduramp4	= p11
ivalamp5	= p12
iduramp5	= p13
ivalamp6	= p14
ivalfreq1	= p15
idurfreq1	= p16
ivalfreq2	= p17
idurfreq2	= p18
ivalfreq3	= p19
idurfreq3	= p20
ivalfreq4	= p21
idurfreq4	= p22
ivalfreq5	= p23
idurfreq5	= p24
ivalfreq6	= p25

ir		tival
i1	= -1
	tigoto ampenv
i1		= 0

ampenv:
if ir == 0 kgoto freqenv

kampenvti	linseg ivalamp1, iduramp1, ivalamp2, iduramp2, ivalamp3, iduramp3, ivalamp4, iduramp4, ivalamp5, iduramp5, ivalamp6


freqenv:
	tigoto oscilator
kfreqenv	expseg ivalfreq1, 1, ivalfreq1, idurfreq1, ivalfreq2, idurfreq2, ivalfreq3, idurfreq3, ivalfreq4, idurfreq4, ivalfreq5, idurfreq5, ivalfreq6
oscilator:
kampenvti = 0
kampenv	expseg ivalamp1, iduramp1, ivalamp2, iduramp2, ivalamp3, iduramp3, ivalamp4, iduramp4, ivalamp5, iduramp5, ivalamp6
asig	oscili 1, kfreqenv, 1, i1
    out asig * ampdbfs(kampenv + kampenvti)
    endin
"""



funcs ="""
f1 0 16384 10 1

"""

def mkInstrClones(instr1, noCopies):
	"""Constructs a series of instrument clones based on an
	instrument definition, assigning a different control channel to
	each instrument.
	return	--> a string of cloned instruments
	"""
	instrString	= instr1
	instrNo		= 2

	for x in xrange(noCopies):
		nInstrNo = ''.join(['instr ', str(instrNo)])
		newInstr = instr1.replace('instr 1', nInstrNo)
		instrString = instrString + newInstr
		instrNo += 1
	return instrString


def mkOrc(orchHead, instr1, noCopies):
	"""Uses the header and instrument
	instantiation method to construct the orchestra.
	return	--> an orchestra string
	"""
	instr2Clones	= mkInstrClones(instr1, noCopies)

	orc = '%s%s' %(orchHead, instr2Clones)
	return orc

orc	= mkOrc(orchHead, instr1, 51)
