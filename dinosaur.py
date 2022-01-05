class Dinosaur:

  def __init__(self, name, nickname, attack, attack_power):
    self.name = name
    self.nickname = nickname
    self.health = 100
    self.attack = attack
    self.attack_power = attack_power

      
  def dino_attack(self, robot, fleet_list):
    input(f"\nIt's {self.nickname}'s turn to fight {robot.name}!\n")
    # print(f"It's {self.nickname}'s turn to fight {robot.name}!\n")

    robot.health -= self.attack_power
    input(f"{self.nickname} {self.attack}s {robot.name}. {robot.name} is at {robot.health}% power\n")
    
    if robot.health <= 0:
      input(f"{self.nickname} beat {robot.name}!")
      fleet_list.remove(robot)


    
    
    
    

# # bonus text for describing robot's current health:
      # if (defender_health is 75:100):
      #   print(f"{current_defender} is ready to rumble!")
      
      # elif (defender_health is 50:75):
      #   print(f"{current_defender} is looking good")

      # elif (defender_health is 20:50):
      #   print(f"{current_defender} is looking alright, but getting a bit shabby")

      # else: 
      #   print(f"{current_defender} is not looking good!")