''' Challenge: Favorite Cities

Objective: Create a class to store information about different locations and use class methods to format and display the data. '''
class City:
  def __init__(self,name,country,population,landmarks):
    self.name=name
    self.country=country
    self.population=int(population)
    self.landmarks=landmarks
New_York = City ('New York','USA',400000,['Washington', 'Statue of liberty'])
