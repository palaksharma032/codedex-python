''' Challenge: Enter PIN

Objective: Implement a while loop to control access to a program by validating a user-entered PIN. '''

print('BANK OF CODÉDEX')

pin = int(input('Enter your PIN: '))

while pin != 1234:
  pin = int(input('Incorrect PIN. Enter your PIN again: '))

if pin == 1234:
  print('PIN accepted!')
