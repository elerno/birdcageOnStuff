import random

import Csnd_interface2 as CsndInterface
import ProcessA as ProcessA

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

sco = []
tempo = 't 0 55 '

vTodos.updateConfig()
for x in xrange(len(vTodos.rythmAtms) + 1):
	oneNote = vTodos.mkNote()
	sco.extend(oneNote)

#####
#####
#####

vTodos.strtNxt = vFibo.strtNxt = vTodos.strtNxt + 30

vTodos.harmNo		= 2
vTodos.distrs		= [.02, .03]
vTodos.durMod		= 1
vTodos.origin		= 212
vTodos.step			= -2

vFibo.rythmAtms		= [1, 1, 2, 3, 5, 8]
vFibo.harmNo		= 2
vFibo.distrs		= [.001, .001]
vFibo.durMod		= .5
vFibo.origin		= 164
vFibo.step			= 1



vFibo.updateConfig()
for x in xrange(len(vFibo.rythmAtms) + 2):
	oneNote = vFibo.mkNote()
	sco.extend(oneNote)

vTodos.updateConfig()
while vTodos.strt < vFibo.srtsMemo[-1]:
	oneNote = vTodos.mkNote()
	sco.extend(oneNote)

#####
#####
#####

vNones.strtNxt =  vPrimos.strtNxt = vTodos.strtNxt + 30

tempo = tempo + str(vNones.strtNxt) + ' 55 '

vTodos.harmNo		= 3
vTodos.distrs		= [.03, .04]
vTodos.durMod		= .5
vTodos.origin		= 116
vTodos.step			= 3

vFibo.harmNo		= 3
vFibo.distrs		= [.001, .002]
vFibo.durMod		= .25
vFibo.origin		= 22
vFibo.step			= -2

vNones.rythmAtms	= [1, 3, 5, 7, 9]
vNones.harmNo		= 3
vNones.distrs		= [.01, .03]
vNones.durMod		= 1
vNones.origin		= 117
vNones.step			= 1

vPrimos.rythmAtms	= [2, 3, 5, 7]
vPrimos.harmNo		= 3
vPrimos.distrs		= [.02, .03]
vPrimos.durMod		= .333
vPrimos.origin		= 70
vPrimos.step		= -1

vNones.updateConfig()
for x in xrange(len(vNones.rythmAtms) + 1):
	oneNote = vNones.mkNote()
	sco.extend(oneNote)

vPrimos.updateConfig()
for x in xrange(len(vPrimos.rythmAtms) + 1):
	oneNote = vPrimos.mkNote()
	sco.extend(oneNote)

vTodos.strtNxt =  vNones.strtNxt
vTodos.updateConfig()
for x in xrange((len(vTodos.rythmAtms) + 1) * 3):
	oneNote = vTodos.mkNote()
	sco.extend(oneNote)
vTodos.durMod = 3
oneNote = vTodos.mkNote()
vTodos.durMod = 1
sco.extend(oneNote)

vFibo.strtNxt =  vPrimos.strtNxt
vFibo.updateConfig()
for x in xrange(len(vFibo.rythmAtms) + 1):
	oneNote = vFibo.mkNote()
	sco.extend(oneNote)

while vNones.strt < vTodos.srtsMemo[-1]:
	oneNote = vNones.mkNote()
	sco.extend(oneNote)
vNones.durMod = 3
oneNote = vTodos.mkNote()
vNones.durMod = 1
sco.extend(oneNote)

for x in xrange(len(vPrimos.rythmAtms) + 1):
	oneNote = vPrimos.mkNote()
	sco.extend(oneNote)

tempo = tempo + str(vNones.strtNxt ) + ' 66 '

#####
#####
#####

vTodos.strtNxt = vFibo.strtNxt =  vNones.strtNxt =  vPrimos.strtNxt =   vPares.strtNxt = vTodos1.strtNxt = vFibo1.strtNxt =  vNones1.strtNxt = vNones.strtNxt + 30

vTodos.harmNo		= 4
vTodos.distrs		= [.04, .05]
vTodos.durMod		= .2
vTodos.origin		= 260
vTodos.step			= -4

vFibo.harmNo		= 4
vFibo.distrs		= [.002, .003]
vFibo.durMod		= .25
vFibo.origin		= 71
vFibo.step			= 3

vNones.harmNo		= 4
vNones.distrs		= [.03, .05]
vNones.durMod		= .333
vNones.origin		= 212
vNones.step			= -2

vPrimos.harmNo		= 4
vPrimos.distrs		= [.03, .05]
vPrimos.durMod		= .5
vPrimos.origin		= 164
vPrimos.step		= 2

vPares.rythmAtms	= [2, 4, 6, 8, 10]
vPares.harmNo		= 4
vPares.distrs		= [.02, .04]
vPares.durMod		= 1
vPares.origin		= 117
vPares.step			= -1

vTodos.updateConfig()
for x in xrange(len(vTodos.rythmAtms) + 2):
	oneNote = vTodos.mkNote()
	sco.extend(oneNote)

