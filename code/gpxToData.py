from xml.dom import minidom
import sys

#-----GPXdata object-----
class gpxData:
    def __init__(self, filename):
            self.lon = []
            self.lat = []
            self.elevation = []
            self.hr = []
            self.cad = []
            self.time = []
            self.filename = filename

    def parseFile(self):
        #Read file
        data = readFile(self.filename)
        #Define different parts
        coordinates = data.getElementsByTagName('trkpt')
        elevation = data.getElementsByTagName('ele')
        timenodes = data.getElementsByTagName('time')
        hrnodes = data.getElementsByTagName('gpxtpx:hr')
        cadnodes = data.getElementsByTagName('gpxtpx:cad')
        #Parsing the data:
        try:
            for i in range(len(coordinates)):
                self.lon.append(float(coordinates[i].attributes['lon'].value))
                self.lat.append(float(coordinates[i].attributes['lat'].value))
                self.elevation.append(float(elevation[i].firstChild.nodeValue))
                self.hr.append(int(hrnodes[i].firstChild.nodeValue))
                #self.cad.append(int(cadnodes[i].firstChild.nodeValue))
                t = timenodes[i].firstChild.nodeValue
                t = t.split('T')
                t = t[1][0:8].split(':')
                self.time.append(toSec(t))
        except:
            print('File error \nDid you use an heart rate sensor during the activity?')
            sys.exit(0)

        fixTime(self.time)

#-----Functions-----
def toSec(time):
    return 3600*(int(time[0])) + 60*(int(time[1])) + int(time[2])

def readFile(filename):
#Reading the file
    try:
        f = open(filename, 'r')
        data = minidom.parse(f)
        f.close()
        return data
    except:
        print("File error")
        sys.exit(0)

def fixTime(data):
#Defines time as seconds from start
    totalTime = 0
    lastTime = data[0]
    for t in range(1,len(data)):
        var = data[t] - lastTime
        lastTime = data[t]
        if (var < 20):
            totalTime += var
        data[t] = totalTime
    data[0] = 0
    return data
