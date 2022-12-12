with open("input.txt", "r") as f:
    letters = []
    line = f.readline().strip()
    counter = -1
    for i in range(14):
        letters.append(line[i])
    for i in range(len(line)):
        counter += 1
        letters[counter % 14] = line[i]
        if len(letters) == len(set(letters)):
            print(i + 1)
            break
    print(letters)