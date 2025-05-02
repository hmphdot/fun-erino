from ossapi import Ossapi

def recommendationParams():    
    mods = 1 # ask for mods (should be able to interpret any length permutation of two letter segments)
    playstyle = 1 # which difficulty rating to look for

    return mods, playstyle

def findRecommendation(mods, playstyle):
    listOfRecs = mods * playstyle # api magic here

    return listOfRecs

def printRecommendations(recs):
    for rec in recs:
        print("hello world...")
    
    # no return