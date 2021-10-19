""" Assumptions of this program: 
    Every floor is 1:1 difficulty, meaning this is really only applicable to ironmen
    Prestige 60 (I tried to make variable prestige and it would just require way too much data)
    Level mod and bonus rooms will balance out, which, on average, they just about will, unless you clear every monster
    No deaths
    Buying team cards isn't optimal with finite tokens (this is probably correct)
"""
from flrMethods import *

# Ranges of floor sizes/cards. Second value is exclusive
skipRange = range(0, 0)
c1Range = range(0, 0)
c6Range = range(1, 30)
medRange = range(30, 36)
uncardLargeRange = range(36, 36)
mosquitoRange = range(36, 42)
ibisRange = range(42, 49)
locustRange = range(49, 57)
teamRange = range(30, 30)


# average floor time in minutes for a floor size
rushTime = 1.5
smallTime = 2.5
medTime = 5
largeTime = 13

# use calcTotal for total exp from every floor, getTotExp for exp of a single floor

def calcTotal():
    totalExp = 0
    totalMins = 0
    tokenProfit = 0

    for flr in skipRange:
        tokenProfit -= skipCost(flr)

    for flr in c1Range:
        exp = getTotExp(flr, "c1")
        totalExp += exp
        totalMins += rushTime
        tokenProfit += exp / 10

    for flr in c6Range:
        exp = getTotExp(flr, "small")
        totalExp += exp
        totalMins += smallTime
        tokenProfit += exp / 10

    for flr in medRange:
        exp = getTotExp(flr, "med")
        totalExp += exp
        totalMins += medTime
        tokenProfit += exp / 10

    for flr in uncardLargeRange:
        exp = getTotExp(flr, "large")
        totalExp += exp
        totalMins += largeTime
        tokenProfit += exp / 10

    for flr in mosquitoRange:
        exp = getTotExp(flr, "large")
        totalExp += exp
        totalMins += largeTime
        tokenProfit += exp / 5

    for flr in ibisRange:
        exp = getTotExp(flr, "large")
        totalExp += exp * 1.5
        totalMins += largeTime
        tokenProfit += exp / 10

    for flr in locustRange:
        exp = getTotExp(flr, "large")
        totalExp += exp * 2
        totalMins += largeTime
        tokenProfit += exp / 10
        
    for flr in teamRange:
        exp = getTotExp(flr, "large")
        totalExp += exp * 2.5
        totalMins += largeTime
        tokenProfit += exp / 5 - 150000
    
    tokenProfit -= max(len(locustRange), len(ibisRange), len(mosquitoRange)) * 50000 # potentially inaccurate but I don't see a better way to calculate this

    return "Tokens: " + str(tokenProfit) + "\nTotal Exp: " + str(totalExp) + "\nExp/hr: " + str(totalExp / (totalMins / 60))

print(calcTotal())