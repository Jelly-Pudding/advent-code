with open("input.txt", "r") as f:
    lst = []
    counter = -1
    for line in f:
        lst.append([])
        counter += 1
        for number in line.strip():
            lst[counter].append(int(number))

visible = 0

for i in range(len(lst)):
    for j in range(len(lst[0])):
        if i == 0 or i == len(lst) - 1:
            visible += 1
            continue
        elif j == 0 or j == len(lst[0]) - 1:
            visible += 1
            continue
        current_value = lst[i][j]
        counter = 1
        is_visible = False
        # up
        while i - counter >= 0:
            if current_value <= lst[i - counter][j]:
                break
            if i - counter == 0:
                visible += 1
                is_visible = True
                break
            counter += 1

        if is_visible:
            continue
        counter = 1
        is_visible = False
        # down
        while i + counter <= len(lst) - 1:
            if current_value <= lst[i + counter][j]:
                break
            if i + counter == len(lst) - 1:
                visible += 1
                is_visible = True
                break
            counter += 1

        if is_visible:
            continue
        counter = 1
        is_visible = False
        # left
        while j - counter >= 0:
            if current_value <= lst[i][j - counter]:
                break
            if j - counter == 0:
                visible += 1
                is_visible = True
                break
            counter += 1

        if is_visible:
            continue
        counter = 1
        # right
        while j + counter <= len(lst[0]) - 1:
            if current_value <= lst[i][j + counter]:
                break
            if j + counter == len(lst[0]) - 1:
                visible += 1
                break
            counter += 1

print(visible)


