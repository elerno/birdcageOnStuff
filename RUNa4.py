import random

import Csnd_interface2 as CsndInterface
import ProcessA4 as ProcessA

vTodos		= ProcessA.OneVoice(centre=(56,13), instrt= 1, spectrm=0)
vFibo		= ProcessA.OneVoice(centre=(56,13), instrt= 2, spectrm=3)
vNones		= ProcessA.OneVoice(centre=(56,13), instrt= 3, spectrm=1)
vPrimos		= ProcessA.OneVoice(centre=(56,13), instrt= 4, spectrm=4)
vPares		= ProcessA.OneVoice(centre=(56,13), instrt= 5, spectrm=2)

vTodos1		= ProcessA.OneVoice(centre=(56,13), instrt= 6, spectrm=0)
vFibo1		= ProcessA.OneVoice(centre=(56,13), instrt= 7, spectrm=3)
vNones1		= ProcessA.OneVoice(centre=(56,13), instrt= 8, spectrm=1)
vPrimos1	= ProcessA.OneVoice(centre=(56,13), instrt= 9, spectrm=4)
vPares1		= ProcessA.OneVoice(centre=(56,13), instrt= 10, spectrm=2)

vTodos2		= ProcessA.OneVoice(centre=(56,13), instrt= 11, spectrm=0)
vFibo2		= ProcessA.OneVoice(centre=(56,13), instrt= 12, spectrm=3)
vNones2		= ProcessA.OneVoice(centre=(56,13), instrt= 13, spectrm=1)
vPrimos2	= ProcessA.OneVoice(centre=(56,13), instrt= 14, spectrm=4)
vPares2		= ProcessA.OneVoice(centre=(56,13), instrt= 15, spectrm=2)

vTodos3		= ProcessA.OneVoice(centre=(56,13), instrt= 16, spectrm=0)
vFibo3		= ProcessA.OneVoice(centre=(56,13), instrt= 17, spectrm=3)
vNones3		= ProcessA.OneVoice(centre=(56,13), instrt= 18, spectrm=1)
vPrimos3	= ProcessA.OneVoice(centre=(56,13), instrt= 19, spectrm=4)
vPares3		= ProcessA.OneVoice(centre=(56,13), instrt= 20, spectrm=2)

vTodos4		= ProcessA.OneVoice(centre=(56,13), instrt= 21, spectrm=0)
vFibo4		= ProcessA.OneVoice(centre=(56,13), instrt= 22, spectrm=3)
vNones4		= ProcessA.OneVoice(centre=(56,13), instrt= 23, spectrm=1)
vPrimos4	= ProcessA.OneVoice(centre=(56,13), instrt= 24, spectrm=4)
vPares4		= ProcessA.OneVoice(centre=(56,13), instrt= 25, spectrm=2)

vTodos5		= ProcessA.OneVoice(centre=(56,13), instrt= 26, spectrm=0)
vFibo5		= ProcessA.OneVoice(centre=(56,13), instrt= 27, spectrm=3)
vNones5		= ProcessA.OneVoice(centre=(56,13), instrt= 28, spectrm=1)
vPrimos5	= ProcessA.OneVoice(centre=(56,13), instrt= 29, spectrm=4)
vPares5		= ProcessA.OneVoice(centre=(56,13), instrt= 30, spectrm=2)

vTodos6		= ProcessA.OneVoice(centre=(56,13), instrt= 31, spectrm=0)
vFibo6		= ProcessA.OneVoice(centre=(56,13), instrt= 32, spectrm=3)
vNones6		= ProcessA.OneVoice(centre=(56,13), instrt= 33, spectrm=1)
vPrimos6	= ProcessA.OneVoice(centre=(56,13), instrt= 34, spectrm=4)
vPares6		= ProcessA.OneVoice(centre=(56,13), instrt= 35, spectrm=2)

