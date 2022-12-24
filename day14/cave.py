from collections import defaultdict

lst = []
with open("input.txt", "r") as f:
    for line in f:
        lst.append(line.strip())

def draw_cave(paths):
  # Create a map of the cave
  cave = defaultdict(lambda: '.')
  
  # Set the source of the sand to +
  cave[(500, 0)] = '+'
  
  # Add the paths to the cave map
  for path in paths:
    # Split the path into a list of points
    points = path.split(' -> ')
    
    # Connect the points with # characters
    for i in range(len(points) - 1):
      x1, y1 = map(int, points[i].split(','))
      x2, y2 = map(int, points[i+1].split(','))
      
      # Add the # characters to the cave map
      if x1 == x2:
        # The path is vertical
        for y in range(min(y1, y2), max(y1, y2) + 1):
          cave[(x1, y)] = '#'
      elif y1 == y2:
        # The path is horizontal
        for x in range(min(x1, x2), max(x1, x2) + 1):
          cave[(x, y1)] = '#'
  
  # Find the dimensions of the cave
  min_x = min(x for x, y in cave)
  max_x = max(x for x, y in cave)
  min_y = min(y for x, y in cave)
  max_y = max(y for x, y in cave)
  
  # Initialize the result string
  result = ''
  
  # Add each row of the cave to the result string
  for y in range(min_y, max_y + 1):
    result += ''.join(cave[(x, y)] for x in range(min_x, max_x + 1)) + '\n'
  
  return result

print(draw_cave(lst))

