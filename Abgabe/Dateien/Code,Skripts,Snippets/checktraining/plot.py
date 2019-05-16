#!/usr/bin/python
# -*- coding: utf-8 -*-
#by Alexander Wachtberger
import argparse 
import sys
import matplotlib.pyplot as plt
import numpy as np
from pylab import * 

def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument(   
        "-all",  dest='all', 
        action='store_const',
        const=True,
        default=False,
        help = "all values starting from 2000"
        )
    parser.add_argument(   
        "-ALL",  dest='ALL', 
        action='store_const',
        const=True,
        default=False,
        help = "all values"
        )
    parser.add_argument(   
        "-def",  dest='default', 
        action='store_const',
        const=True,
        default=False,
        help = "default values"
        )
    parser.add_argument(   
        "-i",  dest='mod', 
        default=500, type=int,
        help = "mean is calculated over i values"
        )
    parser.add_argument(   
        "-f",  dest='file', 
        default="data\loss.txt", 
        help = "path to log file"
        )
    params = parser.parse_args()
    f = open(params.file)
    lines  = [line.rstrip("\n") for line in f.readlines()]
    numbers = {'1','2','3','4','5','6','7','8','9'}
    iters = []
    loss = []
    avgloss = []
    fig,ax = plt.subplots()   
#    fig.suptitle("Fehler Zerfall Kurve")
    prev_line = ""
    avglossdict = {}    
    meanAvglossX = []
    meanAvgloss = []
    i=0
    counter = 0.0
    highest = 0.0
    lowest = 2000.0
    for line in lines:
        args = line.split(' ')
        if args[0][-1:]==':' and args[0][0] in numbers :
            i += 1
            iters.append(int(args[0][:-1]))            
            loss.append(float(args[1][:-1]))
            avgloss.append(float(args[2]))
            avglossdict[int(args[0][:-1])] = float(args[2]) 
            lowest = float(args[2]) if float(args[2])<lowest else lowest
            #avg line
            counter += float(args[2])
            if i%params.mod == 0:
                meanAvgloss.append(counter/i)
                meanAvglossX.append(int(args[0][:-1]))
                highest= counter/i if counter/i>highest else highest
                counter=0.0
                i=0
#    print("104500 %f" % avglossdict[104500])
#    print(f"{avglossdict[107000]}")
#    print(f"{avglossdict[109500]}")
#    print(f"{avglossdict[112500]}")
#    print(f"95044 {avglossdict[115000]}")
#    print(f"{avglossdict[97548]}")
#    for i in range(10000,10020):
#        print(f"{i} {avglossdict[i]}")
    
    meanAvgloss.append(counter/i)
    meanAvglossX.append(int(args[0][:-1]))
    highest= counter/i if counter/i>highest else highest
    ticks = np.arange(0, 0.3, 0.01)
    ax.set_yticks(ticks)
   # ax.plot(iters,loss)
#    ax.plot(iters,avgloss)
    line1, = ax.plot(avglossdict.keys(),avglossdict.values())
    line2, = ax.plot(meanAvglossX,meanAvgloss)
    legend((line1, line2), ('Durchschnittliche Fehlerkurve', f"Ausgleichskurve des Fehlers"))
    #plt.plot(iters,avgloss)
    #Achsengröße [xvon,xbis,yvon,ybis] 
    if params.all:
        plt.axis([2000, iters[len(iters)-1]+100, 0, 0.3])    
    elif params.ALL:
        plt.axis([0, iters[len(iters)-1]+100, 0, 0.3])
    elif params.default:
        wtf=0    
    else:
        plt.axis([iters[len(iters)-1]-3000, iters[len(iters)-1]+100,lowest-0.01, lowest+avgloss[len(avgloss)-1000]])
  #  plt.axis([100, iters[len(iters)-1]+100, 0, 10])
    plt.xlabel('Anzahl der Iterationen')
    plt.ylabel('Fehler in Prozent')
    plt.grid()
    plt.show()
    
if __name__ == "__main__":
    main(sys.argv)