vTodos7		= ProcessA.OneVoice(centre=(56,13), instrt= 36, spectrm=0)
vFibo7		= ProcessA.OneVoice(centre=(56,13), instrt= 37, spectrm=3)
vNones7		= ProcessA.OneVoice(centre=(56,13), instrt= 38, spectrm=1)
vPrimos7	= ProcessA.OneVoice(centre=(56,13), instrt= 39, spectrm=4)
vPares7		= ProcessA.OneVoice(centre=(56,13), instrt= 40, spectrm=2)

vTodos8		= ProcessA.OneVoice(centre=(56,13), instrt= 41, spectrm=0)
vFibo8		= ProcessA.OneVoice(centre=(56,13), instrt= 42, spectrm=3)
vNones8		= ProcessA.OneVoice(centre=(56,13), instrt= 43, spectrm=1)
vPrimos8	= ProcessA.OneVoice(centre=(56,13), instrt= 44, spectrm=4)
vPares8		= ProcessA.OneVoice(centre=(56,13), instrt= 45, spectrm=2)

vTodos9		= ProcessA.OneVoice(centre=(56,13), instrt= 46, spectrm=0)
vFibo9		= ProcessA.OneVoice(centre=(56,13), instrt= 47, spectrm=3)



voiceLstInc = [vTodos,
			vFibo,
			vNones,
			vPrimos,
			vPares,
			vTodos1,
			vFibo1,
			vNones1,
			vPrimos1,
			vPares1,
			vTodos2,
			vFibo2,
			vNones2,
			vPrimos2,
			vPares2,
			vTodos3,
			vFibo3,
			vNones3,
			vPrimos3,
			vPares3,
			vTodos4,
			vFibo4,
			vNones4,
			vPrimos4,
			vPares4,
			vTodos5,
			vFibo5,
			vNones5,
			vPrimos5,
			vPares5,
			vFibo6,
			vPrimos6]


sco = []
tempo = 't 0 88 '






vFibo.harmNo		= 10
vFibo.distrs		= [.021, .034]
vFibo.durMod		= 1
vFibo.origin		= 164
vFibo.step			= 1

vPrimos.harmNo		= 10
vPrimos.distrs		= [.13, .17]
vPrimos.durMod		= .5
vPrimos.origin		= 140
vPrimos.step		= -1

vPares.harmNo		= 10
vPares.distrs		= [.1, .12]
vPares.durMod		= .333
vPares.origin		= 211
vPares.step			= 1

vNones.harmNo		= 10
vNones.distrs		= [.13, .15]
vNones.durMod		= .25
vNones.origin		= 235
vNones.step			= -1

vTodos.harmNo		= 10
vTodos.distrs		= [.12, .13]
vTodos.durMod		= .2
vTodos.origin		= 258
vTodos.step			= 1

vFibo.strtNxt = 0
vFibo.updateConfig()
for x in xrange(len(vFibo.rythmAtms) + 1):
	oneNote = vFibo.mkNote()
	sco.extend(oneNote)

vPrimos.strtNxt = vFibo.srtsMemo[-1]
vPrimos.updateConfig()
for x in xrange(len(vPrimos.rythmAtms) + 1):
	oneNote = vPrimos.mkNote()
	sco.extend(oneNote)

vPares.strtNxt = vPrimos.srtsMemo[-1]
vPares.updateConfig()
for x in xrange(len(vPares.rythmAtms) + 1):
	oneNote = vPares.mkNote()
	sco.extend(oneNote)

vNones.strtNxt = vPares.srtsMemo[-1]
vNones.updateConfig()
for x in xrange(len(vNones.rythmAtms) + 1):
	oneNote = vNones.mkNote()
	sco.extend(oneNote)

vTodos.strtNxt = vNones.srtsMemo[-1]
vTodos.updateConfig()
for x in xrange(len(vTodos.rythmAtms) + 1):
	oneNote = vTodos.mkNote()
	sco.extend(oneNote)

#####
#####
vTodos1.strtNxt = vFibo.srtsMemo[-1]
vTodos1.harmNo		= 11
vTodos1.distrs		= [.14, .15]
vTodos1.durMod		= .5
vTodos1.origin		= 164
vTodos1.step		= -1
vTodos1.ampModify	= 1
vTodos1.updateConfig()
for x in xrange(len(vTodos.rythmAtms) + 1):
	oneNote = vTodos1.mkNote()
	sco.extend(oneNote)

