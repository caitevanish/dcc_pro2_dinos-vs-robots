class Dinosaur:

  def __init__(self, name, nickname, attack, attack_power):
    self.name = name
    self.nickname = nickname
    self.health = 100
    self.attack = attack
    self.attack_power = attack_power


  def dino_attack(self, dino, robot): #battle() -> dino_turn()
    dino_turn = True
    current_attacker = dino
    current_defender = robot
    defender_health = self.#robot.health
    attack = self.#dino.attack
    attack_power = self.#dino.attack_power
    
    while (dino_turn == True) and (defender_health > 0):
      print(f"It's {current_attacker}'s turn to fight {current_defender}!\n")#hit enter to continue

      if (defender_health is 75:100):
        print(f"{current_defender} is ready to rumble!")
      
      elif (defender_health is 50:75):
        print(f"{current_defender} is looking good")

      elif (defender_health is 20:50):
        print(f"{current_defender} is looking alright, but getting a bit shabby")

      else: 
        print(f"{current_defender} is not looking good!")

      #dino attack, robot health update
      if 
      health_update = defender_health - attack_power
      health_status = 
      print(f"\n{current_attacker} {attack}s {current_defender}, they are at {health_status}")
    

    else:
      dino_turn == False
      #append robots health
      return(dino,robot)
    



    self.robot = attack_powe


    if self.health > 0:


    # else:
    # pass