vFibo.updateConfig()
for x in xrange(len(vFibo.rythmAtms) + 2):
	oneNote = vFibo.mkNote()
	sco.extend(oneNote)

vNones.updateConfig()
for x in xrange(len(vNones.rythmAtms) + 2):
	oneNote = vNones.mkNote()
	sco.extend(oneNote)

vPrimos.updateConfig()
for x in xrange(len(vPrimos.rythmAtms) + 2):
	oneNote = vPrimos.mkNote()
	sco.extend(oneNote)

vPares.updateConfig()
for x in xrange(len(vPares.rythmAtms) + 2):
	oneNote = vPares.mkNote()
	sco.extend(oneNote)

######
######

vTodos1.strtNxt = vTodos.srtsMemo[1]
vTodos1.harmNo		= 5
vTodos1.distrs		= [.06, .06]
vTodos1.durMod		= .5
vTodos1.origin		= 256
vTodos1.step		= 1
vTodos1.ampModify	= 1
vTodos1.updateConfig()
for x in xrange((len(vTodos1.rythmAtms) + 1) * 4):
	oneNote = vTodos1.mkNote()
	sco.extend(oneNote)

vFibo1.strtNxt = vFibo.srtsMemo[1]
vFibo1.harmNo		= 5
vFibo1.distrs		= [.005, .005]
vFibo1.durMod		= .5
vFibo1.origin		= 68
vFibo1.step			= -1
vFibo1.ampModify	= 1
vFibo1.updateConfig()
for x in xrange((len(vFibo1.rythmAtms) + 1) * 4):
	oneNote = vFibo1.mkNote()
	sco.extend(oneNote)

vNones1.strtNxt = vNones.srtsMemo[1]
vNones1.harmNo		= 5
vNones1.distrs		= [.07, .07]
vNones1.durMod		= .5
vNones1.origin		= 210
vNones1.step		= 1
vNones1.updateConfig()
for x in xrange((len(vNones1.rythmAtms) + 1) * 4):
	oneNote = vNones1.mkNote()
	sco.extend(oneNote)

#####
#####
#####

tempoOpts = [vTodos.strtNxt, vFibo.strtNxt,  vNones.strtNxt,  vPrimos.strtNxt,
				vPares.strtNxt]
tempoOpts.sort()

tempo = tempo + str(tempoOpts[2]) + ' 66 '

vTodos.harmNo		= 6
vTodos.distrs		= [.07, .08]
vTodos.durMod		= .2
vTodos.origin		= 214
vTodos.step			= 1

vFibo.harmNo		= 6
vFibo.distrs		= [.005, .008]
vFibo.durMod		= .25
vFibo.origin		= 25
vFibo.step			= -1

vNones.harmNo		= 6
vNones.distrs		= [.07, .09]
vNones.durMod		= .333
vNones.origin		= 166
vNones.step			= 1

vPrimos.harmNo		= 6
vPrimos.distrs		= [.05, .07]
vPrimos.durMod		= .5
vPrimos.origin		= 118
vPrimos.step		= -1

vPares.harmNo		= 6
vPares.distrs		= [.04, .06]
vPares.durMod		= 0.166666667
vPares.origin		= 171
vPares.step			= 2



vFibo.updateConfig()
for x in xrange((len(vFibo.rythmAtms) + 1) * 1):
	oneNote = vFibo.mkNote()
	sco.extend(oneNote)

vPares.updateConfig()
for x in xrange((len(vPares.rythmAtms) + 1) * 1):
	oneNote = vPares.mkNote()
	sco.extend(oneNote)

vPrimos.updateConfig()
for x in xrange((len(vPrimos.rythmAtms) + 1) * 2):
	oneNote = vPrimos.mkNote()
	sco.extend(oneNote)

vNones.updateConfig()
for x in xrange((len(vNones.rythmAtms) + 1) * 3):
	oneNote = vNones.mkNote()
	sco.extend(oneNote)

vTodos.updateConfig()
for x in xrange((len(vTodos.rythmAtms) + 1) * 4):
	oneNote = vTodos.mkNote()
	sco.extend(oneNote)

#####
#####

vTodos1.strtNxt = vTodos.srtsMemo[13]
vTodos1.harmNo		= 7
vTodos1.distrs		= [.08, .08]
vTodos1.durMod		= .5
vTodos1.origin		= 302
vTodos1.step		= -1
vTodos1.ampModify	= 0
vTodos1.updateConfig()
for x in xrange((len(vTodos1.rythmAtms) + 1) * 2):
	oneNote = vTodos1.mkNote()
	sco.extend(oneNote)

vFibo1.strtNxt = vFibo.srtsMemo[5]
vFibo1.harmNo		= 7
vFibo1.distrs		= [.013, .013]
vFibo1.durMod		= .5
vFibo1.origin		= 208
vFibo1.step			= 1
vFibo1.ampModify	= 1
vFibo1.updateConfig()
for x in xrange((len(vFibo1.rythmAtms) + 1) * 2):
	oneNote = vFibo1.mkNote()
	sco.extend(oneNote)

