''' Challenge: Currency Converter

Objective: Build a script that converts multiple foreign currencies into USD based on user input and exchange rates.'''
pesos=float(input("eneter currency left in peso"))
soles=float(input("Enter currency left in sole"))
reias=float(input("Enter currency ledt in reia"))
total=float(pesos*0.00026+ soles*0.3+reias *0.185)
print(total)