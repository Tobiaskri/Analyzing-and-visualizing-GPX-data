import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

def plotHr(hr, time, hrZone):
    plt.plot(1,2);
    for i in range(len(hr)):
        if (hr[i] > hrZone[4]):              #Zone 5
            plt.plot(time[i], hr[i], 'ro')
        elif (hr[i] > hrZone[3]):           #Zone 4
            plt.plot(time[i],hr[i], 'go')
        elif (hr[i] > hrZone[2]):           #Zone 3
            plt.plot(time[i],hr[i])
        elif (hr[i] > hrZone[1]):          #Zone 2
            plt.plot(time[i],hr[i])
        elif (hr[i] > hrZone[0]):          #Zone 1
            plt.plot(time[i],hr[i])
        else:                                       #Zone 0
            plt.plot(time[i],hr[i])
    plt.show()
