def timeDiff(timeList, n):
    #Finds the time-difference between two points
    return timeList[n+1]-timeList[n]

def secToHour(time):
    #Goes from seconds to a vector: [hr, min, sec]
    hr = time // 3600
    time = time - hr*3600
    min = time // 60
    sec = time - min*60
    vec = [hr,min,sec]
    for n in range(len(vec)):
        if (vec[n] < 10):
            vec[n] = "0"  + str(vec[n])
        else:
            vec[n] = str(vec[n])
    return vec

def timeVectorToString(time):
    #Goes from [hr,min,sec] to ex: 1h 23m 48s
    return time[0] + "h " + time[1]+ "m "+time[2]+"s "

def timeInZone(hrList, timeList,hrZone):
    #Goes throug the hr data and finds the time spent in each zone. Finds max hr
    zoneArray = [0,0,0,0,0,0]
    maxHr = 0
    for n in range(len(hrList)-1):
         if (hrList[n] > maxHr):
             maxHr = hrList[n]
         if (hrList[n] > hrZone[4]):
             zoneArray[5] += timeDiff(timeList,n)
         elif (hrList[n] >= hrZone[3]):
            zoneArray[4] += timeDiff(timeList,n)
         elif (hrList[n] >= hrZone[2]):
            zoneArray[3] += timeDiff(timeList,n)
         elif (hrList[n] >= hrZone[1]):
            zoneArray[2] += timeDiff(timeList,n)
         elif (hrList[n] >= hrZone[0]):
            zoneArray[1] += timeDiff(timeList,n)
         elif (hrList[n] < hrZone[0]):
            zoneArray[0] += timeDiff(timeList,n)
    return zoneArray, maxHr

def sufferScore(zoneArray):
    #Finds the "sufferScore" with the formula timeI1 + 2*timeI2 + 4*timeI3 + 8*timeI4 + 16*timeI5. Time in I0 is not added.
    return (zoneArray[1]//60)+(zoneArray[2]//60)*2+(zoneArray[3]//60)*4 + (zoneArray[4]//60)*8 + (zoneArray[5]//60)*16

def percentageInZone(time,totTime):
    #Finds percentage.
    return time/totTime *100
