from ossapi import ScoreType
from decimal import Decimal

def askInput():
    # dict to define all types of filters and modes
    post_types = {
        'T': ScoreType.BEST,
        'R': ScoreType.RECENT,
    }
    
    postType = post_types.get(input("Input filter - T(op play), R(ecent score): ").upper())
    print("Checking that play... \n")
    return postType

def generateScorepost(api, subject, filter):
    # define all the commonly used data as single words so its easier to gram
    playList = api.user_scores(user_id=subject.id, type=filter, include_fails=False, 
            limit=1, offset=0, legacy_only=False)
    topPlaySet = playList[0].beatmapset
    mapInfo = playList[0].beatmap
    mapper = topPlaySet.creator

    # acc is stored as a float so we have to do some gimmick to turn it into a two place decimal
    acc = Decimal(playList[0].accuracy * 100).quantize(Decimal("1.00"))

    # lots of printing/formatting under this
    print(subject.username, " | ", topPlaySet.artist, " - ", topPlaySet.title, " [", playList[0].beatmap.version, "] +", 
        end="", sep="")
    if len(playList[0].mods) == 1:
        print("NMCL", end="", sep="")
    else:
        for mod in playList[0].mods:
            print(mod.acronym, end="", sep="")
    print(" (", mapper, ", ", mapInfo.difficulty_rating, "*) ", acc, "% ", sep="", end="")
    if playList[0].accuracy == 1:
        print("SS")
    elif playList[0].statistics.combo_break != None:
        print(playList[0].statistics.miss, "xMiss, ", sep="", end="")
    else:
        print(playList[0].statistics.ok, "x100, ", sep="", end="")
    print(int(playList[0].pp), "pp, ", playList[0].max_combo, "/", mapInfo.max_combo, "x", sep="")