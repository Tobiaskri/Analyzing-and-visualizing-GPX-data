import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

from Code.gpxToData import gpxData
from Code.hrAnalysis import *
#from printGraph import printGraph
from Code.gpsAnalysis import *
from Code.dataPlot import *

#Variables
maxHr = 195
hrZone = [60,72,82,87,92] #%

#GPX-file
filename = input("Filename: ")
if (filename[len(filename)-4:len(filename)] != ".gpx"):
    filename = filename + ".gpx"

#Parsing through the file
data = gpxData(filename)
data.parseFile()

#Going from percentage to hr-values
for i in range(len(hrZone)):
  hrZone[i] = int(hrZone[i] * maxHr / 100)

#finds time in each zone and max hr
timeInZoneArray, maxHrVar = timeInZone(data.hr, data.time, hrZone)

#Finds total time
totTime = 0
for n in timeInZoneArray:
  totTime += n
totTimeHr = secToHour(totTime)
print("Total time:\t", timeVectorToString(totTimeHr))

#Prints time and percentage in each zone
print("Time in zone and percentage:  ")
print("-----------------------------------")
for n in range(len(timeInZoneArray)):
    time = secToHour(timeInZoneArray[n])
    percentage = percentageInZone(timeInZoneArray[n],totTime)
    print("Zone", str(n),  timeVectorToString(time),"%.1f" % percentage, "%")
print("-----------------------------------")

print("More data:")
#Prints sufferScore
sScore = sufferScore(timeInZoneArray)
print("SufferScore:  \t " + str(sScore))

#Prints average hr
avHr = 0
for n in data.hr:
    avHr +=  n/  len(data.hr)

print("Average hr:\t", "%.1f" % avHr)

#pritns max hr
print("Max hr:\t\t", maxHrVar)

#plots graphs
#printGraph(data.hr, data.elevation, data.time,hrZone,avHr)

ang = findDistanceVector(data.lat,data.lon)

d = 0
for n in ang:
    d += n

print("distance: ",d)

#plt.plot(data.lon,data.lat)
#plt.show()

print(hrZone);

plotHr(data.hr, data.time, hrZone);
