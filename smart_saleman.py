"""
    My solution fo the saleman problem.
    Works with the .txt file given in input
"""

import sys
from math import sqrt
from random import shuffle

def main():
  lines = io_file()
  points = create_points(lines)

  path = get_path(points)
  l = trip_length(points)

  for i in range(10000):
    points = my_shuffle(points)
    l_tmp = trip_length(points)
    if l_tmp < l:
      l = l_tmp
      path = get_path(points)

  print("Shortest path is:")
  print(*path, sep=' -> ')
  print("With a total length of %d" % l)

# ----------------------------------------------------------------------------

def my_shuffle(points):
  tmp = points[2:]
  shuffle(tmp)
  points[2:] = tmp
  return points

# ----------------------------------------------------------------------------

def get_path(points):
  """
  Return list of path points.
  """
  path = []
  for point in points:
    path.append(point[0])
  return path

# ----------------------------------------------------------------------------

def trip_length(points):
  """
  Compute total trip length.
  """
  l = 0
  previous = None
  for point_struct in points:
    if previous:
      l += point_struct[1].length(previous)
    previous = point_struct[1]
  return int(l)

# ----------------------------------------------------------------------------

class Point():
  """
  Class for coordinates.
  Attributs are 'x' and 'y'.
  """
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def length(self, point):
    """
    Length between self and point.
    """
    return sqrt((point.x - self.x) ** 2 + (point.y - self.y) ** 2)

  def __str__(self):
    """
    Printable representation of a Point.
    """
    return '(%d, %d)' % (self.x, self.y)

# ----------------------------------------------------------------------------

def create_points(lines):
  """
  Create a dict of point with key a number and value a point.
  """
  points = []
  count = 1
  for line in lines:
    line = line.strip().split(' ')
    point = Point(int(line[0]), int(line[-1]))
    points.append([count, point])
    count += 1
  return points

# ----------------------------------------------------------------------------

def io_file():
  """
  Open file given in input and fill a list of lines.
  """
  try:
    fi = open(sys.argv[1])
  except:
    print("File error.")
    sys.exit(1)

  lines = fi.readlines()
  fi.close()
  return lines

# ----------------------------------------------------------------------------

if __name__ == '__main__':
  main()
