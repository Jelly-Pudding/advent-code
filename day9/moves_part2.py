import re

def is_adjacent(head, tail):
    h = abs(head[0] - tail[0]) + abs(head[1] - tail[1])
    if head[0] == tail[0] or head[1] == tail[1]:
        if h <= 1:
            return True
    else:
        if h <= 2:
            return True
    return False

def calculate_move(head, tail):

    # diagonal - top right
    if head[0] < tail[0] and head[1] > tail[1] and abs(head[0] - tail[0]) == 2 and abs(head[1] - tail[1]) == 2:
        return 1, -1

    # diagonal - top left
    if head[0] < tail[0] and head[1] < tail[1] and abs(head[0] - tail[0]) == 2 and abs(head[1] - tail[1]) == 2:
        return 1, 1

    # diagonal - bottom left
    if head[0] > tail[0] and head[1] < tail[1] and abs(head[0] - tail[0]) == 2 and abs(head[1] - tail[1]) == 2:
        return -1, 1

    # diagonal - bottom right 
    if head[0] > tail[0] and head[1] > tail[1] and abs(head[0] - tail[0]) == 2 and abs(head[1] - tail[1]) == 2:
        return -1, -1

    # up and to the right (height difference should be 1)
    if head[0] < tail[0] and head[1] > tail[1] and abs(head[0] - tail[0]) == 1:
        return 0, -1
    
    # up and to the left (height difference should be 1)
    if head[0] < tail[0] and head[1] < tail[1] and abs(head[0] - tail[0]) == 1:
        return 0, 1

    # two spaces up and to the right or left (height difference should be 2)
    if head[0] < tail[0] and abs(head[0] - tail[0]) == 2:
        return 1, 0

    # down and to the left (height difference should be 1)
    if head[0] > tail[0] and head[1] < tail[1] and abs(head[0] - tail[0]) == 1:
        return 0, 1

    # down and to the right (height difference should be 1)
    if head[0] > tail[0] and head[1] > tail[1] and abs(head[0] - tail[0]) == 1:
        return 0, -1

    # two spaces down and to the right or left (height difference should be 2)
    if head[0] > tail[0] and abs(head[0] - tail[0]) == 2:
        return -1, 0

    # simply up
    if head[0] < tail[0]:
        return 1, 0

    # simply down
    if head[0] > tail[0]:
        return -1, 0

    # simply right
    if head[1] > tail[1]:
        return 0, -1

    # simply left
    if head[1] < tail[1]:
        return 0, 1

    return False, False


pattern_up = re.compile(r"U (\d*)")
pattern_down = re.compile(r"D (\d*)")
pattern_right = re.compile(r"R (\d*)")
pattern_left = re.compile(r"L (\d*)")

grid = [["o" for i in range(10000)] for j in range(10000)]
grid[5000][5000] = "H"

current_h = [5000, 5000]
current_t = [[5000, 5000], [5000, 5000], [5000, 5000], [5000, 5000], [5000, 5000], [5000, 5000], [5000, 5000], [5000, 5000], [5000, 5000]]

#for g in grid:
#    print(g)

set_t = set()
set_t.add((current_t[0][0], current_t[0][1]))

with open("input.txt", "r") as f:
    for line in f:
        up = re.match(pattern_up, line.strip())
        down = re.match(pattern_down, line.strip())
        right = re.match(pattern_right, line.strip())
        left = re.match(pattern_left, line.strip())
        if up:
            spaces = int(up.group(1))
            for i in range(spaces):
                grid[current_h[0]][current_h[1]] = "o"
                current_h = [current_h[0] - 1, current_h[1]]
                grid[current_h[0]][current_h[1]] = "H"

                for i in range(9):
                    if i == 0:
                        next = [current_h[0], current_h[1]]
                        directionx = 1
                        directiony = 0
                    else:
                        next = [current_t[i - 1][0], current_t[i - 1][1]]
                        directionx, directiony = calculate_move(next, current_t[i])

                    if not is_adjacent(next, current_t[i]):
                        grid[current_t[i][0]][current_t[i][1]] = "o"
                        current_t[i] = [next[0] + directionx, next[1] + directiony]
                        grid[current_t[i][0]][current_t[i][1]] = str(i)
                        if i == 8:
                            set_t.add((current_t[i][0], current_t[i][1]))
                #for g in grid:
                #    print(g)
                #print("\n\n")


        elif down:
            spaces = int(down.group(1))
            for i in range(spaces):
                grid[current_h[0]][current_h[1]] = "o"
                current_h = [current_h[0] + 1, current_h[1]]
                grid[current_h[0]][current_h[1]] = "H"

                for i in range(9):
                    if i == 0:
                        next = [current_h[0], current_h[1]]
                        directionx = -1
                        directiony = 0
                    else:
                        next = [current_t[i - 1][0], current_t[i - 1][1]]
                        directionx, directiony = calculate_move(next, current_t[i])

                    if not is_adjacent(next, current_t[i]):
                        grid[current_t[i][0]][current_t[i][1]] = "o"
                        current_t[i] = [next[0] + directionx, next[1] + directiony]
                        grid[current_t[i][0]][current_t[i][1]] = str(i)
                        if i == 8:
                            set_t.add((current_t[i][0], current_t[i][1]))
                #for g in grid:
                #    print(g)
                #print("\n\n")

        elif right:
            spaces = int(right.group(1))
            for i in range(spaces):
                grid[current_h[0]][current_h[1]] = "o"
                current_h = [current_h[0], current_h[1] + 1]
                grid[current_h[0]][current_h[1]] = "H"

                for i in range(9):
                    if i == 0:
                        next = [current_h[0], current_h[1]]
                        directionx = 0
                        directiony = -1
                    else:
                        next = [current_t[i - 1][0], current_t[i - 1][1]]
                        directionx, directiony = calculate_move(next, current_t[i])

                    if not is_adjacent(next, current_t[i]):
                        grid[current_t[i][0]][current_t[i][1]] = "o"
                        current_t[i] = [next[0] + directionx, next[1] + directiony]
                        grid[current_t[i][0]][current_t[i][1]] = str(i)
                        if i == 8:
                            set_t.add((current_t[i][0], current_t[i][1]))
                #for g in grid:
                #    print(g)
                #print("\n\n")

        elif left:
            spaces = int(left.group(1))
            for i in range(spaces):
                grid[current_h[0]][current_h[1]] = "o"
                current_h = [current_h[0], current_h[1] - 1]
                grid[current_h[0]][current_h[1]] = "H"

                for i in range(9):
                    if i == 0:
                        next = [current_h[0], current_h[1]]
                        directionx = 0
                        directiony = 1
                    else:
                        next = [current_t[i - 1][0], current_t[i - 1][1]]
                        directionx, directiony = calculate_move(next, current_t[i])

                    if not is_adjacent(next, current_t[i]):
                        grid[current_t[i][0]][current_t[i][1]] = "o"
                        current_t[i] = [next[0] + directionx, next[1] + directiony]
                        grid[current_t[i][0]][current_t[i][1]] = str(i)
                        if i == 8:
                            set_t.add((current_t[i][0], current_t[i][1]))
                #for g in grid:
                #    print(g)
                #print("\n\n")

print(set_t)
print(len(set_t))