vNones1.strtNxt = vNones.srtsMemo[12]
vNones1.harmNo		= 7
vNones1.distrs		= [.11, .11]
vNones1.durMod		= .5
vNones1.origin		= 303
vNones1.step		= -1
vNones1.ampModify	= 0
vNones1.updateConfig()
for x in xrange((len(vNones1.rythmAtms) + 1) * 2):
	oneNote = vNones1.mkNote()
	sco.extend(oneNote)

vPrimos1.strtNxt = vPrimos.srtsMemo[7]
vPrimos1.harmNo		= 7
vPrimos1.distrs		= [.11, .11]
vPrimos1.durMod		= 0.5
vPrimos1.origin		= 256
vPrimos1.step		= -1
vPrimos1.ampModify	= 0
vPrimos1.updateConfig()
for x in xrange((len(vPrimos1.rythmAtms) + 1) * 2):
	oneNote = vPrimos1.mkNote()
	sco.extend(oneNote)

vPares1.strtNxt = vPares.srtsMemo[4]
vPares1.harmNo		= 7
vPares1.distrs		= [.08, .08]
vPares1.durMod		= 0.5
vPares1.origin		= 210
vPares1.step		= 1
vPares1.ampModify	= 1
vPares1.updateConfig()
for x in xrange((len(vPares1.rythmAtms) + 1) * 2):
	oneNote = vPares1.mkNote()
	sco.extend(oneNote)

vTodos2.strtNxt = vTodos1.srtsMemo[2]
tempo = tempo + str(vTodos2.strtNxt ) + ' 77 '
vTodos2.harmNo		= 8
vTodos2.distrs		= [.09, .09]
vTodos2.durMod		= .333
vTodos2.origin		= 309
vTodos2.step		= 2
vTodos2.ampModify	= 0
vTodos2.updateConfig()
for x in xrange((len(vTodos2.rythmAtms) + 1) * 3):
	oneNote = vTodos2.mkNote()
	sco.extend(oneNote)

vFibo2.strtNxt = vFibo1.srtsMemo[2]
vFibo2.harmNo		= 8
vFibo2.distrs		= [.021, .021]
vFibo2.durMod		= .333
vFibo2.origin		= 214
vFibo2.step			= -2
vFibo2.ampModify	= 2
vFibo2.updateConfig()
for x in xrange((len(vFibo2.rythmAtms) + 1) * 3):
	oneNote = vFibo2.mkNote()
	sco.extend(oneNote)

vNones2.strtNxt = vNones1.srtsMemo[2]
vNones2.harmNo		= 8
vNones2.distrs		= [.13, .13]
vNones2.durMod		= .333
vNones2.origin		= 308
vNones2.step		= 2
vNones2.ampModify	= 0
vNones2.updateConfig()
for x in xrange((len(vNones2.rythmAtms) + 1) * 3):
	oneNote = vNones2.mkNote()
	sco.extend(oneNote)

vPrimos2.strtNxt = vPrimos1.srtsMemo[2]
vPrimos2.harmNo		= 8
vPrimos2.distrs		= [.13, .13]
vPrimos2.durMod		= 0.333
vPrimos2.origin		= 260
vPrimos2.step		= 2
vPrimos2.ampModify	= 1
vPrimos2.updateConfig()
for x in xrange((len(vPrimos2.rythmAtms) + 1) * 3):
	oneNote = vPrimos2.mkNote()
	sco.extend(oneNote)

vPares2.strtNxt = vPares1.srtsMemo[2]
vPares2.harmNo		= 8
vPares2.distrs		= [.1, .1]
vPares2.durMod		= 0.333
vPares2.origin		= 213
vPares2.step		= -1
vPares2.ampModify	= 1
vPares2.updateConfig()
for x in xrange((len(vPares2.rythmAtms) + 1) * 3):
	oneNote = vPares2.mkNote()
	sco.extend(oneNote)

tempo = tempo + str(vTodos2.srtsMemo[3] - .001) + ' 88 '
tempo = tempo + str(vTodos2.srtsMemo[3]) + ' 77 '

vTodos3.strtNxt = vTodos2.srtsMemo[3]
vTodos3.harmNo		= 9
vTodos3.distrs		= [.1, .1]
vTodos3.durMod		= .25
vTodos3.origin		= 348
vTodos3.step		= -2
vTodos3.ampModify	= 0
vTodos3.updateConfig()
for x in xrange((len(vTodos3.rythmAtms) + 1) * 4):
	oneNote = vTodos3.mkNote()
	sco.extend(oneNote)
vNones.durMod = 2
oneNote = vTodos.mkNote()
vNones.durMod = 1
sco.extend(oneNote)

#####
#####
#####

