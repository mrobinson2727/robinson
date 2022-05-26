import math
from pprint import pp
from tkinter import N
from start import *
from itertools import islice

#CONDA ACTIVATE THESIS


def moveToEAB1():
    global runningSimTimeCH53 
    global ch53IterationCounter
    global LAWIterationCounter
    global LHDIterationCounter
    global runningSimTimeLAW
    global runningSimTimeLHD
    global runningSimTimeEn
    global enIterationCounter
    global timeUntilNextWave
    CH53List=[]                                             
    LAWList=[]                                              
    LHDList=[]                                              

    if numOfCH53 == 0:
        runningSimTimeCH53 = 1000000
    if numOfLAWs == 0:
        runningSimTimeLAW = 1000000
    if numOfLHDs == 0:
        runningSimTimeLHD = 1000000    
# CH53 OPERATIONS
# read in number of assets from variables file
# create it into a list
# create space in list to calculate the how many assets transport asset can carry
# variable to place ground asset into list before split into nested list
    if numOfCH53 > 0 and runningSimTimeCH53 < runningSimTimeEn:  
        CH53List=[]                                         
        maxCapIterationCH53 = maxCapCH53 *numOfCH53         
        x = 1                                               
        for i in range(maxCapIterationCH53):    
            # pop from ground asset list from EAB1 to the logistical transport assets list
            if bool(nmesisEAB1) != False: 
                CH53List.insert(x, nmesisEAB1.pop(0))       
            elif bool(gatorEAB1) != False:
                CH53List.insert(x, gatorEAB1.pop(0))
            elif bool(jltvEAB1) != False:
                CH53List.insert(x, jltvEAB1.pop(0))
            elif bool(madisEAB1) != False:
                CH53List.insert(x, madisEAB1.pop(0))

        if bool(CH53List) != False:
            ch53IterationCounter += 1
            if ch53IterationCounter > 0:
                runningSimTimeCH53 = (CH53timeOneIteration*ch53IterationCounter) + CH53timeToEAB1
            
                #print('CH53 Time Iteration: ', runningSimTimeCH53)
                #print('\n CH53 iteration: ', ch53IterationCounter,': sim time: ', runningSimTimeCH53, ' transport load: \n', CH53List)
        else:
            runningSimTimeCH53 = 1000000

#LAW OPERATION
    if (runningSimTimeCH53 + CH53timeToEAB1) \
        > LAWtimeToEAB1 and numOfLAWs > 0 and LAWIterationCounter < maxLawIterations \
             and runningSimTimeLAW < runningSimTimeEn:

        # create space in list to calculate the how many assets transport asset can carry
        maxCapIterationLAWs = (maxCapLAW)*numOfLAWs        
        x = 1                                              
        for i in range(maxCapIterationLAWs):    
            # pop from ground asset list from EAB1 to the logistical transport assets list
            if bool(nmesisEAB1) != False: 
                LAWList.insert(x, nmesisEAB1.pop(0))       
            elif bool(gatorEAB1) != False:
                LAWList.insert(x, gatorEAB1.pop(0))
            elif bool(acvEAB1) != False:
                LAWList.insert(x, acvEAB1.pop(0))    
            elif bool(jltvEAB1) != False:
                LAWList.insert(x, jltvEAB1.pop(0))
            elif bool(madisEAB1) != False:
                LAWList.insert(x, madisEAB1.pop(0))
            
        # place ground asset in proper place depending on capacity of transport ship

        if bool(LAWList) != False:
            LAWIterationCounter += 1
            runningSimTimeLAW = (LAWtimeOneIteration*LAWIterationCounter)
            if LAWIterationCounter > 1:
                runningSimTimeLAW = (LAWtimeOneIteration) + (LAWafterFirstIter*(LAWIterationCounter - 1)) 
            #print('\n LAW iteration: ', LAWIterationCounter,': ', LAWList)
        else:
            pass

