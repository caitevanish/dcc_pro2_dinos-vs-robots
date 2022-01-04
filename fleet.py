from robot import Robot
from weapon import Weapon

class Fleet:
  
  def __init__(self):
    self.robot_list = []
    self.create_fleet()
    

  def create_fleet(self):
    # robot_weapon = Weapon()
    # robot_weapon.pick_weapon()

    weapon1 = Weapon("Cannon", 20)
    robot_one = Robot("T-2022", weapon1)

    weapon2 = Weapon("Sword", 25)
    robot_two = Robot("Sabotage 1000", weapon2)
    
    weapon3 = Weapon("Morning Star", 30)
    robot_three = Robot("MurderPal v2", weapon3)

    self.robot_list.append(robot_one)
    self.robot_list.append(robot_two)
    self.robot_list.append(robot_three)