vTodos.strtNxt = vFibo.strtNxt =  vNones.strtNxt =  vPrimos.strtNxt = vPares.strtNxt = vTodos1.strtNxt = vFibo1.strtNxt =  vNones1.strtNxt = vPrimos1.strtNxt = vPares1.strtNxt = vTodos2.strtNxt = vFibo2.strtNxt =  vNones2.strtNxt = vPrimos2.strtNxt = vPares2.strtNxt = vTodos3.strtNxt = vFibo3.strtNxt =  vNones3.strtNxt = vPrimos3.strtNxt = vPares3.strtNxt = vTodos4.strtNxt = vFibo4.strtNxt =  vNones4.strtNxt =  vPrimos4.strtNxt = vPares4.strtNxt = vTodos5.strtNxt = vFibo5.strtNxt =  vNones5.strtNxt =  vPrimos5.strtNxt = vPares5.strtNxt = vTodos6.strtNxt = vFibo6.strtNxt = vTodos3.srtsMemo[3]

vTodos.harmNo		= 10
vTodos.distrs		= [.12, .13]
vTodos.durMod		= .2
vTodos.origin		= 211
vTodos.step			= -5

vFibo.harmNo		= 10
vFibo.distrs		= [.021, .034]
vFibo.durMod		= .25
vFibo.origin		= 23
vFibo.step			= 4

vNones.harmNo		= 10
vNones.distrs		= [.13, .15]
vNones.durMod		= .333
vNones.origin		= 164
vNones.step			= -3

vPrimos.harmNo		= 10
vPrimos.distrs		= [.13, .17]
vPrimos.durMod		= 0.142857143
vPrimos.origin		= 117
vPrimos.step		= 3

vPares.harmNo		= 10
vPares.distrs		= [.1, .12]
vPares.durMod		= 0.166666667
vPares.origin		= 70
vPares.step			= -2

vTodos.updateConfig()
for x in xrange(len(vTodos.rythmAtms) + 1):
	oneNote = vTodos.mkNote()
	sco.extend(oneNote)

vFibo.updateConfig()
for x in xrange(len(vFibo.rythmAtms) + 1):
	oneNote = vFibo.mkNote()
	sco.extend(oneNote)

vNones.updateConfig()
for x in xrange(len(vNones.rythmAtms) + 1):
	oneNote = vNones.mkNote()
	sco.extend(oneNote)

vPrimos.updateConfig()
for x in xrange(len(vPrimos.rythmAtms) + 1):
	oneNote = vPrimos.mkNote()
	sco.extend(oneNote)

vPares.updateConfig()
for x in xrange(len(vPares.rythmAtms) + 1):
	oneNote = vPares.mkNote()
	sco.extend(oneNote)

#####
#####

vTodos1.strtNxt = vTodos.srtsMemo[1]
vTodos1.harmNo		= 11
vTodos1.distrs		= [.14, .14]
vTodos1.durMod		= .5
vTodos1.origin		= 211
vTodos1.step		= 3
vTodos1.ampModify	= 1
vTodos1.updateConfig()
for x in xrange(len(vTodos1.rythmAtms) + 1):
	oneNote = vTodos1.mkNote()
	sco.extend(oneNote)

vFibo1.strtNxt = vFibo.srtsMemo[1]
vFibo1.harmNo		= 11
vFibo1.distrs		= [.055, .055]
vFibo1.durMod		= .5
vFibo1.origin		= 211
vFibo1.step			= 2
vFibo3.ampModify	= 3
vFibo1.updateConfig()
for x in xrange(len(vFibo1.rythmAtms) + 1):
	oneNote = vFibo1.mkNote()
	sco.extend(oneNote)

vNones1.strtNxt = vNones.srtsMemo[1]
vNones1.harmNo		= 11
vNones1.distrs		= [.17, .17]
vNones1.durMod		= .5
vNones1.origin		= 211
vNones1.step		= 2
vNones1.ampModify	= 1
vNones1.updateConfig()
for x in xrange(len(vNones1.rythmAtms) + 1):
	oneNote = vNones1.mkNote()
	sco.extend(oneNote)

vPrimos1.strtNxt = vPrimos.srtsMemo[1]
vPrimos1.harmNo		= 11
vPrimos1.distrs		= [.19, .19]
vPrimos1.durMod		= 0.5
vPrimos1.origin		= 117
vPrimos1.step		= 2
vPrimos1.ampModify	= 1
vPrimos1.updateConfig()
for x in xrange(len(vPrimos1.rythmAtms) + 1):
	oneNote = vPrimos1.mkNote()
	sco.extend(oneNote)

vPares1.strtNxt = vPares.srtsMemo[1]
vPares1.harmNo		= 11
vPares1.distrs		= [.14, .14]
vPares1.durMod		= 0.5
vPares1.origin		= 70
vPares1.step		= 2
vPares1.ampModify	= 1
vPares1.updateConfig()
for x in xrange(len(vPares1.rythmAtms) + 1):
	oneNote = vPares1.mkNote()
	sco.extend(oneNote)

vTodos2.strtNxt = vTodos.srtsMemo[2]
vTodos2.harmNo		= 12
vTodos2.distrs		= [.15, .15]
vTodos2.durMod		= .333
vTodos2.origin		= 211
vTodos2.step		= -3
vTodos2.ampModify	= 2
vTodos2.updateConfig()
for x in xrange(len(vTodos2.rythmAtms) + 1):
	oneNote = vTodos2.mkNote()
	sco.extend(oneNote)

