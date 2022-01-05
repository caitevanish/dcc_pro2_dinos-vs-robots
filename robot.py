from weapon import Weapon
import random

class Robot:

  def __init__(self, name, weapon):
    self.name = name
    self.weapon = weapon
    self.health = 100

  def robot_attack(self, dinosaur, herd_list):
    input(f"\nHere comes {self.name}, watch out {dinosaur.nickname}!\n")

    dinosaur.health -= self.weapon.attack_power
    input(f"{self.name} attacks {dinosaur.nickname} with his {self.weapon.name}, knocking {dinosaur.nickname}'s health to {dinosaur.health}.")

    if dinosaur.health <= 0:
      input(f"{self.name} beat {dinosaur.nickname}!")
      herd_list.remove(dinosaur) 