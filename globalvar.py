x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()
#########
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
#########
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x) #will print both
#########
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x) #will b eonly last one with global
#########

