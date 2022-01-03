from robot import Robot

class Fleet:
  
  def __init__(self):
    self.robot_list = []
    self.create_fleet()
    

  def create_fleet(self):
    robot_one = Robot("WALL-E")
    robot_two = Robot("Marvin the Android")
    robot_three = Robot("The Iron Giant")

    self.robot_list.append(robot_one)
    self.robot_list.append(robot_two)
    self.robot_list.append(robot_three)
    pass