vFibo1.strtNxt = vPrimos.srtsMemo[-1]
vFibo1.harmNo		= 11
vFibo1.distrs		= [.034, .055]
vFibo1.durMod		= .333
vFibo1.origin		= 188
vFibo1.step			= 1
vFibo1.ampModify	= 1
vFibo1.updateConfig()
for x in xrange(len(vFibo.rythmAtms) + 1):
	oneNote = vFibo1.mkNote()
	sco.extend(oneNote)

vNones1.strtNxt = vTodos.srtsMemo[-1]
vNones1.harmNo		= 11
vNones1.distrs		= [.17, .19]
vNones1.durMod		= 0.166666667
vNones1.origin		= 258
vNones1.step		= -1
vNones1.ampModify	= 1
vNones1.updateConfig()
for x in xrange(len(vNones.rythmAtms) + 1):
	oneNote = vNones1.mkNote()
	sco.extend(oneNote)

vPrimos1.strtNxt = vPares.srtsMemo[-1]
vPrimos1.harmNo		= 11
vPrimos1.distrs		= [.19, .23]
vPrimos1.durMod		= 0.25
vPrimos1.origin		= 211
vPrimos1.step		= -1
vPrimos1.ampModify	= 1
vPrimos1.updateConfig()
for x in xrange(len(vPrimos.rythmAtms) + 1):
	oneNote = vPrimos1.mkNote()
	sco.extend(oneNote)

vPares1.strtNxt = vNones.srtsMemo[-1]
vPares1.harmNo		= 11
vPares1.distrs		= [.14, .16]
vPares1.durMod		= 0.2
vPares1.origin		= 235
vPares1.step		= 1
vPares1.ampModify	= 1
vPares1.updateConfig()
for x in xrange(len(vPares.rythmAtms) + 1):
	oneNote = vPares1.mkNote()
	sco.extend(oneNote)


#####
#####
vTodos2.strtNxt = vPrimos1.srtsMemo[-1]
vTodos2.harmNo		= 12
vTodos2.distrs		= [.16, .17]
vTodos2.durMod		= .25
vTodos2.origin		= 188
vTodos2.step		= -1
vTodos2.ampModify	= 2
vTodos2.updateConfig()
for x in xrange(len(vTodos.rythmAtms) + 1):
	oneNote = vTodos2.mkNote()
	sco.extend(oneNote)

vFibo2.strtNxt = vPares1.srtsMemo[-1]
vFibo2.harmNo		= 12
vFibo2.distrs		= [.055, .089]
vFibo2.durMod		= .2
vFibo2.origin		= 211
vFibo2.step			= 1
vFibo2.ampModify	= 2
vFibo2.updateConfig()
for x in xrange(len(vFibo.rythmAtms) + 1):
	oneNote = vFibo2.mkNote()
	sco.extend(oneNote)

vNones2.strtNxt = vFibo1.srtsMemo[-1]
vNones2.harmNo		= 12
vNones2.distrs		= [.21, .23]
vNones2.durMod		= .333
vNones2.origin		= 164
vNones2.step		= 1
vNones2.ampModify	= 2
vNones2.updateConfig()
for x in xrange(len(vNones.rythmAtms) + 1):
	oneNote = vNones2.mkNote()
	sco.extend(oneNote)

vPrimos2.strtNxt = vNones1.srtsMemo[-1]
vPrimos2.harmNo		= 12
vPrimos2.distrs		= [.29, .31]
vPrimos2.durMod		= 0.166666667
vPrimos2.origin		= 235
vPrimos2.step		= -1
vPrimos2.ampModify	= 2
vPrimos2.updateConfig()
for x in xrange(len(vPrimos.rythmAtms) + 1):
	oneNote = vPrimos2.mkNote()
	sco.extend(oneNote)

