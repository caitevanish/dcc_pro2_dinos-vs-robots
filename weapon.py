class Weapon:

  def __init__(self, name, attack_power):
    self.name = name
    self.power = attack_power

  
  # # I should take this out because the user cannot add their own weapons, right?:

  # def add_weapon(self, name):
  #   self.name = input("Add a new weapon: ")
  #   return
  #   pass

  # def attack_power(self):
    # self.power = 
    # pass

weapon1 = Weapon("Cannon", -20)
weapon2 = Weapon("Sword", -25)
weapon3 = Weapon("Morning Star", -30)

# #Testing out whether I can use the debugger here (it didn't work):

# Weapon.add_weapon(self, self.name)
