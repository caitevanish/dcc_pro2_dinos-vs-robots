# [dino] [attack]s [robo] and does [int] damage.
# [robo] counters the attack and
from _typeshed import Self
from herd import Herd
from fleet import Fleet
from battlefield import Battlefield

battlefield = Battlefield()
battlefield.run_game()

class Battlefield:

  def __init__(self):
    self.fleet = Fleet()
    self.herd = Herd()

 
  def run_game(self):
    self.display_welcome()
    #self.introduction()
    #self.begin_game()
    self.round_one()


  def round_one(self):
    robot_health = Fleet(self.robot_list.robot_one.health)
    print(robot_health)
    #dino_health =  
    #attack
    #self.first_attack = (fleet.robot_list.robot_one.health)   