vPares2.strtNxt = vTodos1.srtsMemo[-1]
vPares2.harmNo		= 12
vPares2.distrs		= [.18, .20]
vPares2.durMod		= 0.142857143
vPares2.origin		= 164
vPares2.step		= 1
vPares2.ampModify	= 2
vPares2.updateConfig()
for x in xrange(len(vPares.rythmAtms) + 1):
	oneNote = vPares2.mkNote()
	sco.extend(oneNote)
###
###


vTodos3.strtNxt = vPares2.srtsMemo[-1]
vTodos3.harmNo		= 13
vTodos3.distrs		= [.18, .19]
vTodos3.durMod		= 0.166666667
vTodos3.origin		= 211
vTodos3.step		= 1
vTodos3.ampModify	= 3
vTodos3.updateConfig()
for x in xrange(len(vTodos.rythmAtms) + 1):
	oneNote = vTodos3.mkNote()
	sco.extend(oneNote)

vFibo3.strtNxt = vNones2.srtsMemo[-1]
vFibo3.harmNo		= 13
vFibo3.distrs		= [.089, .144]
vFibo3.durMod		= 0.142857143
vFibo3.origin		= 235
vFibo3.step			= 1
vFibo3.ampModify	= 3
vFibo3.updateConfig()
for x in xrange(len(vFibo.rythmAtms) + 1):
	oneNote = vFibo3.mkNote()
	sco.extend(oneNote)

vNones3.strtNxt = vPrimos2.srtsMemo[-1]
vNones3.harmNo		= 13
vNones3.distrs		= [.25, .27]
vNones3.durMod		= .2
vNones3.origin		= 188
vNones3.step		= 1
vNones3.ampModify	= 3
vNones3.updateConfig()
for x in xrange(len(vNones.rythmAtms) + 1):
	oneNote = vNones3.mkNote()
	sco.extend(oneNote)

vPrimos3.strtNxt = vTodos2.srtsMemo[-1]
vPrimos3.harmNo		= 13
vPrimos3.distrs		= [.37, .41]
vPrimos3.durMod		= 0.125
vPrimos3.origin		= 258
vPrimos3.step		= -1
vPrimos3.ampModify	= 3
vPrimos3.updateConfig()
for x in xrange(len(vPrimos.rythmAtms) + 1):
	oneNote = vPrimos3.mkNote()
	sco.extend(oneNote)

vPares3.strtNxt = vFibo2.srtsMemo[-1]
vPares3.harmNo		= 13
vPares3.distrs		= [.22, .24]
vPares3.durMod		= 0.25
vPares3.origin		= 164
vPares3.step		= -1
vPares3.ampModify	= 3
vPares3.updateConfig()
for x in xrange(len(vPares.rythmAtms) + 1):
	oneNote = vPares3.mkNote()
	sco.extend(oneNote)
###########
vTodos4.strtNxt = vNones.srtsMemo[-1]
vTodos4.harmNo		= 14
vTodos4.distrs		= [.20, .21]
vTodos4.durMod		= .125
vTodos4.origin		= 235
vTodos4.step		= -4
vTodos4.ampModify	= -1
vTodos4.updateConfig()
for x in xrange(len(vTodos.rythmAtms) + 1):
	oneNote = vTodos4.mkNote()
	sco.extend(oneNote)

vFibo4.strtNxt = vTodos3.srtsMemo[-1]
vFibo4.harmNo		= 14
vFibo4.distrs		= [.144, .233]
vFibo4.durMod		= .1111
vFibo4.origin		= 258
vFibo4.step			= 1
vFibo4.ampModify	= 4
vFibo4.updateConfig()
for x in xrange(len(vFibo.rythmAtms) + 1):
	oneNote = vFibo4.mkNote()
	sco.extend(oneNote)

vNones4.strtNxt = vPares3.srtsMemo[-1]
vNones4.harmNo		= 14
vNones4.distrs		= [.29, .31]
vNones4.durMod		= 0.142857143
vNones4.origin		= 211
vNones4.step		= 1
vNones4.ampModify	= 4
vNones4.updateConfig()
for x in xrange(len(vNones.rythmAtms) + 1):
	oneNote = vNones4.mkNote()
	sco.extend(oneNote)

