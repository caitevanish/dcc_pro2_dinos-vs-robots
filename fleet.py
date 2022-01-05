from robot import Robot
from weapon import Weapon

class Fleet:
  
  def __init__(self):
    self.fleet_list = []
    self.create_fleet()
    

  def create_fleet(self):
    # robot_weapon = Weapon()
    # robot_weapon.pick_weapon()

    weapon = Weapon("Cannon", 20)
    robot_one = Robot("T-2022", weapon)

    weapon = Weapon("Sword", 25)
    robot_two = Robot("Sabotage 1000", weapon)
    
    weapon = Weapon("Morning Star", 30)
    robot_three = Robot("MurderPal v2", weapon)

    self.fleet_list.append(robot_one)
    self.fleet_list.append(robot_two)
    self.fleet_list.append(robot_three)

