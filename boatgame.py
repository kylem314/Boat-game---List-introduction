# Function to print the coin
def coinprint1(stdscr):
  stdscr.addstr(2,coinspace,"x")

# Function to generate a coin
def coingen(spacecount,coinvalid):
  global coinpresent, coinspace
  while coinvalid == False:
    coinspace = random.randrange(100)

# Making sure the coin isn't printing on top of or right next to the ship
    if coinspace >= spacecount + shiplengths[activeship] + 10 or coinspace <= spacecount - 10:
      coinvalid = True
      coinpresent = True
    else:
      coinvalid = False
  return coinpresent, coinspace

# Function to call to print the ocean, coin, and score
def sceneprint(oceanstate, coinspace, playerscore):
  print("\r" + u"\u001B[34m" + oceandict[oceanstate] * 100 + u"\u001B[0m")
  print("\r" + u"\u001B[34m" + oceandict[oceanstate] * 100 + u"\u001B[0m")
  print("\r" + coinspace * " " + "🧭")
  print("\rScore: " + str(playerscore))

# Setting up the Curses module
stdscr =  curses.initscr()
curses.curs_set(0)
curses.noecho()
curses.cbreak() 
stdscr.keypad(True)

# Welcome statement
print("Welcome to the boat game! Hit the left or right arrows to begin.")
time.sleep(1)

# While the game is being played:
while looping == True:

# If a coin doesn't exist, generate a new coin
  if coinpresent == False:
    coingen(spacecount,coinvalid)

# Getting the space from the right edge, in order to make it so you can't move past the right border
  border_distance = 100 - spacecount

# Randomizing the ocean character
  oceanchange += 1
  if oceanchange % 10 == 0:
    oceanstate = random.randrange(3)
  key = stdscr.getch()
# If the player clicks right, move the ship and print the scene
  if key == curses.KEY_RIGHT:
    if border_distance == shiplengths[activeship]:
      pass
    else:
      spacecount += 1
      shipprint = shipfunctions_R[activeship]
      shipprint(spacecount)
      stdscr.refresh()
      sceneprint(oceanstate, coinspace, playerscore)   

# If the player clicks left, move the ship and print the scene
  if key == curses.KEY_LEFT:
    spacecount -= 1
    shipprint = shipfunctions_L[activeship]
    shipprint(spacecount)
    stdscr.refresh()
    sceneprint(oceanstate, coinspace, playerscore)


# If the ship hits a coin, add a point and generate a new coin
  if coinspace == spacecount - 1 or coinspace == spacecount + shiplengths[activeship]:
    coinpresent = False
    playerscore += 1

# If the player reaches a score benchmark, change the ship
    for key,value in shipdict.items():
      if playerscore == key:
        activeship = value

# Curses module settings
curses.curs_set(1)
curses.echo()
curses.nobreak()
stdscr.keypad(False)  