import sys
import math
from decimal import *
from operator import attrgetter

class Point :
    def __init__(self, x_val, y_val):
        self.energy = x_val # holds the value of the seam
        self.minSeam = y_val # will hold the value of the minSeam
        
    def __repr__(self):
        return "(%.2f, %.2f)" % (self.energy, self.minSeam)

def READ_FROM_FILE():
    i = 0
    points = []
    file = open(sys.argv[1],"r")
    
    for line in file:
        x_y = line.split(", ")
        points.append([])
        for j in range(0, len(x_y)):
            points[i].append(Point(Decimal(x_y[j]), Decimal(0)))
            if i == 0:  points[i][j].minSeam = points[i][j].energy
        i = i + 1
        
    return points

def SeamCarving(list1):
    index = 0
    for rows in range(1, len(list1)):
        for cols in range(0, len(list1[rows])):
            if cols == 0:   
                list1[rows][cols].minSeam = list1[rows][cols].energy + min(list1[rows-1][cols].minSeam, list1[rows-1][cols+1].minSeam)
            elif cols == len(list1[rows]) - 1:  
                list1[rows][cols].minSeam = list1[rows][cols].energy + min(list1[rows-1][cols-1].minSeam, list1[rows-1][cols].minSeam)
            else:   
                list1[rows][cols].minSeam = list1[rows][cols].energy + min(list1[rows-1][cols-1].minSeam, list1[rows-1][cols].minSeam, list1[rows-1][cols+1].minSeam)
    minSeam = list1[len(list1) - 1][0].minSeam
    for i in range(0, len(list1)):
        if list1[len(list1) - 1][i].minSeam < minSeam:
            minSeam = list1[len(list1) - 1][i].minSeam
            index = i
    return minSeam, index
        
def traceBack(list1, index, minSeam, name):
    indexList = []
    otherList = []
    for i in range((len(list1)-1), -1, -1):
        if index == 0:
            value = min(list1[i][index].minSeam, list1[i][index+1].minSeam)
            if list1[i][index+1] == value:
                index = index + 1
        elif index == len(list1[i]) - 1:
            value = min(list1[i][index-1].minSeam, list1[i][index].minSeam)
            if list1[i][index-1].minSeam == value:
                index = index - 1
        else:
            value = min(list1[i][index-1].minSeam, list1[i][index].minSeam, list1[i][index+1].minSeam)
            if list1[i][index+1].minSeam == value:
                index = index + 1
            elif list1[i][index-1].minSeam == value:
                index = index - 1
        indexList.append(index)
        otherList.append(i)
        
    WRITE_TO_FILE(name, indexList, otherList, minSeam, list1)
        
def WRITE_TO_FILE(name, indexList, otherList, minSeam, list1):
    output = (open(name, 'w'))
    output.write("Min Seam: ")
    output.write(str(minSeam) + '\n')
    for i in range(0, len(list1)):
        tempString = "[" + str(otherList[i]) + ", " + str(indexList[i]) + ", " + str(list1[otherList[i]][indexList[i]].energy) + "]" + '\n'
        output.write(str(tempString))
        
list1 = READ_FROM_FILE()
minSeam, index = SeamCarving(list1)
name = sys.argv[1].replace(".txt", "_trace.txt")
traceBack(list1, index, minSeam, name)