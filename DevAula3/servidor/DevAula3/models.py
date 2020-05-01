from django.db import models
import math, time, random
from math import *

# print(pi)
# print(dir(math))
# print('function seno', math.pi*2)
# pi1 = math.pi
# pi2 = math.pi
# total = pi1+ pi2
# raiz = sqrt(9)
# print(total)
# print(raiz)

# total = 0 
# number = 99

# for i in range(0, number,2):
#     total = total+i
#     print(i)

# print(total)

# print("test list\n")

# mylist=[0,1,2,3,4,5,10]
# newList= []

# print("position", mylist[6])
# print(mylist)
# print("quantidade de itens", len(mylist))

# for list in mylist:
#     print(list)

# print("nova lista\n")

# newList.insert(0,5)
# newList.insert(10,4)

# print(newList)

# myRandomList = []
# total = 0

# lis=[1,1,1,1,1,]

# for i in range(25):
#     myRandomList.append(random.randrange(1,100))

# myRandomList.sort()
# print(myRandomList)
# print("quantidade de itens selecionados\n",myRandomList.count(2))

# seachList = input("numero buscado")
# seachList = int(seachList)

# if seachList in myRandomList:
#     print("found no index", myRandomList.index(seachList))
# else:
#     print("not found")

# print ("tuples")

# myTuple = 'wagner', 2020, "devmedia", 73, 1.75
# (nome, ano, curso, peso, altura) = myTuple

# print("meu tuple", myTuple)
# print(len(myTuple))
# print(myTuple[2])
# print("nome", nome)

print ("Test Multidimensional Sequences")

def printList(inputList):
    print("Value in List: ")
    for row in inputList:
        for item in row:
            print (item, " ")
        print ()

def average(gradesOfStudent):
    total = 0.0
    for grade in gradesOfStudent:
        total += grade
    return total/len(gradesOfStudent)

listOfGrades = [ [6.4, 7.5, 8.2, 7.7], [9.8, 8.8, 8.9, 9.1], [8.2, 9.0, 8.6, 8.7], [6.1, 3.2, 0.0, 7.1] ]

printList(listOfGrades)

for i in range(len(listOfGrades)):
    print("Average / Student", i, "is", average(listOfGrades[i]))