# LHD OPERATION
    if (runningSimTimeCH53 + CH53timeToEAB1) \
        > LHDtimeToEAB1 and numOfLHDs > 0 and LHDIterationCounter < maxLHDIterations \
            and runningSimTimeLHD < runningSimTimeEn:

        maxCapIterationLHDs = (maxCapLHD)*numOfLHDs        
        x = 1                                              
        for i in range(maxCapIterationLHDs):    
            if bool(acvEAB1) != False:
                LHDList.insert(x, acvEAB1.pop(0))

        if bool(LHDList) != False:
            LHDIterationCounter += 1
            runningSimTimeLHD = (LHDtimeOneIteration * LHDIterationCounter)
            if LHDIterationCounter > 1:
                runningSimTimeLHD = (LHDtimeOneIteration) + (LHDafterFirstIter*(LHDIterationCounter-LHDIterationCounter)) 
            #print('\n LHD iteration: ', LHDIterationCounter,': ', LHDList)
        else:
            pass
        
     # Add transportation List to EAB 2 Global List. Then clear transportation list for next iteration   
    if bool(CH53List) != False: 
        GlobalEAB2.extend(CH53List)
        CH53List.clear()

    if bool(LAWList) != False: 
        GlobalEAB2.extend(LAWList)
        LAWList.clear()

    if bool(LHDList) != False:
        GlobalEAB2.extend(LHDList)
        LHDList.clear()

# ENEMY OPERATIONS
    if enJets > 0 and runningSimTimeEn < runningSimTimeCH53 and \
         runningSimTimeEn < runningSimTimeLAW and runningSimTimeEn < runningSimTimeLHD:
            # create space in list to calculate the how many assets transport asset can carry
        enKillsPerWave = (killsPerJet) * enJets       
        x = 1                                               
        for i in range(enKillsPerWave):    
            # pop from ground asset list from EAB1 to the logistical transport assets list
            if bool(nmesisEAB1) != False: 
                assetsDestroyedOneIteration.insert(x, nmesisEAB1.pop(0))       
            elif bool(gatorEAB1) != False:
                assetsDestroyedOneIteration.insert(x, gatorEAB1.pop(0))
            elif bool(jltvEAB1) != False:
                assetsDestroyedOneIteration.insert(x, jltvEAB1.pop(0))
            elif bool(madisEAB1) != False:
                assetsDestroyedOneIteration.insert(x, madisEAB1.pop(0))
            elif bool(acvEAB1) != False:
                assetsDestroyedOneIteration.insert(x, acvEAB1.pop(0))

        if bool(assetsDestroyedOneIteration) != False:
            enIterationCounter += 1
            #print('\n ENEMY KILLS iteration: ', enIterationCounter,': ', assetsDestroyedOneIteration)
            #print('Time of EN attack: ', runningSimTimeEn)
            assetsDestroyed.extend(assetsDestroyedOneIteration)
            assetsDestroyedOneIteration.clear()

            runningSimTimeEn = timeUntilFirstWave + (timeUntilNextWave * enIterationCounter)
        else: 
            pass


    # If no EN or CH53 and LAW/LHD are not making return trips
    if numOfCH53 == 0 and LAWIterationCounter == maxLawIterations and \
         LHDIterationCounter == maxLHDIterations and enJets == 0:

        assetsDestroyed.extend(nmesisEAB1)
        assetsDestroyed.extend(gatorEAB1)
        assetsDestroyed.extend(jltvEAB1)
        assetsDestroyed.extend(acvEAB1)
        assetsDestroyed.extend(madisEAB1)
        nmesisEAB1.clear()
        gatorEAB1.clear()
        jltvEAB1.clear()
        acvEAB1.clear()
        madisEAB1.clear()

        #print('\n Assets destroyed: \n', assetsDestroyed)
            
    return 

# Keep running Move to EAB1 Function until all ground assets are either displaced to EAB2 or destroyed


### START HERE ####

# ITERATE THROUGH DIFFERENT FORCE DESIGNS
# THIS RUNS THROUGH 100 scenarios (25 force design combos, 4 distances)
# COMBINATION OF ALL INPUTS INCLUDES LAW, CH53, AND PREPOSITIONING DISTANCE
#  #COMBINATIONOFTRANSPORT IS JUST LAW AND CH53s
g = 0                                               
while g < len(combinationOfAllinputs):              
                                                
    numOfLAWs = combinationOfAllinputs[g][0][0]
    numOfCH53 = combinationOfAllinputs[g][0][1] 
    prePositioning = combinationOfAllinputs[g][1]
    g = g +1

