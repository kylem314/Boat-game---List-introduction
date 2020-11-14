# Note how these lists look disorganized - By printing them line by line (in the for loops), we can create order from this chaos
# Starting Boat
ship1_L = ["   /|   ", "   \|   ", "\___|__/", " \____/ "]
ship1_R = ["    |\  ", "    |/  ", "\___|__/", " \____/ "]

# Yacht
ship2_L = ["           ____       ", "     _____/____|      ", "____/_____\_____\_____", "\____________________/"]
ship2_R = ["      ____", "     |____\_____", "____/_____/_____\____", "\___________________/ "]

# Tug Boat
ship3_L = ["      __|__         ", "      || ||_____    ", "      || ||    |    ", "--------------------", "\   O   O   O   O  /", " \________________/ "]
ship3_R = ["         __|__", "     ____|| ||", "    |    || ||", "--------------------", "\ O   O   O   O    /", " \________________/"]
# Large Yacht
ship4_L = ["         __/__     //", "    ____/_____|   // ", "___/___\______\__//__", "\    < < < < < <    /", " \_________________/ "]
ship4_R = ["\\\\      __/__", " \\\\    |_____/___", "__\\\\__/______/___\___", "\    > > > > > >    /", " \_________________/ "]
# Pirate Ship
ship5_L = ["        |", "      -----              |", "      )___(            -----", "        |              )___(","    ---------            |", "   /   ⚓     \        -------", "  /___________\      /  ⚓    \ ", "        |           /_________\  ","\_______|________________|_______", " \_    > > >   > > >   > > >   _/", "   \__________________________/"]
ship5_R = ["                         |", "        |              -----", "      -----            )___(", "      )___(              |","        |            ---------", "     -------        /   ⚓     \ ", "    /  ⚓    \      /___________\ ", "   /_________\           |","  ______|________________|________/", "  \_     < < <  < < <  < < <    _/", "    \__________________________/"]

# Defining functions to be printed later - called in boatgame.py
def ship1R(spacecount):
  os.system("clear")
  for line in ship1_R:
    space = " " * int(spacecount)
    print("\r" + space + line)
def ship1L(spacecount):
  os.system("clear")
  for line in ship1_L:
    space = " " * int(spacecount)
    print("\r" + space + line)
def ship2R(spacecount):
  os.system("clear")
  for line in ship2_R:
    space = " " * int(spacecount)
    print("\r" + space + line)
def ship2L(spacecount):
  os.system("clear")
  for line in ship2_L:
    space = " " * int(spacecount)
    print("\r" + space + line)
def ship3R(spacecount):
  os.system("clear")
  for line in ship3_R:
    space = " " * int(spacecount)
    print("\r" + space + line)
def ship3L(spacecount):
  os.system("clear")
  for line in ship3_L:
    space = " " * int(spacecount)
    print("\r" + space + line)
def ship4R(spacecount):
  os.system("clear")
  for line in ship4_R:
    space = " " * int(spacecount)
    print("\r" + space + line)
def ship4L(spacecount):
  os.system("clear")
  for line in ship4_L:
    space = " " * int(spacecount)
    print("\r" + space + line)
def ship5R(spacecount):
  os.system("clear")
  for line in ship5_R:
    space = " " * int(spacecount)
    print("\r" + space + line)
def ship5L(spacecount):
  os.system("clear")
  for line in ship5_L:
    space = " " * int(spacecount)
    print("\r" + space + line)