vFibo2.strtNxt = vFibo1.srtsMemo[1]
vFibo2.harmNo		= 12
vFibo2.distrs		= [.089, .089]
vFibo2.durMod		= .333
vFibo2.origin		= 211
vFibo2.step			= -3
vFibo2.ampModify	= 2
vFibo2.updateConfig()
for x in xrange(len(vFibo2.rythmAtms) + 1):
	oneNote = vFibo2.mkNote()
	sco.extend(oneNote)

vNones2.strtNxt = vNones.srtsMemo[2]
vNones2.harmNo		= 12
vNones2.distrs		= [.19, .19]
vNones2.durMod		= .333
vNones2.origin		= 211
vNones2.step		= -3
vNones2.ampModify	= 2
vNones2.updateConfig()
for x in xrange(len(vNones2.rythmAtms) + 1):
	oneNote = vNones2.mkNote()
	sco.extend(oneNote)

vPrimos2.strtNxt = vPrimos.srtsMemo[2]
vPrimos2.harmNo		= 12
vPrimos2.distrs		= [.23, .23]
vPrimos2.durMod		= 0.333
vPrimos2.origin		= 117
vPrimos2.step		= 3
vPrimos2.ampModify	= 2
vPrimos2.updateConfig()
for x in xrange(len(vPrimos2.rythmAtms) + 1):
	oneNote = vPrimos2.mkNote()
	sco.extend(oneNote)

vPares2.strtNxt = vPares.srtsMemo[2]
vPares2.harmNo		= 12
vPares2.distrs		= [.16, .16]
vPares2.durMod		= 0.333
vPares2.origin		= 70
vPares2.step		= -2
vPares2.ampModify	= 2
vPares2.updateConfig()
for x in xrange(len(vPares2.rythmAtms) + 1):
	oneNote = vPares2.mkNote()
	sco.extend(oneNote)

vTodos3.strtNxt = vTodos.srtsMemo[3]
vTodos3.harmNo		= 13
vTodos3.distrs		= [.16, .16]
vTodos3.durMod		= .25
vTodos3.origin		= 211
vTodos3.step		= 4
vTodos3.ampModify	= 3
vTodos3.updateConfig()
for x in xrange(len(vTodos3.rythmAtms) + 1):
	oneNote = vTodos3.mkNote()
	sco.extend(oneNote)

vFibo3.strtNxt = vFibo.srtsMemo[3]
vFibo3.harmNo		= 13
vFibo3.distrs		= [.144, .144]
vFibo3.durMod		= .25
vFibo3.origin		= 211
vFibo3.step			= 3
vFibo3.ampModify	= 3
vFibo3.updateConfig()
for x in xrange(len(vFibo3.rythmAtms) + 1):
	oneNote = vFibo3.mkNote()
	sco.extend(oneNote)

vNones3.strtNxt = vNones.srtsMemo[3]
vNones3.harmNo		= 13
vNones3.distrs		= [.21, .21]
vNones3.durMod		= .25
vNones3.origin		= 211
vNones3.step		= 3
vNones3.ampModify	= 3
vNones3.updateConfig()
for x in xrange(len(vNones3.rythmAtms) + 1):
	oneNote = vNones3.mkNote()
	sco.extend(oneNote)

vPrimos3.strtNxt = vPrimos.srtsMemo[3]
vPrimos3.harmNo		= 13
vPrimos3.distrs		= [.29, .29]
vPrimos3.durMod		= 0.25
vPrimos3.origin		= 117
vPrimos3.step		= -3
vPrimos3.ampModify	= 3
vPrimos3.updateConfig()
for x in xrange(len(vPrimos3.rythmAtms) + 1):
	oneNote = vPrimos3.mkNote()
	sco.extend(oneNote)

vPares3.strtNxt = vPares.srtsMemo[3]
vPares3.harmNo		= 13
vPares3.distrs		= [.18, .18]
vPares3.durMod		= 0.25
vPares3.origin		= 70
vPares3.step		= 3
vPares3.ampModify	= 3
vPares3.updateConfig()
for x in xrange(len(vPares3.rythmAtms) + 1):
	oneNote = vPares3.mkNote()
	sco.extend(oneNote)

vTodos4.strtNxt = vTodos.srtsMemo[4]
vTodos4.harmNo		= 14
vTodos4.distrs		= [.17, .17]
vTodos4.durMod		= .2
vTodos4.origin		= 211
vTodos4.step		= -4
vTodos4.ampModify	= 4
vTodos4.updateConfig()
for x in xrange(len(vTodos4.rythmAtms) + 1):
	oneNote = vTodos4.mkNote()
	sco.extend(oneNote)

vFibo4.strtNxt = vFibo.srtsMemo[4]
vFibo4.harmNo		= 14
vFibo4.distrs		= [.233, .233]
vFibo4.durMod		= .2
vFibo4.origin		= 211
vFibo4.step			= -4
vFibo4.ampModify	= 4
vFibo4.updateConfig()
for x in xrange(len(vFibo4.rythmAtms) + 1):
	oneNote = vFibo4.mkNote()
	sco.extend(oneNote)

