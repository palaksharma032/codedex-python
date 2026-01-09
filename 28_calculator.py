''' Challenge: Calculator

Objective: Build a modular program where each mathematical operation (add, subtract, etc.) is handled by a separate function. '''
# Write code below 💖
def add(a,b):
  Total = a + b
  return (Total)

def subtract(a,b):
  Difference = a - b
  return (Difference)

def multiply(a,b):
  Multiplication = a*b
  return(Multiplication)

def divide(a,b):
  if b!=0:
    Division = a/b
    return (Division)
  else:
    return ("Invalid")
  
  def exp(a,b):
    Exponent = b**a
    return (Exponent)

  add(2,3)
  subtract(2,3)
  multiply(2,3)
  divide(2,0)
  exp(2,2)



