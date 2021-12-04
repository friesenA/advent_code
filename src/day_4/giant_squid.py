"""Giant Squid"""

class Board:
  
  def __init__(self, rows):
    self.rows = [0] * 5
    self.columns = [0] * 5
    self.board = [[int(x) for x in row.split()] for row in rows]
    
  def mark(self, num):
    for r, row in enumerate(self.board):
      for c, col in enumerate(row):
        if col == num:
          self.rows[r] += 1
          self.columns[c] += 1
          self.board[r][c] = -1
          break
   
  def check_win(self):
    for row, col in zip(self.rows, self.columns):
      if row == 5 or col == 5:
        return True
    return False
    
    
def play_game_to_win(boards, random_draws):
  for draw in random_draws:
    for board in boards:
      board.mark(draw)
      if board.check_win():
        return board, draw
  raise Exception
  
  
def play_game_to_lose(boards, random_draws):
  for draw in random_draws:
    count = len(boards)
    removal = []
    for board in boards:
      board.mark(draw)
      if board.check_win():
        if count > 1:
          count -= 1
          removal.append(board)
        else:
          return board, draw
    if removal:
      for x in removal:
        boards.remove(x)
  raise Exception
        
        
def calculate_score(board, draw):
  total = sum([sum([x for x in row if x != -1]) for row in board.board])
  return total * draw
      

if __name__ == '__main__':
  with open('data2.txt') as f:
    random_draws = [int(x) for x in f.readline().split(',')]
    
    boards = []
    while (empty_line := f.readline()):
        boards.append(Board([f.readline().rstrip() for _ in range(5)]))
        
#   board, draw = play_game_to_win(boards, random_draws)
#   print(f'Winning score: {calculate_score(board, draw)}')
  
  board, draw = play_game_to_lose(boards, random_draws)
  print(f'Losing score: {calculate_score(board, draw)}')
