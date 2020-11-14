## Welcome to our Introduction to Lists & Dictionary and Iteration!

# Lists

## Definition

#### Lists are another data type, and they store multiple values such as variables, integers, strings, etc. 
They are zero-indexed, meaning the first term is the "0th" term, and then it increases by 1 for each term. Example, if a list had 3 values, the first value will be the 0 index, the second will be the 1 index, the third will be the 2 index.

## Syntax

Lists are defined by `listname = [term1, term2, term3, etc]`.  Remember, when you want to make a term a string, you must add quotes; `listname = ["term1", "term2", "term3", "etc"]`

You can pull values out of a list by typing `listname[index]`, where index is the piece you want to pull out.

For example,
```
example_list = [1, 2, 3, 4]
print(example_list[2])
```
would print the number 3 in the output terminal. Remember, the index starts at 0, so the 2nd index is the 3rd term.

# Loops

## Definition

#### Used for iteration (repeating a section of code multiple times), there are multiple types of loops.

### For loops

These will run the following code for a certain number of times, which is specified in the syntax;

## Syntax

For loops are used by 
```
for variable in range(loops):
  loop content
```
Note - anything inside of a loop must be indented - that's what tells the computer that the code is inside of the loop
The variable can be anything - that will record the number of times it's been iterated through.

**For** example,
```
for x in range(3)
  print(x)
```
would print 

0
1
2

in the output terminal.  These are also zero indexed, so the first time it is iterated through, the variable will be 0, then 1, and so on.

# Dictionary
A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.

Example
### Create and print a dictionary:
```
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict)
```
above will print: 
```{'year': 1964, 'model': 'Mustang', 'brand': 'Ford'}```

### Accessing Items
You can access the items of a dictionary by referring to its key name, inside square brackets:

Example
Get the value of the "model" key:
```
x = thisdict["model"]
```
above will print: 
```Mustang```
There is also a method called get() that will give you the same result:

Example
Get the value of the "model" key:
```
x = thisdict.get("model")
```
above will print: 
```Mustang```

# Combining these concepts

Lists can be iterated through, meaning you can run code for each term in a list
This is done by writing a for loop, but instead of giving a range, you would give the list

For example,
`
for variable in list:
  print(variable)
`

# Implementing the concepts
## How to Store Images in Lists
Lists in "boatgame.py" are used by storing each slice of the ship as different values within the list

`
ship1_L = ["   /|   ", "   \|   ", "\___|__/", " \____/ "]
ship1_R = ["    |\  ", "    |/  ", "\___|__/", " \____/ "]
`

if we wanted to print out the bottom of the ship we would type
`print(ship1_L[3])`
in terminal we would get the output:
```
" \____/ "
```
as we have 4 values in the list they are each labeled in a base 3 format
so if we wanted to get the top of the ship we would call
`print(ship1_L[0])`

in terminal we would get the output:
```
"   /|   "
```

if we wanted to get the whole ship 
```
print(ship1_L[0])
print(ship1_L[1])
print(ship1_L[2])
print(ship1_L[3])
```

This would provide the image in terminal 
```
   /|   
   \|   
\___|__/
 \____/ 
```
## Using Iteration to Print Lists

alternatively we can get the same output by the code
```
for variable in ship1_L:
  print(variable)
```

This would provide the image in terminal
```
   /|   
   \|   
\___|__/
 \____/  
```

as there are 4 units within the list, the for loop iterates or loops 4 times, printing all units of data (all slices of the ship) in the terminal 

This allows the code to be modular, if the programmer wanted to edit the design of the ASCII ship within the program without the usage of list, they would have to copy and paste each ASCII line into the code, if there was a larger ship. 
```
        |
      -----               |
      )___(             -----
        |               )___(
     ---------            |
   /  ⚓⚓  \        -------
  /___________\      / ⚓⚓ \
        |           /_________\  
________|________________|______/      
\_    > > >   > > >   > > >   _/
  \__________________________/
```
the code would still be the same length
```
for variable in ship5_L:
  print(variable)
```
because this ship is 10 slices (10 lines tall) the for loop would iterate 10 times to print out the entire ship within the terminal

This concept of using iteration allows programmers less headache while developing code. All art can be sliced into lists before coding and the programmer will not need to worry about copy and pasting the ASCII art within print statements.



