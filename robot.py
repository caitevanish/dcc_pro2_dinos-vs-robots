from weapon import Weapon

class Robot:

  def __init__(self, name, attack_power):
    self.name = name
    self.attack_power = attack_power
    self.health = 100
    self.weapon1 = Weapon("Cannon", -20)
    self.weapon2 = Weapon("Sword", -25)
    self.weapon3 = Weapon("Morning Star", -30)

  def attack(self, dinosaur):
    
    pass


  # def name_robot(self):
  #   pass


  # def health_robot(self):
  #   pass