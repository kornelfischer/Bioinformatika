#ID: HAMM
import sys, os
dn=os.path.dirname(__file__)
pdn=os.path.join(dn,"..")
sys.path.append(pdn)
import utils

inFile = sys.argv[1]

utils.hamm(inFile)