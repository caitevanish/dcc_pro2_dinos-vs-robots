from dinosaur import Dinosaur

class Herd:

  def __init__(self):
    self.herd_list = []
    self.create_herd()

  def create_herd(self):
    dino_one = Dinosaur("Tyrannosaurus Rex", "T-bone", "bite", 25)
    dino_two = Dinosaur("Pachycephalosaurus","Pach-o", "ram", 30)
    dino_three = Dinosaur("Diplodocus", "Docus", "whip", 20)

    self.herd_list.append(dino_one)
    self.herd_list.append(dino_two)
    self.herd_list.append(dino_three)

    
