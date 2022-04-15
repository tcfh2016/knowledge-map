class Player(object):
  pass

class Human(Player):
  def play(self):
    print "Human plays."

class Computer(Player):
  def play(self):
    print "Computer plays."

map(lambda x:x.play(), [Human(), Computer()])
