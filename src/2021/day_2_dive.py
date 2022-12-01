"""Dive!"""

class Position:

  def __init__(self):
    self.depth = 0
    self.horizontal = 0
    self.aim = 0
    
  def move(self, command):
    getattr(self, command.action)(command.qty)
    
  def forward(self, qty):
    self.horizontal += qty
    self.depth += self.aim * qty
    
  def down(self, qty):
    self.aim += qty
    
  def up(self, qty):
    self.aim -= qty


class Command:
  
  def __init__(self, action, qty):
    self.action = action
    self.qty = qty
    

if __name__ == '__main__':
  commands = []
  with open('day2_data.txt') as f:
    for line in f.readlines():
      action, qty = line.replace('\n', '').split(' ')
      commands.append(Command(action, int(qty)))
  
  position = Position()
  for command in commands:
    position.move(command)
    
  print(position.depth * position.horizontal)
      
    
  
