import random

import Csnd_interface as CsndInterface
import ProcessIntro
import ProcessIntro2
import scoData

#voice1	= ProcessInt	ro.Process1(pitch1='0.00',
#									distr1=0.618,
#									pitch2='0.00',
#									distr2=0.618)
#offset1	= voice1.strts[len(voice1.strts) - 1]
#scoData.write('\noffset1 =' + str(offset1))
#offset2	= voice1.strts[len(voice1.strts)- 65]
#scoData.write('\noffset1 =' + str(offset2))
#offset3	= voice1.strts[len(voice1.strts)- 33]
#scoData.write('\noffset1 =' + str(offset3))
#offset4	= voice1.strts[len(voice1.strts)- 17]
#scoData.write('\noffset1 =' + str(offset4))
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
#p1 = voice1.sco + voice2.sco + voice3.sco + voice4.sco + voice5.sco
#############################################################################

# Only first Time:
#oldDistr2	= 1
#vOffset		= 0
#vInstrt		= 6

# Copy from scoData after the first time.
vOffsets = [1, 4.9577715409940808, 8.6544771558097864, 12.107337499329645, 15.332437302806007, 18.344800302631292, 21.158459226592377, 23.786521163631512, 26.241228621630924, 28.534016557651398, 30.675565646293265, 32.675852034323995, 34.544193813348286, 36.289294427008038, 37.919283214919218, 39.441753282214833, 40.863796871104483, 42.192038399224785, 43.432665318685736, 44.591456939566129, 45.673811352128808, 46.684770573169658, 47.629044033641485, 48.511030516967125, 49.334838650238638, 50.104306043758456, 50.823017168081684, 51.494320051837533, 52.121341878114784, 52.707003552064997, 53.254033307585026, 53.764979416463817, 54.242222059197573, 54.687984412771989, 55.104343007062681, 55.49323739809784, 55.85647920324481, 56.19576054040995, 56.512661910564709, 56.808659560317793, 57.085132358830982, 57.343368221113927, 57.584570107620081, 57.809861628092101, 58.020292275761598, 58.216842316286105, 58.400427354197795]
# Not first time:
oldDistr2	= scoData.oldDistr2
vInstrt		= scoData.vInstrt
vOffset = vOffsets[vInstrt - 6] - 1

# Constants
shrinkFact	= 0.618
p1			= []
p2			= []



vStrtCll =(random.randint(0, 112), random.randint(0, 48))
pitchPrts = divmod(vInstrt - 1, 47)
if pitchPrts[1] < 10:
	vPitch1	= ''.join([str(pitchPrts[0]), '.0', str(pitchPrts[1])])
	vPitch2	= ''.join([str(pitchPrts[0] + 1), '.0', str(pitchPrts[1])])
else:
	vPitch1	= ''.join([str(pitchPrts[0]), '.', str(pitchPrts[1])])
	vPitch2	= ''.join([str(pitchPrts[0] + 1), '.', str(pitchPrts[1])])
vDistr2 = oldDistr2 * 0.618
print 'Cell= ', vStrtCll, '\npitch1= ', vPitch1, '\ndistor1= ', shrinkFact, '\npitch2= ', vPitch2, '\ndistor2= ', vDistr2, '\noffset= ', vOffset, '\ninstr= ', vInstrt
voice	= ProcessIntro2.Process1(initCll=vStrtCll,
									strtCll=vStrtCll,
									pitch1=vPitch1,
									distr1=shrinkFact,
									pitch2=vPitch2,
									distr2=vDistr2,
									offset=vOffset,
									instrt=vInstrt)
p1.extend(voice.silentSpec)
p2.extend(voice.prtlsStmnts)
oldDistr2	= vDistr2
vInstrt		+= 1

scoData = open('scoData.py', 'w')
scoData.write('\noldDistr2 = ' + str(oldDistr2))
scoData.write('\nvInstrt = ' + str(vInstrt))
scoData.write('\nvOffsets = ' + str(voice.strts))

sco = p1 + p2


#CsndCtrl	= CsndInterface.CsndCtrl(voice1.sco)
CsndCtrl	= CsndInterface.CsndCtrl(sco)

CsndCtrl.render()

