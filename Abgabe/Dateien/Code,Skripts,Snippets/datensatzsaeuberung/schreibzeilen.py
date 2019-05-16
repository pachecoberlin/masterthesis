#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

def main(argv):
    f = open("filtered2.txt","a")
    for i in range(6330,6931):
        f.write("/home/pacheco/data/Master/bilddaten/second_selfmade/images/bike%07d.jpg\n" % i)
    for i in range(8250,9405):
        f.write("/home/pacheco/data/Master/bilddaten/second_selfmade/images/bike%07d.jpg\n" % i)
    for i in range(12260,12561):
        f.write("/home/pacheco/data/Master/bilddaten/second_selfmade/images/bike%07d.jpg\n" % i)
    f.close()   
    
if __name__ == "__main__":
    main(sys.argv)