# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 20:56:59 2023

@author: samadi
"""

import random
 
def rollDie():
    """returns a random int between 1 and 6"""
    return random.choice([2,3,4,5,7,9])
 
def testRoll(n = 10):
    result = ''
    for i in range(n):
        result = result + str(rollDie())
    print(result) 
    
testRoll(9) 

random.seed(5)

def runSim(goal, numTrials, txt):
    total = 0
    for i in range(numTrials):
        result = ''
        for j in range(len(goal)):
            result += str(rollDie())
        if result == goal:
            total += 1
    print('Actual probability of', txt, '=',
          round(1/(6**len(goal)), 8)) 
    estProbability = round(total/numTrials, 8)
    print('Estimated Probability of', txt, '=',
          round(estProbability, 8))

runSim('11111', 1000, '11111')


def sameDate(numPeople, numSame):
    possibleDates = range(366) 
    
    birthdays = [0]*366
    for p in range(numPeople):
        birthDate = random.choice(possibleDates)
        birthdays[birthDate] += 1
    return max(birthdays) >= numSame 


def birthdayProb(numPeople, numSame, numTrials):
    numHits = 0
    for t in range(numTrials):
        if sameDate(numPeople, numSame):
            numHits += 1
    return numHits/numTrials 

import math

for numPeople in [10, 20, 40, 100]:
    print('For', numPeople,
          'est. prob. of a shared birthday is',
          birthdayProb(numPeople, 2, 10000))
    numerator = math.factorial(366)
    denom = (366**numPeople)*math.factorial(366-numPeople)
    print('Actual prob. for N = 100 =',
          1 - numerator/denom)
    
# Run it for 100000 trails (iterations) and for 3 people!

#math lib provides the random sampling!

import math

for numPeople in [15, 25, 35 , 85]:
    print('For', numPeople,
          'est. prob. of a shared birthday is',
          birthdayProb(numPeople, 2, 10000))
    numerator = math.factorial(366)
    denom = (366**numPeople)*math.factorial(366-numPeople)
    print('Actual prob. for N = 100 =',
          1 - numerator/denom)


    