vNones4.strtNxt = vNones.srtsMemo[4]
vNones4.harmNo		= 14
vNones4.distrs		= [.23, .23]
vNones4.durMod		= .2
vNones4.origin		= 211
vNones4.step		= -4
vNones4.ampModify	= 4
vNones4.updateConfig()
for x in xrange(len(vNones4.rythmAtms) + 1):
	oneNote = vNones4.mkNote()
	sco.extend(oneNote)

vPrimos4.strtNxt = vPrimos.srtsMemo[4]
vPrimos4.harmNo		= 14
vPrimos4.distrs		= [.31, .31]
vPrimos4.durMod		= 0.2
vPrimos4.origin		= 117
vPrimos4.step		= 4
vPrimos4.ampModify	= 4
vPrimos4.updateConfig()
for x in xrange(len(vPrimos4.rythmAtms) + 1):
	oneNote = vPrimos4.mkNote()
	sco.extend(oneNote)

vPares4.strtNxt = vPares.srtsMemo[4]
vPares4.harmNo		= 14
vPares4.distrs		= [.2, .2]
vPares4.durMod		= 0.2
vPares4.origin		= 70
vPares4.step		= -3
vPares4.ampModify	= 4
vPares4.updateConfig()
for x in xrange(len(vPares4.rythmAtms) + 1):
	oneNote = vPares4.mkNote()
	sco.extend(oneNote)

vTodos5.strtNxt = vTodos.srtsMemo[5]
vTodos5.harmNo		= 15
vTodos5.distrs		= [.18, .18]
vTodos5.durMod		= 0.166666667
vTodos5.origin		= 211
vTodos5.step		= 5
vTodos5.ampModify	= 5
vTodos5.updateConfig()
for x in xrange(len(vTodos5.rythmAtms) + 1):
	oneNote = vTodos5.mkNote()
	sco.extend(oneNote)

vFibo5.strtNxt = vFibo.srtsMemo[5]
vFibo5.harmNo		= 15
vFibo5.distrs		= [.377, .377]
vFibo5.durMod		= 0.166666667
vFibo5.origin		= 211
vFibo5.step			= 4
vFibo5.ampModify	= 5
vFibo5.updateConfig()
for x in xrange(len(vFibo5.rythmAtms) + 1):
	oneNote = vFibo5.mkNote()
	sco.extend(oneNote)

vNones5.strtNxt = vNones.srtsMemo[5]
vNones5.harmNo		= 15
vNones5.distrs		= [.25, .25]
vNones5.durMod		= 0.166666667
vNones5.origin		= 211
vNones5.step		= 4
vNones5.ampModify	= 5
vNones5.updateConfig()
for x in xrange(len(vNones5.rythmAtms) + 1):
	oneNote = vNones5.mkNote()
	sco.extend(oneNote)

vPrimos5.strtNxt = vPrimos1.srtsMemo[1]
vPrimos5.harmNo		= 15
vPrimos5.distrs		= [.37, .37]
vPrimos5.durMod		= 0.166666667
vPrimos5.origin		= 117
vPrimos5.step		= -4
vPrimos5.ampModify	= 5
vPrimos5.updateConfig()
for x in xrange(len(vPrimos5.rythmAtms) + 1):
	oneNote = vPrimos5.mkNote()
	sco.extend(oneNote)

vPares5.strtNxt = vPares.srtsMemo[5]
vPares5.harmNo		= 15
vPares5.distrs		= [.22, .22]
vPares5.durMod		= 0.166666667
vPares5.origin		= 70
vPares5.step		= 4
vPares5.ampModify	= 5
vPares5.updateConfig()
for x in xrange(len(vPares5.rythmAtms) + 1):
	oneNote = vPares5.mkNote()
	sco.extend(oneNote)

vTodos6.strtNxt = vTodos.srtsMemo[6]
vTodos6.harmNo		= 16
vTodos6.distrs		= [.19, .19]
vTodos6.durMod		= 0.142857143
vTodos6.origin		= 211
vTodos6.step		= -5
vTodos6.ampModify	= 6
vTodos6.updateConfig()
for x in xrange(len(vTodos6.rythmAtms) + 1):
	oneNote = vTodos6.mkNote()
	sco.extend(oneNote)

vFibo6.strtNxt = vFibo.srtsMemo[6]
vFibo6.harmNo		= 16
vFibo6.distrs		= [.610, .610]
vFibo6.durMod		= 0.142857143
vFibo6.origin		= 211
vFibo6.step			= -5
vFibo6.ampModify	= 6
vFibo6.updateConfig()
for x in xrange(len(vFibo6.rythmAtms) + 1):
	oneNote = vFibo6.mkNote()
	sco.extend(oneNote)

#####
#####
#####

tempo = tempo + str(vNones5.srtsMemo[0]) + ' 88 '
tempo = tempo + str(vNones5.srtsMemo[0]) + ' 77 '

