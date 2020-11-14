import time
import os
from random import randrange, randint
item = 0

#terminal print commands
#define function
def startrail():
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
    print("\n\n\n\n")
    print(OCEAN_COLOR + "  " * 50)

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
      return position - delete[randrange(5)] #number of spaces behind the trail
    def insert():
      return position - space #number of star characters printed behind the ship
    def sp00():
      return " " * space #prints the spaces
    def randomRange():
      return characters[randrange(11)] #chooses random character from array
    def color():
      return possibleColor[randrange(7)] #chooses random color from array

    #defining the variables from the functions above
    global space
    space = spaceFunction()
    sp00 = sp00()
    insert = insert() #position - space
    randomRange = randomRange()
    color = color()

    
    #4 for looops for printing each line of code
    print(sp00, end="")
    for x in range(int(insert - 1)):
      randomEvent = randint(0,4)
      if randomEvent < 2:
        print(possibleColor[randrange(7)] + characters[randrange(11)], end=" ")
      else:
        print(possibleColor[randrange(7)] + " ", end=" ")
    print(SHIP_COLOR + "    |\   ")

    print(sp00, end="")
    for x in range(int(insert - 1)):
      randomEvent = randint(0,4)
      if randomEvent < 2:
        print(possibleColor[randrange(7)] + characters[randrange(11)], end=" ")
      else:
        print(possibleColor[randrange(7)] + " ", end=" ")
    print(SHIP_COLOR +"    |/   ") 

    print(sp00, end="")
    for x in range(int(insert - 1)):
      randomEvent = randint(0,4)
      if randomEvent < 2:
        print(possibleColor[randrange(7)] + characters[randrange(11)], end=" ")
      else:
        print(possibleColor[randrange(7)] + " ", end=" ")
    print(SHIP_COLOR +"\__ |__/ ")

    print(sp00, end="")
    for x in range(int(insert - 1)):
      randomEvent = randint(0,4)
      if randomEvent < 2:
        print(possibleColor[randrange(7)] + characters[randrange(11)], end=" ")
      else:
        print(possibleColor[randrange(7)] + " ", end=" ")
    print(SHIP_COLOR +" \____/  ")
    

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
