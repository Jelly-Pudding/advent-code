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

def manhattan_distance(node):
    h = abs(node[0] - end[0]) + abs(node[1] - end[1])
    return h

def a_star():
    path = []
    open_list = []
    closed_list = []
    open_list.append({"the_node": start, "parent": None, "g_value": 0, "f_value": 0})
    while open_list != []:
        dict_with_lowest_f_value = min(open_list, key=lambda x:x["f_value"])
        current_node = dict_with_lowest_f_value["the_node"]
        parent_of_current_node = dict_with_lowest_f_value["parent"]
        current_node_g_value = dict_with_lowest_f_value["g_value"]  
        current_node_index = next((index for (index, d) in enumerate(open_list) if d["the_node"] == current_node), None)
        open_list.pop(current_node_index)
        closed_list.append(dict_with_lowest_f_value)
        children = get_possible_moves(current_node[0], current_node[1])
        for child in children:
            parent = current_node
            child_dist_from_start = current_node_g_value + 1
            child_dist_from_end = manhattan_distance(child)
            child_f = child_dist_from_start + child_dist_from_end
            if child == end:
                path.append(child)
                path.append(parent)
                parent = parent_of_current_node
                while parent != None:
                    path.append(parent)
                    parent_closed_list_index = next((index for (index, d) in enumerate(closed_list) if d["the_node"] == parent), None)
                    if parent_closed_list_index == None:
                        parent = None
                    else:
                        parent = closed_list[parent_closed_list_index]["parent"]
                return path[::-1]

            child_closed_list_node_index = next((index for (index, d) in enumerate(closed_list) if d["the_node"] == child), None)
            if child_closed_list_node_index != None:
                continue
            child_open_list_node_index = next((index for (index, d) in enumerate(open_list) if d["the_node"] == child), None)
            if child_open_list_node_index == None:
                open_list.append({"the_node": child, "parent": parent, "g_value": child_dist_from_start, "f_value": child_f})
            elif child_f >= open_list[child_open_list_node_index]["f_value"]:
                continue
            child_open_list_node_index = next((index for (index, d) in enumerate(open_list) if d["the_node"] == child), None)
            open_list[child_open_list_node_index] = {"the_node": child, "parent": parent, "g_value": child_dist_from_start, "f_value": child_f}

a_lst = []

for i in range(len(lst)):
    for j in range(len(lst[i])):
        if lst[i][j] == "a":
            start = (i, j)
            path = a_star()
            if path != None:
                a_lst.append(len(path) - 1)

print(a_lst)
print(min(a_lst))