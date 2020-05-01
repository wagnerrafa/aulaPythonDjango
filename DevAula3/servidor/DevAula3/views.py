from django.shortcuts import render
import random

listLudo=['wagner','josue','amanda','carol','denis','esly','fabricio','jeferson','jonatham','leonardo','fernando','nikolas','pc','rone','vitor','washington','thais','cecilia','leticia','ligia']
random.shuffle(listLudo)

n = 5
splited = [listLudo[i::n] for i in range(n)]

for i in splited:
    print(i)
