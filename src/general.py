from ossapi import GameMode

# todo
#   change the XX on line 17 to whatever i set the command to be

def startUpInput():
    # dict of all mode types
    mode_types = {
        'STD': GameMode.OSU,
        'MANIA': GameMode.MANIA,
        'CATCH': GameMode.CATCH,
        'TAIKO': GameMode.TAIKO
    }
    # below asks user input
    name = input("Hi! Welcome to fun-erino, the tillerino ripoff! Please enter your osu! user: ")
    mode = mode_types.get(input("Input gamemode - STD, MANIA, CATCH, TAIKO: "))
    print("Thank you! These settings can be changed at any time with the command XX.")

    return name, mode