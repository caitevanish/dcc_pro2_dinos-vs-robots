from fleet import Fleet 
from herd import Herd 

class Battlefield:

  def __init__(self):
    self.fleet = Fleet()
    print('done 1')
    self.herd = Herd()
    print('done 2')

  def run_game(self):
    self.display_welcome() #TESTED
    self.introduction() #TESTED
    self.begin_game() #TESTED
    self.battle() #This is the scenic route to the end.

    # Quick_battle() is a shortcut. 
    #Comment out self.battle() and uncomment quick_battle below
    #self.quick_battle()  
    
    self.display_winners()

#---------------------------------------------------

  def display_welcome(self):
    print("\nWelcome to the epic battle of the millenia! \nMeet the furious fleet of robots:\n")

    for robot in self.fleet.fleet_list:
      print(robot.name)

    print("\nAnd of the Jurassic weight class, give it up for this horrible herd:\n")

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
    if user_answer == 'yes' or 'y':
      print("Let's do it!\n")
    elif user_answer == 'no' or 'n':
      print("Okay bye")
      quit()
    # else: 
    #   Make a varificationstep here to restart when an incorrect input has been made
  

  def battle(self):
    while len(self.fleet.fleet_list) > 0 and len(self.herd.herd_list) > 0:
      self.dino_turn()
      if len(self.fleet.fleet_list) == 0:
        pass
      else:
        self.robo_turn()

# #Get to the end faster
  #def quick_battle(self):
    # self.herd.herd_list = ["Docus"]
    # self.fleet.fleet_list = []
    # if (len(self.herd.herd_list) != 0):
    #   self.display_winners()

#---------------------------------------------------

  def dino_turn(self):

    #Fix so that if the wrong button is pushed, person can resubmit answer!!!
    self.show_dino_options()
    dino_index = int(input("\n"))
    self.show_robo_options()
    robot_index = int(input("\n"))
    
    self.herd.herd_list[dino_index - 1].dino_attack(self.fleet.fleet_list[robot_index - 1], self.fleet.fleet_list)

    # pass

  def robo_turn(self):

    self.show_robo_options()
    robot_index = int(input("\n"))
    self.show_dino_options()
    dino_index = int(input("\n"))
    
    self.fleet.fleet_list[robot_index - 1].robot_attack(self.herd.herd_list[dino_index - 1], self.herd.herd_list)

  def show_dino_options(self):
    print("\nChoose a dinosaur to send to battle: \n")
    index_reference = 1
    for dinosaur in self.herd.herd_list:
      print(f'Press {index_reference} to select {dinosaur.nickname} [health level: {dinosaur.health} | Attack style: {dinosaur.attack}]')
      index_reference += 1
    
  def show_robo_options(self):
    print("\nChoose a robot to send to battle: \n")
    index_reference = 1
    for robot in self.fleet.fleet_list:
      print(f'Press {index_reference} to select {robot.name} [Power level: {robot.health} | weapon: {robot.weapon.name}]')
      index_reference += 1


  def display_winners(self):
    if (len(self.herd.herd_list) > 0):
      print(f'Congratulations to the Horrible Herd of Dinosaurs! {self.herd.herd_list.nickname} is the last killer standing!')
    else:
      print(f'Congratulations to the Furious Fleet of Robots! {self.fleet.fleet_list.name} is the last killer standing!')


# Test Loop----------------      
   # self.test()

  # def test(self):
  #   for dinosaur in self.herd.herd_list:
  #     print(f'{dinosaur.nickname} + {dinosaur.attack} + {dinosaur.attack_power}')

  # def test(self):
  #   for robot in self.fleet.robot_list:
  #     print(f'{robot.name} + {robot.weapon.name} + {robot.weapon.attack_power}')
# #-----------------