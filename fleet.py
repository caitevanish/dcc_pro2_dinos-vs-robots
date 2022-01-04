from robot import Robot

class Fleet:
  
  def __init__(self):
    self.robot_list = []
    self.create_fleet()
    

  def create_fleet(self):
    robot_one = Robot("T-2022")
    robot_two = Robot("Sabotage 1000")
    robot_three = Robot("MurderPal v2")

    self.robot_list.append(robot_one)
    self.robot_list.append(robot_two)
    self.robot_list.append(robot_three)

