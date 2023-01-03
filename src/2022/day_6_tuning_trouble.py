
def find_start_marker(datastream: str, num_of_uniques = 4):
  for x in range(num_of_uniques, len(datastream)):
    if unique_char(datastream[x-num_of_uniques:x]):
      return x
      

def unique_char(string: str):
  for char in string:
    if len(string.replace(char, "")) < len(string) - 1:
      return False
  return True


if __name__ == '__main__':
  with open('src/2022/day6_data.txt') as f:
    datastream = f.readline().rstrip()

  packet_start = find_start_marker(datastream, 4)
  message_start = find_start_marker(datastream, 14)
  print(f"Part 1: {packet_start}")
  print(f"Part 2: {message_start}")