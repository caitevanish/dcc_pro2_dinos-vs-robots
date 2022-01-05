from weapon import Weapon
import random

class Robot:

  def __init__(self, name, weapon):
    self.name = name
    self.weapon = weapon
    self.health = 100

  def robot_attack(self, dinosaur, herd_list):
    print(f"Here comes {self.name}, watch out {dinosaur.nickname}!\n")

    dinosaur.health -= self.weapon.attack_power
    print(f"{self.name} attacks {dinosaur.nickname} with his {self.weapon.name}, knocking {dinosaur.nickname}'s health to {dinosaur.health}.")

    if dinosaur.health <= 0:
      print(f"{self.name} beat {dinosaur.nickname}!")
      herd_list.remove(dinosaur) 



    # self.selected_weapon = weapon
    # self.select_weapon()

    # self.weapon1 = Weapon("Cannon", 20)
    # self.weapon2 = Weapon("Sword", 25)
    # self.weapon3 = Weapon("Morning Star", 30)


  # def select_weapon(self):
  #   random.choice([self.weapon1, self.weapon2, self.weapon3])
  #   return


    