"""
# Python Variables
Variables are containers for storing data values.
"""

"""
# Creating Variables
Python has no command for declaring a variable.
A variable is created the moment you first assign a value to it.
"""
x = 5
y = "John"
print(x)
print(y)

"""
Variables do not need to be declared with any particular type, and can even 
change type after they have been set.
"""
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

"""
# Casting
If you want to specify the data type of a variable, this can be done with 
casting.
"""
x = str(3)   # x will be '3'
y = int(3)   # y will be 3
z = float(3) # z will be 3.0

"""
# Get the Type
You can get the data type of a variable with the type() function.
"""
print(type(x))  # <class 'str'>
print(type(y))  # <class 'int'>
print(type(z))  # <class 'float'>

"""
# Single or Double Quotes?
String variables can be declared either by using single or double quotes:
"""
x = "John"
# is the same as
x = 'John'

"""
#Case-Sensitive
Variable names are case-sensitive.
"""
a = 4
A = "Sally"
#A will not overwrite a
print(a, A)  # 4 Sally

"""
# Variable Names
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). 

Rules for Python variables:
- A variable name must start with a letter or the underscore character
- A variable name cannot start with a number
- A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
- Variable names are case-sensitive (age, Age and AGE are three different variables)
- A variable name cannot be any of the Python keywords.
"""

# Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

"""
Illegal variable names:

2myvar = "John"
my-var = "John"
my var = "John"
"""

"""
# Multi Words Variable Names
"""

# camelCase
# Each word, except the first, starts with a capital letter:
myVariableName = "Rômulo"

# Pascal Case
# Each word starts with a capital letter:
MyVariableName = "Rômulo"

# Camel Case
# Each word is separated by an underscore character:
my_variable_name = "Rômulo"

"""
# Assign Multiple Values
"""
# Python allows you to assign values to multiple variables in one line:
x, y, z = "Banana", "Maça", "Laranja"
print(x, y, z)  # Banana Maça Laranja

# One Value to Multiple Variables
x = y = z = "Banana"
print(x, y, z)  # Banana Banana Banana

# Unpack a Collection: if you have a collection of values in a list, tuple etc. 
# Python allows you to extract the values into variables.
fruits = ["Banana", "Maça", "Laranja"]
x, y, z = fruits
print(x, y, z)  # Banana Maça Laranja

"""
# Global Variables
Variables that are created outside of a function (as in all of the examples in 
the previous pages) are known as global variables.

Global variables can be used by everyone, both inside of functions and outside.
"""
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

"""
If you create a variable with the same name inside a function, this variable 
will be local, and can only be used inside the function. 

The global variable with the same name will remain as it was, global and with 
the original value.
"""
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

"""
The global Keyword

Normally, when you create a variable inside a function, that variable is local, 
and can only be used inside that function.
"""

# To create a global variable inside a function, you can use the global keyword.
def myfunc():
  global x
  x = "fantastic2"

myfunc()

print("Python is " + x)

# To change the value of a global variable inside a function
x = "awesome3"

def myfunc():
  global x
  x = "fantastic3"

myfunc()

print("Python is " + x)

