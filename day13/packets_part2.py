import ast

all_packets = []

with open("input.txt", "r") as f:
    for line in f:
        if line.strip() == "":
            continue
        all_packets.append(ast.literal_eval(line.strip()))

all_packets.append([[6]])
all_packets.append([[2]])

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

def order_items(items):
    # Set the reference item to the first item in the list
    reference = items[0]

    # Sort the items using a custom key function
    sorted_items = sorted(items[1:], key=lambda x: compare(reference, x))

    # Insert the reference item at the beginning of the sorted list
    sorted_items.insert(0, reference)

    # Check that each item and all items at higher indices return True when passed to compare_items
    for i in range(len(sorted_items) - 1):
        for j in range(i + 1, len(sorted_items)):
            if not compare(sorted_items[i], sorted_items[j]):
                # If an item and a higher-indexed item do not return True, swap them
                sorted_items[i], sorted_items[j] = sorted_items[j], sorted_items[i]

                # Start the inner loop over again from the current index
                j = i

    return sorted_items

ordered_packets = order_items(all_packets)

multiply = []
for i in range(len(ordered_packets)):
    if ordered_packets[i] == [[6]] or ordered_packets[i] == [[2]]:
        multiply.append(i + 1)

print(multiply[0] * multiply[1])