#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse 
import sys
import matplotlib.pyplot as plt
import numpy as np
from pylab import * 

def main(argv):
 #   f = open("schlechte.txt")
    f = open("gute.txt")
    lines  = [line.rstrip("\n") for line in f.readlines()]
    goodones = {}    
    for line in lines:
        goodones[line]=1
    f.close()
#    f = open("gute.txt")
    f = open("schlechte.txt")
    lines  = [line.rstrip("\n") for line in f.readlines()]
    for line in lines:
        goodones[line]=0
    f.close()
#    f = open("filtered.txt","w+")
    f = open("final.txt","w+")
    for line,good in goodones.items():
        if good==1:
            f.write("%s\n" % line)
    f.close()
    
if __name__ == "__main__":
    main(sys.argv)