vPrimos4.strtNxt = vFibo3.srtsMemo[-1]
vPrimos4.harmNo		= 14
vPrimos4.distrs		= [.43, .47]
vPrimos4.durMod		= 0.2
vPrimos4.origin		= 164
vPrimos4.step		= 1
vPrimos4.ampModify	= 4
vPrimos4.updateConfig()
for x in xrange(len(vPrimos.rythmAtms) + 1):
	oneNote = vPrimos4.mkNote()
	sco.extend(oneNote)

vPares4.strtNxt = vPrimos3.srtsMemo[-1]
vPares4.harmNo		= 14
vPares4.distrs		= [.26, .28]
vPares4.durMod		= 0.166666667
vPares4.origin		= 188
vPares4.step		= -1
vPares4.ampModify	= 4
vPares4.updateConfig()
for x in xrange(len(vPares.rythmAtms) + 1):
	oneNote = vPares4.mkNote()
	sco.extend(oneNote)

vTodos5.strtNxt = vTodos4.srtsMemo[-1]
vTodos5.harmNo		= 15
vTodos5.distrs		= [.22, .23]
vTodos5.durMod		= 0.1
vTodos5.origin		= 281
vTodos5.step		= -1
vTodos5.ampModify	= 5
vTodos5.updateConfig()
for x in xrange(len(vTodos.rythmAtms) + 1):
	oneNote = vTodos5.mkNote()
	sco.extend(oneNote)

vFibo5.strtNxt = vFibo4.srtsMemo[-1]
vFibo5.harmNo		= 15
vFibo5.distrs		= [.233, .377]
vFibo5.durMod		= 0.166666667
vFibo5.origin		= 188
vFibo5.step			= 1
vFibo5.ampModify	= 5
vFibo5.updateConfig()
for x in xrange(len(vFibo.rythmAtms) + 1):
	oneNote = vFibo5.mkNote()
	sco.extend(oneNote)

vNones5.strtNxt = vNones4.srtsMemo[-1]
vNones5.harmNo		= 15
vNones5.distrs		= [.33, .35]
vNones5.durMod		= 0.1111
vNones5.origin		= 258
vNones5.step		= -1
vNones5.ampModify	= 5
vNones5.updateConfig()
for x in xrange(len(vNones.rythmAtms) + 1):
	oneNote = vNones5.mkNote()
	sco.extend(oneNote)

vPrimos5.strtNxt = vPrimos4.srtsMemo[-1]
vPrimos5.harmNo		= 15
vPrimos5.distrs		= [.53, .59]
vPrimos5.durMod		= 0.142857143
vPrimos5.origin		= 211
vPrimos5.step		= -1
vPrimos5.ampModify	= 5
vPrimos5.updateConfig()
for x in xrange(len(vPrimos.rythmAtms) + 1):
	oneNote = vPrimos5.mkNote()
	sco.extend(oneNote)

vPares5.strtNxt = vPares4.srtsMemo[-1]
vPares5.harmNo		= 15
vPares5.distrs		= [.30, .32]
vPares5.durMod		= 0.125
vPares5.origin		= 235
vPares5.step		= 1
vPares5.ampModify	= 5
vPares5.updateConfig()
for x in xrange(len(vPares.rythmAtms) + 1):
	oneNote = vPares5.mkNote()
	sco.extend(oneNote)

vPrimos6.strtNxt = vPares5.srtsMemo[-1]
vPrimos6.harmNo		= 30
vPrimos6.distrs		= [.61, .67]
vPrimos6.durMod		= 0.090909091
vPrimos6.origin		= 235
vPrimos6.step		= -5
vPrimos6.ampModify	= 6
vPrimos6.updateConfig()
for x in xrange(len(vPrimos.rythmAtms) + 1):
	oneNote = vPrimos6.mkNote()
	sco.extend(oneNote)

