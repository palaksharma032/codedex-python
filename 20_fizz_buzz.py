''' Challenge: FizzBuzz

Objective: Solve the classic logic puzzle that iterates through numbers and prints specific strings for multiples of 3 and 5. '''
num = 1
while (num<=100):
  if (num%3==0 and num%5==0):
    print("FizzBuzz")
  elif(num%3==0):
    print ("Fizz")
  elif (num%5==0):
    print ("Buzz")
  else:
      print(num)
  num=num+1





