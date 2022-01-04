from fleet import Fleet 
from herd import Herd 

class Battlefield:

  def __init__(self):
    self.fleet = Fleet()
    self.herd = Herd()
  
  
  def run_game(self):
    self.display_welcome()
    #print the list of the robots
    #print the list of the dinosaurs  


  def display_welcome(self):
    print("welcome to RVD")
    pass

   # battle is mainly calling dino_turn and robot_turn
  def battle(self):
    pass
  # this is where the attack method should be called to have them actually fight
  # self.fleet.robot_one.attack(dino_one)
  def dino_turn(self):
    pass

  def robo_turn(self, robot):
    pass

  def show_dino_opponent_options(self):
    pass

  def show_robo_opponent_options(self):
    pass

  def display_winners(self):
    pass