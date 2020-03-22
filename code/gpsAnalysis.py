import numpy as np

def toRad(t):
    return t*np.pi/180

def findDistanceVector(lat,lon):
    #Defines a vector with the distance between points
    #Uses formula from janmatuschek.de/latitudelongitudeboundingcoordinates for distance betveen to points:
    #dist = arccos[sin(lat1)*sin(lat2)+cos(lat1)*cos(lat1)*cos(lon1-lon2))]*R            Using R = 6371 km
    distanceVector = []
    R = 6371000 #m
    for n in range(len(lat)-1):
        lat1 = toRad(lat[n])
        lat2 = toRad(lat[n+1])
        lon1 = toRad(lon[n])
        lon2 = toRad(lon[n+1])

        distance = np.arccos(np.sin(lat1) * np.sin(lat2) + np.cos(lat1) * np.cos(lat2) * np.cos(lon1-lon2))*R

        distanceVector.append(distance)
    return distanceVector
