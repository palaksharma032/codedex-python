''' Challenge: Pythagorean Theorem

Objective: Use the math module to calculate the hypotenuse of a right-angled triangle based on user-provided side lengths.'''
import math
a=float(input("Enter value of a:"))
b=float(input("Enter value of b:"))
c=float (math.sqrt(a**2+b**2))
print(c)