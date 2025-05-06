# fun-erino
Tillerino ripoff that sorts by fun-ness and map type instead of pp \
PREFERABLY KEEP API REQUESTS TO ONE A SCRIPT

# Dependencies (how to setup/use)
Place api information into a file named config.py in the src/ directory. \
see requirements.txt to find all dependencies and their install commands.

# Future Features (todo/bugs)
### main
Create interface (or interact with IRC) so its not cli based

### recommend
input - robustness \
findRecs - 1. check stats against player input and skill level (add compatibility w/ mods) \
find a good ratio that weighs aim and speed properly \
specific api call for beatmap_attributes that has to be called every time the program wants to check the aim/speed ratio of the specific map adds traffic and decreases speed, find a way around that \
make it work with user gamemode (because we removed input, you have to query it directly now) \
add more info to printRec (pp, length, etc.)

### scorepost
askInput - robust user input (misinputs + player has no scores on that gamemode) \
If the score was modded, the star rating doesn't change it shows it NM \
Add an if fc to recent play (must check that it wasn't an fc first) \
add how long ago the play was set (recent) 

### general
be able to change gamemode, rn will take default gamemode of user (before that add confirmation of mode) \
learn how to make mock data so i dont get banned for using the api too much when testing