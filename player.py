class Player:
  def __init__(self, name, age, speed, strength, smorts, kindness, goofiness):
    self.name = name
    self.age = age
    self.speed = speed
    self.strength = strength
    self.smorts = smorts
    self.kindness = kindness
    self.goofiness = goofiness

    if (speed + strength + smorts + kindness + goofiness != 25):
      raise('Total not 25') 
  
  def edit(self, cat, amount):
    if cat == 'speed':
      self.speed += amount;
    elif cat == 'strength':
      self.strenth += amount;
    elif cat == 'smorts':
      self.smorts += amount;
    elif cat == 'kindness':
      self.kindness += amount;
    elif cat == 'goofiness':
      self.goofiness += amount;
    else:
      raise('Edit function failed')

p1 = Player("Maggie", 18, 5, 5, 5, 5, 5)

print(p1.name)
print(p1.speed)
p1.edit("speed", 10)
print(p1.speed) 