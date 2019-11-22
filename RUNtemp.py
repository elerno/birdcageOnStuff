import random

import Csnd_interface as CsndInterface
import ProcessesAll
import ProcessIntro2

import scoData
scoData = open('scoData.py', 'w')



voice1	= ProcessesAll.Process1()
#CsndCtrl	= CsndInterface.CsndCtrl(sco)

CsndCtrl	= CsndInterface.CsndCtrl(voice1.sco)

CsndCtrl.render()

