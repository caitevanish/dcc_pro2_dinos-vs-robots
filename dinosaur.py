class Dinosaur:

  def __init__(self, name, nickname, attack, attack_power):
    self.name = name
    self.nickname = nickname
    self.health = 100
    self.attack = attack
    self.attack_power = attack_power

      
  def dino_attack(self, robot, fleet_list): #battle() -> dino_turn()
    print(f"It's {self.nickname}'s turn to fight {robot.name}!\n")#hit enter to continue
    robot.health -= self.attack_power
    print(f"\n{self.nickname} {self.attack}s {robot.name}, they are at {robot.health}% power")
    if robot.health <= 0:
      print(f"{self.nickname} beat {robot.name}!")
      fleet_list.remove(robot)


    
    
    
    
     # if (robot.health > 0):
    #   dino_turn == False
    #   print(f"Now it's {robot.name}'s turn")
    #   #append robots health?
    #   return(robot)


      #subtract from robot team 1
      #return results and initiate display_winners method in battlefield class?
      #battlefield.display_winners()    





    # else:
    # pass

#previous LONG version

  # def dino_attack(self, dino, robot): #battle() -> dino_turn()
  #   dino_turn = True
  #   current_attacker = dino
  #   current_defender = robot
  #   defender_health = self.#robot.health
  #   attack = self.attack
  #   attack_power = self.attack_power
    
  #   while (dino_turn == True) and (defender_health > 0):
  #     print(f"It's {current_attacker}'s turn to fight {current_defender}!\n")#hit enter to continue
      
  #     robot.health -= self.attack_power
  #     print(f"\n{current_attacker} {attack}s {current_defender}, they are at {robot.health}% power")      

  #   if (robot.health > 0):
  #     dino_turn == False
  #     print(f"Now it's {current_defender}'s turn")
  #     #append robots health?
  #     return(dino,robot)

  #   else:
  #     print(f"{current_attacker} beat {current_defender}!")
  #     #subtract from robot team 1
  #     #return results and initiate display_winners method in battlefield class?
  #     battlefield.display_winners()


# # bonus text for describing robot's current health:
      # if (defender_health is 75:100):
      #   print(f"{current_defender} is ready to rumble!")
      
      # elif (defender_health is 50:75):
      #   print(f"{current_defender} is looking good")

      # elif (defender_health is 20:50):
      #   print(f"{current_defender} is looking alright, but getting a bit shabby")

      # else: 
      #   print(f"{current_defender} is not looking good!")