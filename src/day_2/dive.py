"""Dive!"""

class Position:

  def __init__(self):
    self.depth = 0
    self.lateral = 0
    
  def move(self, command):
    getattr(self, command.action)(command.qty)
    
  def forward(self, qty):
    self.lateral += qty
    
  def down(self, qty):
    self.depth += qty
    
  def up(self, qty):
    self.depth -= qty


class Command:
  
  def __init__(self, action, qty):
    self.action = action
    self.qty = qty
    

if __name__ == '__main__':
  commands = []
  with open('data.txt') as f:
    for line in f.readlines():
      action, qty = line.replace('\n', '').split(' ')
      commands.append(Command(action, int(qty)))
  
  position = Position()
  for command in commands:
    position.move(command)
    
  print(position.depth * position.lateral)
      
    
  
