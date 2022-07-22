"""# the statement will raise an error because x is not defined
try:
  print(x)
except:
  print("An exception occurred")

########################################################################################################################

# try block does not raise any error so the else block is executed
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

########################################################################################################################

# finally block will be executed no matter if try block raises any error or not
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

########################################################################################################################

# Raise an error and stop the program if x is lower than 0
x = -1
if x < 0:
  raise Exception("Sorry, no numbers below zero")"""

########################################################################################################################
x=int(input("x : "))
y=int(input("y : "))
try:
  result = x // y
except ZeroDivisionError:
    print("Sorry ! You are dividing by zero ")
else:
    print("Yeah ! Your answer is :", result)
finally:
    print('This is always executed')