vFibo6.strtNxt = vTodos5.srtsMemo[-1]
vFibo6.harmNo		= 30
vFibo6.distrs		= [.377, .610]
vFibo6.durMod		= 0.083333333
vFibo6.origin		= 281
vFibo6.step			= 1
vFibo6.ampModify	= 6
vFibo6.updateConfig()
for x in xrange(len(vFibo.rythmAtms) + 1):
	oneNote = vFibo6.mkNote()
	sco.extend(oneNote)

#####
#####
#####
lastStrts	= []
for x in voiceLstInc:
	lastStrts.append(x.strtNxt)

lastStrts.sort()

for x in voiceLstInc:
	while x.strt < lastStrts[-1]:
		oneNote = x.mkNote()
		sco.extend(oneNote)

lastStrts[-1] += 3

for x in voiceLstInc[5:]:
	if voiceLstInc.index(x) > len(voiceLstInc) * .5:
		x.distrs = [x.distrs[1], x.distrs[1]]
	if voiceLstInc.index(x) > len(voiceLstInc) * .75:
		x.origin += 1
	else:
		x.origin += 2
	if voiceLstInc.index(x) % 13 == 0:
		x.step = 1
	else:
		x.step = 0

	x.ampModify	-= 2
	while x.strt < lastStrts[-1]:
		oneNote = x.mkNote()
		sco.extend(oneNote)

lastStrts[-1] += 4

for x in voiceLstInc[10:]:
	if voiceLstInc.index(x) > len(voiceLstInc) * .5:
		x.distrs = [x.distrs[1], x.distrs[1]]
	if voiceLstInc.index(x) > len(voiceLstInc) * .75:
		x.origin += 1
	else:
		x.origin += 2
	if voiceLstInc.index(x) % 11 == 0:
		x.step = 2
	else:
		x.step = 0
	x.origin += 1
	x.ampModify	-= 2
	while x.strt < lastStrts[-1]:
		oneNote = x.mkNote()
		sco.extend(oneNote)

lastStrts[-1] += 7

for x in voiceLstInc[15:]:
	if voiceLstInc.index(x) > len(voiceLstInc) * .5:
		x.distrs = [x.distrs[1], x.distrs[1]]
	if voiceLstInc.index(x) > len(voiceLstInc) * .75:
		x.origin += 1
	else:
		x.origin += 2
	if voiceLstInc.index(x) % 7 == 0:
		x.step = 3
	else:
		x.step = 0
	x.origin += 1
	x.ampModify	-= 2
	while x.strt < lastStrts[-1]:
		oneNote = x.mkNote()
		sco.extend(oneNote)

lastStrts[-1] += 11


tempo = tempo + str(vPrimos6.srtsMemo[-1] - .001) + ' 88 '
tempo = tempo + str(vPrimos6.srtsMemo[-1]) + ' 77 '

for x in voiceLstInc[20:]:
	if voiceLstInc.index(x) > len(voiceLstInc) * .5:
		x.distrs = [x.distrs[1], x.distrs[1]]
	if voiceLstInc.index(x) > len(voiceLstInc) * .75:
		x.origin += 1
	else:
		x.origin += 2
	if voiceLstInc.index(x) % 5 == 0:
		x.step = 4
	else:
		x.step = 0
	x.origin += 1
	x.ampModify	+= 2
	while x.strt < lastStrts[-1]:
		oneNote = x.mkNote()
		sco.extend(oneNote)

lastStrts[-1] += 18

tempo = tempo + str(vPrimos6.srtsMemo[-1]) + ' 88 '

for x in voiceLstInc[25:]:
	if voiceLstInc.index(x) > len(voiceLstInc) * .5:
		x.distrs = [x.distrs[1], x.distrs[1]]
	if voiceLstInc.index(x) > len(voiceLstInc) * .75:
		x.origin += 1
	else:
		x.origin += 2
	if voiceLstInc.index(x) % 3 == 0:
		x.step = 5
	else:
		x.step = 0
	x.origin += 1
	x.ampModify	+= 2
	while x.strt < lastStrts[-1]:
		oneNote = x.mkNote()
		sco.extend(oneNote)

