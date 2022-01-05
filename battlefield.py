from fleet import Fleet 
from herd import Herd 

class Battlefield:

  def __init__(self):
    self.fleet = Fleet()
    self.herd = Herd()
    #print('done')

  
  def run_game(self):
    self.display_welcome()
    #self.introduction()
    #self.begin_game()
    self.round_one()
    print(len(robot_list))

    self.battle()



#---------------------------------------------------

  def display_welcome(self):
    print("\nWelcome to the epic battle of the millenia! Meet the furious fleet of robots:\n")

    for robot in self.fleet.robot_list:
      print(robot.name)

    print("\nAnd of the Jurassic weight class, give it up for the horrible herd:\n")

    for dinosaur in self.herd.herd_list:
      print(f'{dinosaur.name}, aka, {dinosaur.nickname}')

  def introduction(self):
    print("\nNow we aren’t here to have a tea party, we’re here to FIGHT!! \n \nEach of our dinosaurs has their own special attack that they can perform:\n")
    
    for dinosaur in self.herd.herd_list:
      print(f'{dinosaur.nickname} can {dinosaur.attack}')
 
    print("\nThe robots are armed as well:\n")

    for robot in self.fleet.robot_list:
      print(f'{robot.name} has a {robot.weapon.name}')

  def begin_game(self):
    user_answer = input("\nNow that you've met the players, are you ready to begin?: ")
    if user_answer == 'yes':
      print("Let's do it!")
    else: 
      print("Okay bye")
  
  robot_list_length = len(self.fleet.robot_list)
  print(robot_list_length)

  #def round_one(self):
    # robot_health = Fleet(robot_list.health)
    # print(robot_health)
    #dino_health =  
    #attack
    #self.first_attack = (fleet.robot_list.robot_one.health)  
#---------------------------------------------------

   # battle is mainly calling dino_turn and robot_turn
  def battle(self):
    pass
  # this is where the attack method should be called to have them actually fight
  # self.fleet.robot_one.attack(dino_one)
  def dino_turn(self):
    #dinosaur.attack()
    pass

  def robo_turn(self, robot):
    #robo.attack
    counter = 0
    round_count = counter += 1
    pass

  def show_dino_opponent_options(self):
    pass

  def show_robo_opponent_options(self):
    pass

  def display_winners(self):
    pass