# polymorphism （多态）

python里面的多态比较简单，它会直接根据当前实际的对象去调用对应的方法，比如：

```
class Player(object):
  pass

class Human(Player):
  def play(self):
    print "Human plays."

class Computer(Player):
  def play(self):
    print "Computer plays."

map(lambda x:x.play(), [Human(), Computer()])
```