# z = 0                                         # THIS RUNS THROUGH 25 scenarios (25 force design combos, 1 distance)
# while z < len(combinationOfTransport):        #COMBINATIONOFTRANSPORT IS JUST LAW AND CH53s
    # numOfLAWs = combinationOfTransport[z][0]
    # numOfCH53 = combinationOfTransport[z][1] 
    # z = z + 1    

    # ALL TIME CALCULATIONS
    if g <10000:
    #  CALCULATING CH53 EAB ITERATION
        # calculate time from prePos to EAB1
        CH53timeToEAB1 = prePositioning / SoCH53                  
        #print(CH53timeToEAB1)
        CH53timeToLoadEAB1 = timeToLoadCH53 * maxCapCH53          
        #print(CH53timeToLoadEAB1)
        # calculate time from EAB1 to EAB2
        CH53timeToEAB2 = distanceToDisplacement / SoCH53          
        #print(CH53timeToEAB2)
        CH53timeToUnloadEAB2 = timeToLoadCH53 * maxCapCH53        
        #print(CH53timeToUnloadEAB2)
        # calculate time from EAB2 to PrePos for refueling
        CH53timeToPrePos = distanceBackToPrePositioning / SoCH53  
        #print(CH53timeToPrePos)
        # add all times together for ONE interation plue time to refuel 
        CH53timeOneIteration = \
            CH53timeToEAB1 + CH53timeToLoadEAB1 + \
                CH53timeToEAB2 + CH53timeToUnloadEAB2 + CH53timeToPrePos + timeToRefuel   
        #print(CH53timeOneIteration)
        #  CALCULATING CH53 EAB ITERATION UP TO 10 ITERATIONS 
        #  WHEN IT RETURNS FOR NEXT EAB1 PICK UP       
        CH53timeOneIterationPlusReturnToEAB1SecondTime = \
            CH53timeOneIteration + CH53timeToEAB1

        #  CALCULATING LAW EAB ITERATION
        # calculate time from prePos to EAB1
        LAWtimeToEAB1 = prePositioning / SoLAW                  
        LAWtimeToLoadEAB1 = timeToLoadLAW * maxCapLAW  
        # calculate time from EAB1 to EAB2        
        LAWtimeToEAB2 = distanceToDisplacement / SoLAW          
        LAWtimeToUnloadEAB2 = timeToLoadLAW * maxCapLAW           
        # calculate time from EAB2 to PrePos for refueling
        LAWtimeToPrePos = distanceBackToPrePositioning / SoLAW  

        # add all times together for ONE interation ENDS AT EAB2 DOES NOT RETURN TO PREPOS
        LAWtimeOneIteration = LAWtimeToEAB1 + LAWtimeToLoadEAB1 \
            + LAWtimeToEAB2  + LAWtimeToUnloadEAB2              

        LAWafterFirstIter = LAWtimeToEAB2 + LAWtimeToLoadEAB1 \
            + LAWtimeToEAB2  + LAWtimeToUnloadEAB2

        #  CALCULATING LHD EAB ITERATION
        # calculate time from prePos to EAB1
        LHDtimeToEAB1 = prePositioning / SoLHD                  
        #Time it takes for ACV to swim plus Load Time
        LHDtimeToLoadEAB1 = (distFromShoreLHD/speedToSwimToLHD)  + timeToLoadLHD 
        # calculate time from EAB1 to EAB2
        LHDtimeToEAB2 = distanceToDisplacement / SoLHD          
        # #Time it takes for ACV to swim plus Load Time
        LHDtimeToUnloadEAB2 = (distFromShoreLHD/speedToSwimToLHD) + timeToLoadLHD 
        # calculate time from EAB2 to PrePos for refueling
        LHDtimeToPrePos = distanceBackToPrePositioning / SoLHD  
        # add all times together for ONE interation. ENDS AT EAB2 DOES NOT RETURN TO PREPOS
        LHDtimeOneIteration = LHDtimeToEAB1 + LHDtimeToLoadEAB1 \
            + LAWtimeToEAB2 + LHDtimeToUnloadEAB2                

        LHDafterFirstIter = LHDtimeToEAB2 + LHDtimeToLoadEAB1 \
            + LAWtimeToEAB2 + LHDtimeToUnloadEAB2

        runningSimTimeCH53 = CH53timeToEAB1
        runningSimTimeLAW = LAWtimeToEAB1
        runningSimTimeLHD = LHDtimeToEAB1
        runningSimTimeEn = timeUntilFirstWave
        ch53IterationCounter = 0
        LAWIterationCounter = 0
        LHDIterationCounter = 0
        enIterationCounter = 0

    while True: 
        if bool(nmesisEAB1) == False and bool(gatorEAB1) == False and bool(jltvEAB1) \
            == False and bool(madisEAB1) == False and bool(acvEAB1) == False:
            # add this if need LHD # and runningSimTimeCH53 > runningSimTimeLHD
            print('LAWs / CH53Ks / PP Dist: ', numOfLAWs, '/ ', numOfCH53, '/ ', prePositioning) 
            if runningSimTimeCH53 > runningSimTimeLAW and runningSimTimeCH53 != 1000000: 
                    print(' Running Sim Time CH53 LAST: ', runningSimTimeCH53 - CH53timeToPrePos - timeToRefuel - CH53timeToEAB1)
            # add this if need LHD # and runningSimTimeLAW > runningSimTimeLHD
            elif runningSimTimeCH53 < runningSimTimeLAW and runningSimTimeLAW != 1000000:  
                    print(' Running Sim Time  LAW LAST: ', runningSimTimeLAW)
            #    elif runningSimTimeLHD > runningSimTimeLAW and runningSimTimeCH53 < runningSimTimeLHD:
            #         print('\n Running Sim Time LHD LAST: \n', runningSimTimeLHD)
            elif runningSimTimeLAW == 1000000 and runningSimTimeCH53 == 1000000:
                print(' EN Destroyed Remaining Ground Assets at Sim Time: ', runningSimTimeEn - timeUntilNextWave)
            elif runningSimTimeCH53 == 1000000 and runningSimTimeLAW != 1000000 and (runningSimTimeLAW > runningSimTimeEn or runningSimTimeLAW < timeUntilFirstWave):
                print(' Running Sim Time  LAW LAST: ', runningSimTimeLAW)    
            else:
                print(' Sim Time: ', runningSimTimeEn - timeUntilNextWave)

            
            print(' EAB2 Final Assets: ', len(GlobalEAB2)) #, GlobalEAB2)
            print(' TOTAL ASSETS DESTROYED: ', len(assetsDestroyed)) #, assetsDestroyed)
            print(' CH53 Iterations: ', ch53IterationCounter)
            print(' LAW Iterations: ', LAWIterationCounter)
            #print('\n XXXXXXXXXXXXX END OF STATS XXXXXXXXXXXXXXXXXX \n \n') 

            # RESET ALL STATE VARIABLES TO BEGIN NEW RUN ###
            GlobalEAB2 = []
            assetsDestroyedOneIteration = []
            assetsDestroyed = []
            runningSimTimeCH53 = CH53timeToEAB1
            runningSimTimeLAW = LAWtimeToEAB1
            runningSimTimeLHD = LHDtimeToEAB1
            runningSimTimeEn = timeUntilFirstWave
            ch53IterationCounter = 0
            LAWIterationCounter = 0
            LHDIterationCounter = 0
            enIterationCounter = 0


            #Assign Serial Number to NMESIS
            nmesisEAB1=[]
            for i in range(numOfNMESIS):    
                nmesisEAB1.append('nmesis'+ str(i+1))

            #Assign Serial Number to GATOR
            gatorEAB1=[]
            for i in range(numOfGATOR):    
                gatorEAB1.append('gator'+ str(i+1))

            #Assign Serial Number to JLTV
            jltvEAB1=[]
            for i in range(numOfJLTV):    
                jltvEAB1.append('jltv'+ str(i+1))

            #Assign Serial Number to ACV
            acvEAB1=[]
            for i in range(numOfACV):    
                acvEAB1.append('acv'+ str(i+1))

            #Assign Serial Number to MADIS
            madisEAB1=[]
            for i in range(numOfMADIS):    
                madisEAB1.append('madis'+ str(i+1))


            break

        moveToEAB1()




