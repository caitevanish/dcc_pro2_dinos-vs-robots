from fleet import Fleet 
from herd import Herd 

class Battlefield:

  def __init__(self):
    self.fleet = Fleet()
    self.herd = Herd()
    print('done')
  
  # def __repr__(self) -> str:
  #     pass
  
  def run_game(self):
    self.display_welcome()
    #print the list of the robots
    #print the list of the dinosaurs  

#---------------------------------------------------

  def display_welcome(self):
    print("\nWelcome to the epic battle of the millenia! Meet the furious fleet of robots:\n")
    
    for robot in self.fleet.robot_list:
      print(robot.name)

    print("\nAnd of the Jurassic weight class, give it up for the horrible herd:\n")

    for dinosaur in self.herd.herd_list:
      print(dinosaur.name)


 

      

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