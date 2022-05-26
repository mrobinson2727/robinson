from cmath import sqrt
import math
from pprint import pp
import itertools

# DEFINE SEA STATE ENVIRONMENT / VIGNETTE
calm = False     # Must be opposite of rough
rough = True   # Must be opposite of calm
# DEFINE ENEMY ENVIRONMENT / VIGNETTE 
permissive = True # Must be opposite of kinetic
kinetic = False   # Must be opposite of permissive


# STARTING NUMBER OF ASSETS
iterateThroughCH53s = [0, 4, 8, 12, 16] 
iterateThroughLAWs = [0, 1, 2, 3, 4]
iterateThroughPP = [10, 25, 50, 100]
# list of Force Design combinations
combinationOfTransport = [(f,s) for f in iterateThroughLAWs for s in iterateThroughCH53s] 
combinationOfAllinputs = [(f,s) for f in combinationOfTransport for s in iterateThroughPP]
#print(combinationOfAllinputs)


numOfCH53 = 0
numOfLAWs = 0

prePositioning = 0
distanceToDisplacement = 47

numOfLHDs = 0

#Natutical Miles away the prepositioning forces are
# a^2 + b^2 = c^2
aSquared = math.pow(prePositioning, 2)           
bSquared = math.pow(distanceToDisplacement, 2)
aSqPlusBSq = aSquared + bSquared

distanceBackToPrePositioning = math.pow(aSqPlusBSq, 0.5)


#Light Amphibious Warship (LAW)

if calm == True:    
    SoLAW = 15
    timeToLoadLAW = 0.1667

# Rough Environment reduces speed
# and doubles time to load
if rough == True:
    SoLAW = 15 * 0.67               
    timeToLoadLAW = 0.1667 * 2      

maxCapLAW = 10
totalMoveTimeLAW = 0
maxLawIterations = 4

#Amphibious Assault Ship (LHD)


if calm == True:    
    SoLHD = 19
    timeToLoadLHD = 0.1667

# Rough Environment reduces speed 33%
# and doubles time to load
if rough == True:   
    SoLHD = 15 * 0.67               
    timeToLoadLHD = 0.1667 * 2      

maxCapLHD = 30
speedToSwimToLHD = 5
distFromShoreLHD = 2
totalMoveTimeLHD = 0
maxLHDIterations = 4

#King Stallion Heavy Lift Helicopter CH-53

if calm == True:    
    SoCH53 = 170
    timeToLoadCH53 = 0.0833

# Rough Environment reduces speed 10%
# and doubles time to load / unload
if rough == True:
    SoCH53 = 170 * 0.90               
    timeToLoadCH53 = 0.0833 * 2      

maxCapCH53 = 1
timeToRefuel = 1

#Number of Ground Assets
numOfNMESIS = 6
numOfGATOR = 3
numOfJLTV = 10
numOfACV = 18
numOfMADIS = 3

#Enemy Capabilities 
if permissive == True:
    enJets = 2
    killsPerJet = 2
    numOfWaves = 12
    timeUntilFirstWave = 8
    timeUntilNextWave = 3
    enKillsPerWave = 0

if kinetic == True:
    enJets = 4
    killsPerJet = 2
    numOfWaves = 12
    timeUntilFirstWave = 2
    timeUntilNextWave = 2
    enKillsPerWave = 0

#Assign Serial Number to NMESIS
nmesisEAB1=[]
for i in range(numOfNMESIS):    
    nmesisEAB1.append('nmesis'+ str(i+1))
# print(nmesisEAB1)

#Assign Serial Number to GATOR
gatorEAB1=[]
for i in range(numOfGATOR):    
    gatorEAB1.append('gator'+ str(i+1))
# print(gatorEAB1)

#Assign Serial Number to JLTV
jltvEAB1=[]
for i in range(numOfJLTV):    
    jltvEAB1.append('jltv'+ str(i+1))
# print(jltvEAB1)

#Assign Serial Number to ACV
acvEAB1=[]
for i in range(numOfACV):    
    acvEAB1.append('acv'+ str(i+1))
# print(acvEAB1)

#Assign Serial Number to MADIS
madisEAB1=[]
for i in range(numOfMADIS):    
    madisEAB1.append('madis'+ str(i+1))
# print(madisEAB1)

GlobalEAB2 = []
EAB2List = []
nmesisEAB2 = []
gatorEAB2 = []
jltvEAB2 = []
acvEAB2 = []
madisEAB2 = []
assetsDestroyedOneIteration = []
assetsDestroyed = []



