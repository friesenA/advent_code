"""Binary Diagnostic"""


def most_common_bit(data, bit):
  total = len(data)
  value = sum([int(x[bit]) for x in data])
  if total - value > value:
    return 0
  else:
    return 1

def power_consumption(data):
  width = len(data[0])

  epsilon = ''
  gamma = ''
  
  for i in range(width):
    common = most_common_bit(data, i)
    gamma += str(common)
    epsilon += str(1 - common)
      
  epsilon = int('0b' + epsilon, 2)
  gamma = int('0b' + gamma, 2)
  
  return epsilon * gamma


def life_support(data):
  oxygen_data = data.copy()
  co2_data = data.copy()
  width = len(data[0])
  
  for i in range(width):
    common = most_common_bit(oxygen_data, i)
    oxygen_data = [x for x in oxygen_data if x[i] == str(common)]
    if len(oxygen_data) < 2:
      break
    
  for i in range(width):
    uncommon = 1 - most_common_bit(co2_data, i)
    co2_data = [x for x in co2_data if x[i] == str(uncommon)]
    if len(co2_data) < 2:
      break
  
  oxygen = int('0b' + oxygen_data[0], 2)
  co2 = int('0b' + co2_data[0], 2)
  
  return oxygen * co2


if __name__ == '__main__':
  with open('data.txt') as f:
    data = [line.replace('\n', '') for line in f.readlines()]
  
  print(power_consumption(data))
  print(life_support(data))
