import sys
import math
import random
import os
import timeit

class Point :
    def __init__(self, x_val, y_val):
        self.x = x_val
        self.y = y_val

    def __repr__(self):
        return "(%.2f, %.2f)" % (self.x, self.y)

def Read_Points_From_Command_Line_File():
    points = []
    number_of_args = len(sys.argv)
    file = open(sys.argv[1],"r")

    for line in file:
        line.strip()
        x_y = line.split(" ")
        points.append(Point(float(x_y[0]),float(x_y[1])))

    return points

def Write_to_File(filename, s):
    output = open(filename ,'w')
    output.write(str(s))
    output.write('\n')
    
def distanceCalculator(f, s):
    return ((((f.x - s.x) * (f.x - s.x)) + ((f.y - s.y) * (f.y - s.y)))**(0.5))
    
def cutDownList(oldList, left, right, length):
    newList = []
    for i in range(0, length):
        if (oldList[i].x >= left) and (oldList[i].x <= right):
                newList.append(oldList[i])

    return newList
   
def bruteForce2(lengthList, lists, distanceSmall):
    for i in range(0, lengthList):
        for j in range(i + 1, i + 8):
            if(j < lengthList):
                tempVal = distanceCalculator(lists[i], lists[j])
                if tempVal < distanceSmall: 
                    distanceSmall = tempVal

    return distanceSmall
    
def bruteForce(lengthList, lists, distanceSmall):
    distanceSmall = 1e900
    for i in range(0, lengthList):
        for j in range(i + 1, lengthList):
            tempVal = distanceCalculator(lists[i], lists[j])
            if tempVal < distanceSmall:
                distanceSmall = tempVal

    return distanceSmall
    
def divide_and_conquer(lengthList):
    length = len(lengthList)
    midSection = length / 2
    if length < 2:
        return 1e900
    elif length == 2:
        return distanceCalculator(lengthList[0], lengthList[1])
    else:  
        left = lengthList[:midSection]
        right = lengthList[midSection:]
        minimum = min(divide_and_conquer(left), divide_and_conquer(right))
        newLeft = midSection - minimum
        newRight = midSection + minimum
        smallerList = cutDownList(lengthList, newLeft, newRight, length)
        smallerList = sorted(smallerList, key=lambda Point: Point.y)
        tempMin = bruteForce2(len(lengthList), lengthList, minimum)
        if tempMin < minimum:
            minimum = tempMin
        return minimum 

list1 = Read_Points_From_Command_Line_File()
name = sys.argv[1].replace(".txt", "_distance.txt")
lengthList = len(list1)
list1 = sorted(list1, key=lambda Point: Point.x)
smallestDistance = bruteForce(lengthList, list1, 1e900)
minDistance = divide_and_conquer(list1)
Write_to_File(name, smallestDistance)
