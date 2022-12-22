lst = []

with open("input.txt", "r") as f:
    for line in f:
        line = line.strip()
        lst.append([])
        for idx in range(len(line)):
            lst[-1].append(line[idx])
            if line[idx] == "S":
                start = (len(lst) - 1, idx)
                lst[-1][-1] = "a"
            elif line[idx] == "E":
                end = (len(lst) - 1, idx)
                lst[-1][-1] = "z"
print(lst)
print(start, end)

def get_possible_moves(coords_x, coords_y):
    moves = []
    # up?
    if coords_x - 1 >= 0:
        if ord(lst[coords_x][coords_y]) - 96 + 1 >= ord(lst[coords_x - 1][coords_y]) - 96:
            moves.append((coords_x - 1, coords_y))
    # down?
    if coords_x + 1 <= len(lst) - 1:
        if ord(lst[coords_x][coords_y]) - 96 + 1 >= ord(lst[coords_x + 1][coords_y]) - 96:
            moves.append((coords_x + 1, coords_y))
    # right ?
    if coords_y + 1 <= len(lst[coords_x]) - 1:
        if ord(lst[coords_x][coords_y]) - 96 + 1 >= ord(lst[coords_x][coords_y + 1]) - 96:
            moves.append((coords_x, coords_y + 1))
    # left ?
    if coords_y - 1 >= 0:
        if ord(lst[coords_x][coords_y]) - 96 + 1 >= ord(lst[coords_x][coords_y - 1]) - 96:
            moves.append((coords_x, coords_y - 1))
    return moves

move = get_possible_moves(3, 4)
print(move)
            