from collections import defaultdict

lst = []
with open("input.txt", "r") as f:
    for line in f:
        lst.append(line.strip())

def draw_cave(paths):
  lol = []
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
    lol.append(''.join(cave[(x, y)] for x in range(min_x, max_x + 1)))
  
  return result, lol

def simulate(state):
    # Convert the state to a list of lists
    state = [list(row) for row in state]

    # Find the starting position of the o
    start_row, start_col = None, None
    for i, row in enumerate(state):
        if '+' in row:
            start_row = i
            start_col = row.index('+')
            break
    # Initialize the current position of the o and the rest flag
    cur_row, cur_col = start_row, start_col
    counter = 0
    while True:
        # Keep moving the o down until it can't go any further
        while cur_row < len(state) - 1 and state[cur_row + 1][cur_col] == '.':
            cur_row += 1

        # Try to move it diagonally.
        if cur_row < len(state) - 1:
            # Try to move the o diagonally to the left.
            if cur_col > 0 and state[cur_row + 1][cur_col - 1] == '.':
                cur_row += 1
                cur_col -= 1
                continue
            # If that's not possible, try to move the o diagonally to the right.
            elif cur_col < len(state[0]) - 1 and state[cur_row + 1][cur_col + 1] == '.':
                cur_row += 1
                cur_col += 1
                continue
            # Out of bounds stuff now.
            elif cur_col == 0 or cur_col == len(state[0]) - 1:
                break
            else:
                state[cur_row][cur_col] = "o"
                counter += 1
                cur_row, cur_col = start_row, start_col
    return state, counter

cave = draw_cave(lst)[1]
print(simulate(cave)[1])