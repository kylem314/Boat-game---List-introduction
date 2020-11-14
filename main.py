import time
import os
import curses
import random
from advancedstartrail import advancedStarTrail

exec(open("ship prints.py").read())

# Position variable
spacecount = 37

# Game state variables
looping = True
start = False

# Ocean printing variables
oceanstate = 0
oceanchange = 0
oceandict = {0 : "-", 1 : "~", 2 : "="}

# Point based variables
playerscore = 0
activeship = 1

# Ship printing dictionaries
shipdict = {1 : 2, 3 : 3, 5 : 4, 7 : 5}
shiplengths = {1 : 8, 2 : 22, 3 : 20, 4 : 21, 5 : 35}
shipfunctions_R = {1 : ship1R, 2 : ship2R, 3 : ship3R, 4 : ship4R, 5 : ship5R}
shipfunctions_L = {1 : ship1L, 2 : ship2L, 3 : ship3L, 4 : ship4L, 5 : ship5L}

# Coin related variables
global coinpresent
coinpresent = False
coinvalid = False
coinspace = 0

# Spacing variables, starts at 46 to center the first ship
spacecount = 46
border_distance = 100 - spacecount

def boatGame():
  print("Boat game loading...")
  time.sleep(3)
  os.system("clear")
  exec(open("boatgame.py").read())
  

def starTrail():
  print("You chose Regular Star Trail")
  time.sleep(3)
  os.system("clear")
  import startrail
  startrail.startrail()

def advancedStarTrail():
  print("You chose Advanced Star Trail")
  time.sleep(3)
  os.system("clear")
  exec(open("advancedstartrail.py").read())
  import advancedstartrail
  advancedstartrail.advancedStarTrail()

def credits():
  print("You chose credits")
  time.sleep(3)
  os.system("clear")
  print("Some list stuff")
  time.sleep (3)
  os.system("clear")
  print("By Kyle M, Kian K, Colin S, and James H")
  time.sleep(4)
  os.system("clear")
  choicesmenumatrix()

def exitCode():
  print("Repl boutta die unexpectedly")
  exit()

def StarTrailLen():
  print("You chose Advanced Star Trail Length")
  time.sleep(3)
  os.system("clear")
  exec(open("starlen.py").read())
  import starlen
  starlen.starlen()

choicesmenu = {1 : boatGame, 2 : starTrail, 3 : advancedStarTrail, 4 : credits, 5 : StarTrailLen, 6 : exitCode}

def choicesmenumatrix():
  print("Boat Game + List Introduction")
  print("=" * 30 + "\n1. Boat Game\n2. Regular Star Trail\n3. Advanced Star Trail\n4. Credits\n5. Star Trail Length\n6. Kill Replit (exit)\n" + "=" * 30)
  menunumchosen = input("What would you like to do?\n")
  userChoice = choicesmenu[int(menunumchosen)]
  userChoice()


  
choicesmenumatrix()
