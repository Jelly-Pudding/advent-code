import ast

all_packets = {}
counter = 1

with open("input.txt", "r") as f:
    for line in f:
        if line.strip() == "":
            counter += 1
            continue
        if counter not in all_packets:
            all_packets[counter] = {"A": line.strip()}
        else:
            all_packets[counter]["B"] = line.strip()

def compare(left, right):
    # Convert integers to single-item lists
    if isinstance(left, int) and not isinstance(right, int):
        left = [left]
    elif isinstance(right, int) and not isinstance(left, int):
        right = [right]
    
    # Compare integers
    if isinstance(left, int) and isinstance(right, int):
        return left < right
    
    # Compare lists
    if isinstance(left, list) and isinstance(right, list):
        # Compare elements one by one
        for l, r in zip(left, right):
            if compare(l, r):
                return True
            elif compare(r, l):
                return False
        
        # If lists are the same length and no comparison made a decision, return True if left list is shorter
        return len(left) < len(right)
    
    # If left and right are not integers or lists, we cannot compare them
    return False

indices_summed = 0
for i in range(1, counter + 1):
    packet1 = ast.literal_eval(all_packets[i]["A"])
    packet2 = ast.literal_eval(all_packets[i]["B"])
    if compare(packet1, packet2):
        indices_summed += i

print(indices_summed)