vNones6.strtNxt = vNones5.srtsMemo[-1]
vNones6.harmNo		= 16
vNones6.distrs		= [.27, .27]
vNones6.durMod		= 0.166666667
vNones6.origin		= 211
vNones6.ampModify	= 6
vNones6.updateConfig()
for x in xrange(len(vNones6.rythmAtms) + 1):
	oneNote = vNones6.mkNote()
	sco.extend(oneNote)

vPrimos6.strtNxt = vPrimos5.srtsMemo[-1]
vPrimos6.harmNo		= 16
vPrimos6.distrs		= [.41, .41]
vPrimos6.durMod		= 0.166666667
vPrimos6.origin		= 117
vPrimos6.ampModify	= 6
vPrimos6.updateConfig()
for x in xrange(len(vPrimos6.rythmAtms) + 1):
	oneNote = vPrimos6.mkNote()
	sco.extend(oneNote)

vPares6.strtNxt = vPares5.srtsMemo[-1]
vPares6.harmNo		= 16
vPares6.distrs		= [.24, .24]
vPares6.durMod		= 0.166666667
vPares6.origin		= 70
vPares6.ampModify	= 6
vPares6.updateConfig()
for x in xrange(len(vPares6.rythmAtms) + 1):
	oneNote = vPares6.mkNote()
	sco.extend(oneNote)

#####
#####


vTodos7.strtNxt = vTodos1.srtsMemo[-1]
vTodos7.harmNo		= 17
vTodos7.distrs		= [.20, .20]
vTodos7.durMod		= 0.125
vTodos7.origin		= 211
vTodos7.ampModify	= 6
vTodos7.updateConfig()
for x in xrange(len(vTodos7.rythmAtms) + 1):
	oneNote = vTodos7.mkNote()
	sco.extend(oneNote)

vFibo7.strtNxt 		= vTodos1.srtsMemo[-1]
vFibo7.harmNo		= 17
vFibo7.distrs		= [.987, .987]
vFibo7.durMod		= 0.125
vFibo7.origin		= 211
vFibo7.ampModify	= 6
vFibo7.updateConfig()
for x in xrange(len(vFibo7.rythmAtms) + 1):
	oneNote = vFibo7.mkNote()
	sco.extend(oneNote)

vNones7.strtNxt 	= vTodos1.srtsMemo[-1]
vNones7.harmNo		= 17
vNones7.distrs		= [.29, .29]
vNones7.durMod		= 0.125
vNones7.origin		= 211
vNones7.ampModify	= 6
vNones7.updateConfig()
for x in xrange(len(vNones7.rythmAtms) + 1):
	oneNote = vNones7.mkNote()
	sco.extend(oneNote)

vPrimos7.strtNxt 	= vTodos1.srtsMemo[-1]
vPrimos7.harmNo		= 17
vPrimos7.distrs		= [.43, .43]
vPrimos7.durMod		= 0.125
vPrimos7.origin		= 117
vPrimos7.ampModify	= 6
vPrimos7.updateConfig()
for x in xrange(len(vPrimos7.rythmAtms) + 1):
	oneNote = vPrimos7.mkNote()
	sco.extend(oneNote)

vPares7.strtNxt = vTodos1.srtsMemo[-1]
vPares7.harmNo		= 17
vPares7.distrs		= [.26, .26]
vPares7.durMod		= 0.125
vPares7.origin		= 70
vPares7.ampModify	= 6
vPares7.updateConfig()
for x in xrange(len(vPares7.rythmAtms) + 1):
	oneNote = vPares7.mkNote()
	sco.extend(oneNote)

vTodos8.strtNxt = vTodos1.srtsMemo[-1]
vTodos8.harmNo		= 17
vTodos8.distrs		= [.21, .21]
vTodos8.durMod		= 0.125
vTodos8.origin		= 211
vTodos8.ampModify	= 7
vTodos8.updateConfig()
for x in xrange(len(vTodos8.rythmAtms) + 1):
	oneNote = vTodos8.mkNote()
	sco.extend(oneNote)

vFibo8.strtNxt 		= vTodos1.srtsMemo[-1]
vFibo8.harmNo		= 17
vFibo8.distrs		= [.987, .987]
vFibo8.durMod		= 0.125
vFibo8.origin		= 211
vFibo8.ampModify	= 7
vFibo8.updateConfig()
for x in xrange(len(vFibo8.rythmAtms) + 1):
	oneNote = vFibo8.mkNote()
	sco.extend(oneNote)

vNones8.strtNxt 	= vTodos1.srtsMemo[-1]
vNones8.harmNo		= 17
vNones8.distrs		= [.31, .31]
vNones8.durMod		= 0.125
vNones8.origin		= 211
vNones8.ampModify	= 7
vNones8.updateConfig()
for x in xrange(len(vNones8.rythmAtms) + 1):
	oneNote = vNones8.mkNote()
	sco.extend(oneNote)

vPrimos8.strtNxt 	= vTodos1.srtsMemo[-1]
vPrimos8.harmNo		= 17
vPrimos8.distrs		= [.47, .47]
vPrimos8.durMod		= 0.125
vPrimos8.origin		= 117
vPrimos8.ampModify	= 7
vPrimos8.updateConfig()
for x in xrange(len(vPrimos8.rythmAtms) + 1):
	oneNote = vPrimos8.mkNote()
	sco.extend(oneNote)

