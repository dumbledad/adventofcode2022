from functools import cached_property
import sys
import re

class Cave:
  def __init__(self, filename):
    self.start = (500, 0)
    with open(filename) as file:
      self.data = file.read()
    self.grid = []
    for _ in range(self.bounds['max_y'] + 1):
      self.grid.append(['.'] * (self.bounds['max_x'] + 1))
    for line in self.data.splitlines(): # Overlapping regex too hard
      coords = line.split(' -> ')
      for idx in range(len(coords)):
        if idx + 1 < len(coords):
          start_line = tuple([int(num) for num in coords[idx].split(',')])
          end_line = tuple([int(num) for num in coords[idx + 1].split(',')])
          for x in range(start_line[0], end_line[0] + 1):
            for y in range(start_line[1], end_line[1] + 1):
              self.grid[y][x] = '#'
    self.grid[self.start[1]][self.start[0]] = '+'


  @cached_property
  def bounds(self):
    bounds = { 
      'min_x': self.start[0],
      'max_x': self.start[0],
      'min_y': self.start[1],
      'max_y': self.start[1]
    }
    for line in self.data.splitlines():
      for match in re.finditer(r'(\d+),(\d+)', self.data):
        if int(match.group(1)) < bounds['min_x']:
          bounds['min_x'] = int(match.group(1))
        elif int(match.group(1)) > bounds['max_x']:
          bounds['max_x'] = int(match.group(1))
        if int(match.group(2)) < bounds['min_y']:
          bounds['min_y'] = int(match.group(2))
        elif int(match.group(2)) > bounds['max_y']:
          bounds['max_y'] = int(match.group(2))
    return bounds

  def draw(self):
    for i, row in enumerate(self.grid):
      print(f"{i} {''.join(row[self.bounds['min_x'] - 1:])}")
