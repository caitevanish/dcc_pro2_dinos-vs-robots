from weapon import Weapon

class Robot:

  def __init__(self, name):
    self.name = name
    self.health = 100
    self.selected_weapon = ""
    self.select_weapon()
    self.weapon1 = Weapon("Cannon", -20)
    self.weapon2 = Weapon("Sword", -25)
    self.weapon3 = Weapon("Morning Star", -30)

  def select_weapon(self):
    pass
  
  # def attack(self, dinosaur):
  #     is_alive !=  True 
  #   pass


  # def name_robot(self):
  #   pass


  # def health_robot(self):
  #   pass