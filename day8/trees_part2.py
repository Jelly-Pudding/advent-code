with open("input.txt", "r") as f:
    lst = []
    counter = -1
    for line in f:
        lst.append([])
        counter += 1
        for number in line.strip():
            lst[counter].append(int(number))


biggest_scenic_score = 0

for i in range(len(lst)):
    for j in range(len(lst[0])):
        if i == 0 or i == len(lst) - 1:
            continue
        elif j == 0 or j == len(lst[0]) - 1:
            continue

        directions = [0, 0, 0, 0]
        current_value = lst[i][j]
        counter = 1
        # up
        while i - counter >= 0:
            if current_value <= lst[i - counter][j]:
                directions[0] += 1
                break
            else:
                directions[0] += 1
            counter += 1

        counter = 1
        while i + counter <= len(lst) - 1:
            if current_value <= lst[i + counter][j]:
                directions[1] += 1
                break
            else: 
                directions[1] += 1
            counter += 1

        counter = 1
        # left
        while j - counter >= 0:
            if current_value <= lst[i][j - counter]:
                directions[2] += 1
                break
            else:
                directions[2] += 1
            counter += 1

        counter = 1
        # right
        while j + counter <= len(lst[0]) - 1:
            if current_value <= lst[i][j + counter]:
                directions[3] += 1
                break
            else:
                directions[3] += 1
            counter += 1
        scenic_score = directions[0] * directions[1] * directions[2] * directions[3]
        if scenic_score >= biggest_scenic_score:
            biggest_scenic_score = scenic_score

print(biggest_scenic_score)