from ossapi import BeatmapsetSearchCategory, BeatmapsetSearchExplicitContent, BeatmapsetSearchSort
from ossapi import BeatmapsetSearchMode
# notes - STD: aim_difficulty, slider_factor, speed_difficulty
#   MANIA: none??? idk how that class works ngl

def recommendationParams():    
    mods = input("Please type any combination of mods (i.e. HD, DT, HR): ")
    playstyle = input("What kind of map are you looking for (i.e. AIM, SPEED, SLIDER): ")
    modsCap = mods.upper()
    modlist = []
    # convert string of mods into list of two chars (seperate all input mods so its easier to calc)
    for mod in range(0, len(modsCap), 2):
        modlist.append(modsCap[mod:mod+2])

    return modlist, playstyle

def findRecommendation(api, subject, mods, playstyle):
    reference = pow(subject.statistics.pp, 0.4) * 0.195 # pp to recommended diff conversion
    lowerBound = reference - 0.5
    upperBound = reference + 0.5
    # find list of possible beatmapsets DEFAULT TO OSU
    searchResultSets = api.search_beatmapsets(query="star>{lowerBound}, star<{upperBound}", 
                                      category=BeatmapsetSearchCategory.RANKED, 
                                      explicit_content=BeatmapsetSearchExplicitContent.SHOW, 
                                      sort=BeatmapsetSearchSort.RANKED_DESCENDING,
                                      mode=BeatmapsetSearchMode.OSU).beatmapsets
    while len(searchResultSets) > 1:
        searchResultSets.pop()
    
    songInfo = [] # of type list(beatmapset) - for song name/artist etc.
    listOfRecs = [] # of type list(beatmap) - for id
    for i in range(len(searchResultSets)):
        for j in range(len(searchResultSets[i].beatmaps)):
            # this line is problematic, because it's in the loop it will get called a bunch and slow the program
            # down. there needs to be a better way to do this using the data from search_beatmapsets
            stats = api.beatmap_attributes(beatmap_id=searchResultSets[i].beatmaps[j].id)
            skillRatio = stats.attributes.aim_difficulty / stats.attributes.speed_difficulty
            if skillRatio > 0: # FIGURE THIS OUT
                songInfo.append(searchResultSets[i]) # does not check specific diff/mods, only rec diff
                listOfRecs.append(searchResultSets[i].beatmaps[j])

    return songInfo, listOfRecs

def printRecommendations(songInfo, recs):
    for i in range(len(recs)):
        print(songInfo[i].title, " by ", songInfo[i].artist, " (", recs[i].difficulty_rating,
               "*) - ", recs[i].url, sep="")  
    
    # no return