tempo = tempo + str(vPrimos6.srtsMemo[-1]) + ' 88 '

lastStrts[-1] += 29

for x in voiceLstInc[30:]:
	if voiceLstInc.index(x) > len(voiceLstInc) * .5:
		x.distrs = [x.distrs[1], x.distrs[1]]
	if voiceLstInc.index(x) > len(voiceLstInc) * .75:
		x.origin += 1
	else:
		x.origin += 2.75
	if voiceLstInc.index(x) % 2 == 0:
		x.step = 6
	else:
		x.step = 0
	x.origin += 1
	x.ampModify	+= 2
	while x.strt < lastStrts[-1]:
		oneNote = x.mkNote()
		sco.extend(oneNote)

tempo = tempo + str(vPrimos6.srtsMemo[-1]) + ' 110 '

strtNxtSect = vPrimos6.strtNxt + 20

###############################################################################
strtNxtSect = vPrimos6.strtNxt + 20

sco2 = []

tempo = tempo + str(strtNxtSect) + ' 110 '

voiceLst = [vTodos,
			vFibo,
			vNones,
			vPrimos,
			vPares,
			vTodos1,
			vFibo1,
			vNones1,
			vPrimos1,
			vPares1,
			vTodos2,
			vFibo2,
			vNones2,
			vPrimos2,
			vPares2,
			vTodos3,
			vFibo3,
			vNones3,
			vPrimos3,
			vPares3,
			vTodos4,
			vFibo4,
			vNones4,
			vPrimos4,
			vPares4,
			vTodos5,
			vFibo5,
			vNones5,
			vPrimos5,
			vPares5,
			vTodos6,
			vFibo6,
			vNones6,
			vPrimos6,
			vPares6,
			vTodos7,
			vFibo7,
			vNones7,
			vPrimos7,
			vPares7,
			vTodos8,
			vFibo8,
			vNones8,
			vPrimos8,
			vPares8,
			vTodos9,
			vFibo9]

pitchStepLst = [-1,-2, -3, -4, -5, 1, 1 ,2, 3, 5, 2, 3, 5]


import Numeric_utils as NumericUtils
Scaling		= NumericUtils.Scaling()
Series		= NumericUtils.Series(0)
primes		= Series.prime(47)
pitches		= range(47)

counter = 0
low = []
hi = []
lastMem = []

while counter < 47:
	if counter % 2 == 0:
		low.append((pitches.pop(0),primes.pop(0)))
	else:
		hi.append((pitches.pop(),primes.pop(0)))
	counter += 1

primes		= Series.prime(47)
print primes

low.pop()
hi.reverse()
pitchBeat = low + hi
print pitchBeat

for x, pB in zip(voiceLst, pitchBeat):
	primeIndx = primes.index(pB[1])
	reps = primes[primeIndx + 1]
	x.strtNxt		= strtNxtSect
	x.origin		= pB[0]
	x.harmNo		= 20
	ampModify		= range(reps - 1)
	ampModify.insert(0, 19)
	x.durMod		= pB[1] * .001
	x.countDown 	= 100
	x.pitchSteps	 = random.sample(pitchStepLst, 12)
	x.updateConfig()
	for y in ampModify:
		if x.origin > 0:
			x.origin += random.choice(x.pitchSteps)
		if x.origin < 0:
				x.origin = 0
		x.ampModify = Scaling.valToRng(y, ampModify[1], ampModify[-1], 7, 19)
		oneNote = x.mkNote2()
		lastMem.append(x.srtsMemo[-1])
		sco2.extend(oneNote)
		x.countDown -= 1

lastMem.sort()

tempo = tempo + str(lastMem.pop()) + ' 110 '







#####
#####
#####

#sco.insert(0, tempo)
sco2.insert(0, tempo)
sco2.insert(0, 'a 0 0 ' + str(strtNxtSect))
CsndCtrl	= CsndInterface.CsndCtrl(sco2)
#CsndCtrl	= CsndInterface.CsndCtrl(sco)
CsndCtrl.render()

