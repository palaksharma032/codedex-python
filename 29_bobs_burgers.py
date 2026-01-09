''' Challenge: Bob's Burgers

Objective: Define a class with an __init__ constructor to represent a restaurant menu item and create instances of that class. '''
class Restaurant:
  name =''
  category = ''
  rating = 0.0
  delivery = False

bobs_burgers=Restaurant()
bobs_burgers.name = 'Bob\'s Burgers'
bobs_burgers.category = 'American Diner'
bobs_burgers.rating = 4.7
bobs_burgers.delivery = False

print(vars(bobs_burgers))


