import random

import Csnd_interface as CsndInterface
import ProcessIntro
import ProcessIntro2

scoData = open('scoData.py', 'a')
print 'Opened scoData'
scoStrings = open('scoStrings.py', 'a')
print 'Opened scoStrings'

# Defaults for ProcessIntro() and ProcessIntro2: initCll=(56, 24),
# strtCll=(0, 0), pitch=['(0.00)'], offset=0

voice1	= ProcessIntro.Process1(pitch1='0.00',
									distr1=0.618,
									pitch2='0.00',
									distr2=0.618)
offset1	= voice1.strts[len(voice1.strts) - 1]
scoData.write('# Part1Offsets:\n')
scoData.write('\noffset1 = ' + str(offset1))
offset2	= voice1.strts[len(voice1.strts)- 65]
scoData.write('\noffset2 = ' + str(offset2))
offset3	= voice1.strts[len(voice1.strts)- 33]
scoData.write('\noffset3 = ' + str(offset3))
offset4	= voice1.strts[len(voice1.strts)- 17]
scoData.write('\noffset4 = ' + str(offset4))
scoStrings.write('\np1Voice1 = ' + str(voice1.sco))
print 'Done writing'

#voice2	= ProcessIntro.Process1(strtCll=(112, 48),
#									pitch1='0.01',
#									distr1=0.618,
#									pitch2='0.03',
#									distr2=0.618,
#									offset=offset1,
#									instrt=2)
#voice3	= ProcessIntro.Process1(strtCll=(0, 48),
#									pitch1='0.02',
#									distr1=0.381924,
#									pitch2='0.02',
#									distr2=0.618,
#									offset=offset2,
#									instrt=3)
#voice4	= ProcessIntro.Process1(strtCll=(112, 0),
#									pitch1='0.03',
#									distr1=0.381924,
#									pitch2='0.01',
#									distr2=0.381924,
#									offset=offset3,
#									instrt=4)
#voice5	= ProcessIntro.Process1(strtCll=(0, 0),
#									pitch1='0.04',
#									distr1=0.381924,
#									pitch2='0.04',
#									distr2=0.618,
#									offset=offset4,
#									instrt=5)
#p1 = [voice1.sco + voice2.sco + voice3.sco + voice4.sco + voice5.sco]


#oldDistr2	= 1
#pitchVal	= 0.05
#vDistr1		= 0.618
#vOffset		= offset1

#for x in xrange(47):
#	vStrtCll =(random.randint(0, 112), random.randint(0, 48))
#	vPitch1	= str(pitchVal)
#	vPitch2	= str(pitchVal + 1)
#	vDistr2 = oldDistr2 * 0.618
#	vInstrt	= 6
#	voice	= ProcessIntro2.Process1(strtCll=vStrtCll,
#											pitch1=vPitch1,
#											distr1=vDistr1,
#											pitch2=vPitch2,
#											distr2=vDistr2,
#											offset=vOffset,
#											instrt=vInstrt)
#	p1.append(voice)
#	pitchVal	+= 0.01
#	oldDistr2	= vDistr2
#	vOffset		= voice.strts[1]


#CsndCtrl	= CsndInterface.CsndCtrl(p1)

#CsndCtrl	= CsndInterface.CsndCtrl(voice1.sco)

#CsndCtrl.render()

