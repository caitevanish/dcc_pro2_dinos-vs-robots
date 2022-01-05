from fleet import Fleet 
from herd import Herd 

class Battlefield:

  def __init__(self):
    self.fleet = Fleet()
    print('done 1')
    self.herd = Herd()
    print('done 2')

  
  def run_game(self):
    self.display_welcome()
    self.introduction()
    print('done 3')
    self.begin_game()
    print('done 4')
    self.battle()
    self.show_dino_options() #TESTED




# Test Loop----------------      
   # self.test()

  # def test(self):
  #   for dinosaur in self.herd.herd_list:
  #     print(f'{dinosaur.nickname} + {dinosaur.attack} + {dinosaur.attack_power}')

  # def test(self):
  #   for robot in self.fleet.robot_list:
  #     print(f'{robot.name} + {robot.weapon.name} + {robot.weapon.attack_power}')
# #-----------------


#---------------------------------------------------

  def display_welcome(self):
    print("\nWelcome to the epic battle of the millenia! Meet the furious fleet of robots:\n")

    for robot in self.fleet.fleet_list:
      print(robot.name)

    print("\nAnd of the Jurassic weight class, give it up for the horrible herd:\n")

    for dinosaur in self.herd.herd_list:
      print(f'{dinosaur.name}, aka, {dinosaur.nickname}')

  def introduction(self):
    print("\nNow we aren’t here to have a tea party, we’re here to FIGHT!! \n \nEach of our dinosaurs has their own special attack that they can perform:\n")
    
    for dinosaur in self.herd.herd_list:
      print(f'{dinosaur.nickname} can {dinosaur.attack}')
 
    print("\nThe robots are armed as well:\n")

    for robot in self.fleet.fleet_list:
      print(f'{robot.name} has a {robot.weapon.name}')

  def begin_game(self):
    user_answer = input("\nNow that you've met the players, are you ready to begin?: ")
    if user_answer == 'yes':
      print("Let's do it!")
    else: 
      print("Okay bye")

  def battle(self):
    #while loop between teams
    #while both lists longer than 0, continue going through battle sequence
    #self.herd.herd_list = []
    #self.fleet.fleet_list = []
    # TESTED dino_attack 
    self.herd.herd_list[0].dino_attack(self.fleet.fleet_list[0], self.fleet.fleet_list)
    # need to test robot_attack

  def round_one(self, dino):
    self.herd.herd_list[0] = dino
    first_dino = self.herd.herd_list[0]
    print(first_dino)

    # self.fleet.fleet_list[0] = robot
    # return(dino,robot)
    
    # for dino in self.herd.herd_list:
    #   print(f'{.nickname} + {robot.weapon.name} + {robot.weapon.attack_power}')


  # def round_one(self):
  #   robot_health = Fleet(robot_list.health)
  #   print(robot_health)
  #   dino_health =  
  #   attack
  #   self.first_attack = (fleet.robot_list.robot_one.health)  
#---------------------------------------------------

   # battle is mainly calling dino_turn and robot_turn
  # def battle(self):
    
    pass
  # this is where the attack method should be called to have them actually fight
  # self.fleet.robot_one.attack(dino_one)
  def dino_turn(self):
    #dinosaur.attack()
    pass

  # def robo_turn(self, robot):
  #   #robo.attack
  #   counter = 0
  #   round_count = counter += 1
  #   pass

  def show_dino_options(self):
    print("Dinosaurs Availalbe to Choose")
    index_refrence = 0
    for dino in self.herd.herd_list:
      print(f'Press {index_refrence} to select {dino.name} ({dino.health} health)')
      index_refrence += 1
    pass

  def show_robo_options(self):
    pass

  # def display_winners(self):
    pass