vPares8.strtNxt = vTodos1.srtsMemo[-1]
vPares8.harmNo		= 17
vPares8.distrs		= [.28, .28]
vPares8.durMod		= 0.125
vPares8.origin		= 70
vPares8.ampModify	= 7
vPares8.updateConfig()
for x in xrange(len(vPares8.rythmAtms) + 1):
	oneNote = vPares8.mkNote()
	sco.extend(oneNote)

vTodos9.strtNxt = vTodos1.srtsMemo[-1]
vTodos9.harmNo		= 18
vTodos9.distrs		= [.21, .21]
vTodos9.durMod		= 0.111111111
vTodos9.origin		= 211
vTodos9.ampModify	= 8
vTodos9.updateConfig()
for x in xrange(len(vTodos9.rythmAtms) + 1):
	oneNote = vTodos9.mkNote()
	sco.extend(oneNote)

vFibo9.strtNxt 		= vTodos1.srtsMemo[-1]
vFibo9.harmNo		= 18
vFibo9.distrs		= [.987, .987]
vFibo9.durMod		= 0.111111111
vFibo9.origin		= 211
vFibo9.ampModify	= 8
vFibo9.updateConfig()
for x in xrange(len(vFibo9.rythmAtms) + 1):
	oneNote = vFibo9.mkNote()
	sco.extend(oneNote)

tempo = tempo + str(vFibo9.srtsMemo[-1]) + ' 77 '



#####
#####
#####
vTodos.origin		= 159
vFibo.origin		= 160
vNones.origin		= 161
vPrimos.origin		= 162
vPares.origin		= 163

vTodos1.origin		= 164
vFibo1.origin		= 165
vNones1.origin		= 166
vPrimos1.origin		= 167
vPares1.origin		= 168

vTodos2.origin		= 169
vFibo2.origin		= 170
vNones2.origin		= 171
vPrimos2.origin		= 172
vPares2.origin		= 173

vTodos3.origin		= 174
vFibo3.origin		= 175
vNones3.origin		= 176
vPrimos3.origin		= 177
vPares3.origin		= 178

vTodos4.origin		= 179
vFibo4.origin		= 180
vNones4.origin		= 181
vPrimos4.origin		= 182
vPares4.origin		= 183

vTodos5.origin		= 184
vFibo5.origin		= 185
vNones5.origin		= 186
vPrimos5.origin		= 187
vPares5.origin		= 188

vTodos6.origin		= 189
vFibo6.origin		= 190
vNones6.origin		= 191
vPrimos6.origin		= 192
vPares6.origin		= 193

vTodos7.origin		= 194
vFibo7.origin		= 195
vNones7.origin		= 196
vPrimos7.origin	    = 197
vPares7.origin		= 198

vTodos8.origin		= 199
vFibo8.origin		= 200
vNones8.origin		= 201
vPrimos8.origin		= 202
vPares8.origin		= 203

vTodos9.origin		= 204
vFibo9.origin		= 205

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

pitchStepLst = [-1,-2, -3, -4, -5, -6, -7, -8, -9] + [1, 1 ,2, 3, 5, 8] * 2 + [2, 3, 5, 7] * 2


strtPitch = 112

import Numeric_utils as NumericUtils
Scaling		= NumericUtils.Scaling()
Series		= NumericUtils.Series(0)
primes		= Series.prime(47)
primes.reverse()
primes1 	= primes[24:]
primes2 	= [primes[23]]
primes3		= primes[:23]
primes3.reverse()
primes		= primes1 + primes2 + primes3
fibo		= Series.fibo(11)
fiboSet		= set(fibo)
amps		= range(47)
for x, y, z in zip(voiceLst, primes, amps):
	x.pitchSteps	 = random.sample(pitchStepLst, 12)
	strtPitch		 += 1
	x.harmNo		= 19

	x.ampModify	    = Scaling.valToRng(z, 0 , 46, 6, 18)
	x.step			= 0
	x.durMod		= y * .01
	x.updateConfig()

countDown = 100
for y in xrange(100):
	for x in voiceLst:
		x.countDown = countDown
		if x.origin > 53 and x.instrt % 2:
			x.origin -= random.choice(x.pitchSteps)
			if x.origin < 53:
				x.origin = 0
		elif x.origin < 400 and not x.instrt % 2:
			x.origin += random.choice(x.pitchSteps)
			if x.origin > 400:
				x.origin = 400
		if countDown in fiboSet:
			oldModify = x.ampModify
			x.ampModify += 6
			oneNote = x.mkNote2()
			x.ampModify = oldModify
		else:
			oneNote = x.mkNote2()
		sco.extend(oneNote)
		
		countDown -= 1



tempo = tempo + str(vPares7.srtsMemo[-1]) + ' 220 '

#####
#####
#####

sco.insert(0, tempo)

CsndCtrl	= CsndInterface.CsndCtrl(sco)
CsndCtrl.render()

