import re

class Directory:
  def __init__(self, name):
    self.name = name
    self.contents = []
    self.size = 0

  def add_content(self, item) -> None:
    self.contents.append(item)
    if isinstance(item, File):
      self.size += item.size

  def get_directory(self, name):
    for item in self.contents:
      if isinstance(item, Directory) and item.name == name:
        return item

  @property
  def totalsize(self) -> int:
    return self.size + sum([x.totalsize for x in self.contents if isinstance(x, Directory)])


class File:
  def __init__(self, name, size) -> None:
    self.name = name
    self.size = size


def construct_filesystem(dataset) -> Directory:
  root = Directory("/")
  position = []
  line_num = 0
  while line_num < len(dataset):
    if dataset[line_num][0] == "$":
      if dataset[line_num][2:4] == "cd":
        change_directory(dataset[line_num][5:], position, root)
        line_num += 1
      else:
        x = line_num + 1
        while(x < len(dataset) and dataset[x][0] != "$"):
          if match := re.match(r'^(\d+)\s{1}([\w.]+)$', dataset[x]):
            position[-1].add_content(File(match.group(2), int(match.group(1))))
          else:
            position[-1].add_content(Directory(dataset[x][4:]))
          x += 1
        line_num = x
  return root


def change_directory(value, position, root):
  if value == "/":
    position.clear()
    position.append(root)
  elif value == "..":
    position.pop()
  else:
    dir = position[-1]
    position.append(dir.get_directory(value))
    

def find_directory_sizes(root: Directory, maximum = 70000000, minimum = 0):
  contained_dir = [x for x in root.contents if isinstance(x, Directory)]
  result = []
  if root.totalsize <= maximum and root.totalsize >= minimum:
    result.append(root.totalsize)

  if not contained_dir:
    return result
  else:
    for dir in contained_dir:
      result.extend(find_directory_sizes(dir, maximum, minimum))
    return result


if __name__ == '__main__':
  with open('src/2022/day7_data.txt') as f:
    dataset = [line.replace('\n', '') for line in f.readlines()]

  filesystem = construct_filesystem(dataset)
  dir_sizes = find_directory_sizes(filesystem, maximum=100000)
  print(f"Part 1: {sum(dir_sizes)}")

  space_needed = 30000000 - (70000000 - filesystem.totalsize)
  dir_to_delete = find_directory_sizes(filesystem, minimum=space_needed)
  print(f"Part 2: {min(dir_to_delete)}")

