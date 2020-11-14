#most of this code is the same as startrail.py so look there for comments, it changed on line 86
import time
import os
from random import randrange, randint
item = 0

#terminal print commands
#define function
def advancedStarTrail():
  #defining colors and clear screen
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
  
  possibleColor = [ CBLACK, CRED, CGREEN, CYELLOW, CBLUE, CVIOLET, CBEIGE, CWHITE]
  #defining function that prints the ocean
  def ocean_print():
    #print ocean
    print(ANSI_CLEAR_SCREEN, ANSI_HOME_CURSOR)
    print("\n\n\n\n\n\n\n\n\n\n\n")
    print(OCEAN_COLOR + "  " * 70)

  #print ship with colors and leading spaces
  def ship_print(position):
    #os.system('cls' if os.name=='nt' else 'clear')
    print(ANSI_HOME_CURSOR)
    print(RESET_COLOR)

    #defining arrays
    characters = ["★", "☆", "⋆", "★", "☆", "✦", "✧", "✫", "✬", "✯", "⭐"]
    delete = [2, 4, 3, 5, 6, 7]

    #defining different functions to keep randomization constant
    def spaceFunction():
      return position - delete[randrange(5)]
    def insert():
      return position - space
    def sp00():
      return " " * space #the space behind the trail 
    def randomRange():
      return characters[randrange(11)]
    def color():
      return possibleColor[randrange(7)]
    
    def print7():
      return 6
    def print6():
      return 5
    def print5():
      return 4
    def print4():
      return 3
    def print3():
      return 2
    def print2():
      return 1
    
    printNumber = {
      7: print7,
      6: print6,
      5: print5,
      4: print4,
      3: print3,
      2: print2
    }
    global space
    space = spaceFunction()
    sp00 = sp00()
    insert = insert() #position - space
    randomRange = randomRange()
    color = color()
    for key,value in printNumber.items():
      if insert == key:
        sp0 = value
    #defining an array for each line of the ship
    shipPrints = ["        |","      -----              |","      )___(            -----","        |              )___(","    ---------            |","   /   ⚓     \        -------","  /___________\      /  ⚓    \ ","\_______|________________|_______"," \_    > > >   > > >   > > >   _/","   \__________________________/"]

    #defines variable for which line to choose
    lineNumber = 0
    for x in range (10): #for loop runs 10 times, once for each line of the ship
      
      print(sp00, end="")
      for x in range(int(sp0())):
        randomEvent = randint(0,4)
        if randomEvent < 2:
          print(possibleColor[randrange(7)] + characters[randrange(11)], end=" ")
        else:
          print(possibleColor[randrange(7)] + " ", end=" ")
      print(SHIP_COLOR + shipPrints[lineNumber]) #instead of putting the string here, shipPrints[lineNumber] takes the string from the shipPrints array for each line of the ship
      lineNumber += 1 #adds one to the line number so it prints the next line each time

  #ship function, iterface into this file
  def ship():
    #only need to print ocean once
    ocean_print()   

    #loop control variables
    start = 0         #start at zero
    distance = 80  #how many times to repeat
    step = 4       #count by 2
    
    #loop purpose is to animate ship sailing
    for position in range(start,distance, step): 
      
      ship_print(position)  #call to function with parameter
      time.sleep(.1)
      space

  ship()    
