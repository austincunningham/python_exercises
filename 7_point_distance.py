#!/usr/bin/python3

import math

def point_distance(x0,y0,x1,y1):
    distance = math.sqrt((math.pow((x0-x1),2)) + (math.pow((y0-y1),2)))
    print("Distance between x0,y0 and x1,y1 is %1.2f"%distance)

def main():
    print("Enter x0")
    x0 = input(">")
    print("Enter y0")
    y0 = input(">")
    print("Enter x1")
    x1 = input(">")
    print("Enter y1")
    y1 = input(">")
    point_distance(x0,y0,x1,y1)

if __name__=='__main__':
    main()

