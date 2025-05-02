from ossapi import GameMode, UserLookupKey, ScoreType
from decimal import Decimal

def generateScorepost(api):
    player = input("Type name of user: ")
    scoreOffset = int(input("Type which play you want displayed (1 for top play): ")) - 1
    print("Checking the std play... \n")

    subject = api.user(user=player, mode=GameMode.OSU, key=UserLookupKey.USERNAME)
    playList = api.user_scores(user_id=subject.id, type=ScoreType.BEST, include_fails=False, mode=GameMode.OSU, 
            limit=1, offset=scoreOffset, legacy_only=False)
    topPlaySet = playList[0].beatmapset
    creator = api.user(user=topPlaySet.user_id, key=UserLookupKey.ID)

    acc = Decimal(playList[0].accuracy * 100).quantize(Decimal("1.00"))

    print(subject.username, " | ", topPlaySet.artist, " - ", topPlaySet.title, " [", playList[0].beatmap.version, "] +", 
        end="", sep="")
    if len(playList[0].mods) == 1:
        print("NMCL", end="", sep="")
    else:
        for mod in playList[0].mods:
            print(mod.acronym, end="", sep="")
    print(" (", creator.username, ", ", api.beatmap(beatmap_id=playList[0].beatmap_id,).difficulty_rating, "*) ", 
        acc, "% ", sep="", end="")
    if playList[0].accuracy == 1:
        print("SS")
    elif playList[0].statistics.combo_break != None:
        print(playList[0].statistics.miss, "xMiss, ", sep="", end="")
    elif playList[0].statistics.ok != 0:
        print(playList[0].statistics.ok, "x100, ", sep="", end="")
    print(int(playList[0].pp), "pp, ", playList[0].max_combo, "/", api.beatmap(beatmap_id=playList[0].beatmap_id,).max_combo, 
        "x", sep="")