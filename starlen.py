import time
import os
from random import randrange
item = 0


def starlen():
  sp = 0 
  #terminal print commands
  ANSI_CLEAR_SCREEN = u"\u001B[2J"
  ANSI_HOME_CURSOR = u"\u001B[0;0H\u001B[2"
  OCEAN_COLOR = u"\u001B[44m\u001B[2D"
  SHIP_COLOR = '\33[32m' #u"\u001B[35m\u001B[2D"
  RESET_COLOR = u"\u001B[0m\u001B[2D"

  CBLACK  = '\33[30m'
  CRED    = '\33[31m'
  CGREEN  = '\33[32m'
  CYELLOW = '\33[33m'
  CBLUE   = '\33[34m'
  CVIOLET = '\33[35m'
  CBEIGE  = '\33[36m'
  CWHITE  = '\33[37m'

  #possible color list stores the variables corresponding to the coloring to the text colotrs
  possibleColor = [CBLACK, CRED, CGREEN, CYELLOW, CBLUE, CVIOLET, CBEIGE, CWHITE]

  # defining the trail of stars
  characters = ["★", "☆", "⋆", "★", "☆", "✦", "✧", "✫", "✬", "✯", "⭐", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", " ", " "] 

  #defining the ship
  #ship1_R = ["    |\  ", "    |/  ", "\___|__/", " \____/ "] 
  ship1_R = ["                         |", "        |              -----", "      -----            )___(", "      )___(              |","        |            ---------", "     -------        /   ⚓     \ ", "    /  ⚓    \      /___________\ ", "   /_________\           |","  ______|________________|________/", "  \_     < < <  < < <  < < <    _/", "    \__________________________/"]
  #defining the length of the trail
  character_count = 5

  #prints the ocean once in the program
  def ocean_print():
    #print ocean
    print(ANSI_CLEAR_SCREEN, ANSI_HOME_CURSOR)
    
    for i in range(len(ship1_R)+1): #this moves the cursor down 
      print("\n", end="")
    print(OCEAN_COLOR + "  " * 50)

  #print ship with colors and leading spaces
  def ship_print(position,characters,ship1_R,character_count,possibleColor):
    print(ANSI_HOME_CURSOR)#to clear the screen print in the same top left corner every time
    print(RESET_COLOR) #to stop coloring after the ocean, without this line then everything is highlighted
    sp = " " * position#taking the control variable and translating the value into amount of spaces
    for i in range(len(ship1_R)): #itterating for the length of the ship1_R list
      print(sp, end="")#prints and spaces and appends the next line
      for x in range(character_count):#for character_count, chooses a random color, then random character
        print(possibleColor[randrange(len(possibleColor))] + characters[randrange(len(characters))], end=" ")
      print(SHIP_COLOR + ship1_R[i])#prints the slice of the ship with color

  #ship function, iterface into this file
  def ship():
    #only need to print ocean once
    ocean_print()   

    #loop control variables
    start = 0         #start at zero
    distance = 80  #how many times to repeat
    step = 4       #count by 2
    
    #loop purpose is to animate ship sailing
    for position in range(start,distance,step): 
      
      ship_print(position,characters,ship1_R,character_count,possibleColor)  #call to function with parameter
      time.sleep(.1)
      #space

  ship()    
  #print (len(ship1_R))