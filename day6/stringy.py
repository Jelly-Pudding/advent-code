with open("input.txt", "r") as f:
    letters = ["Z", "Z", "Z", "Z"]
    line = f.readline().strip()
    counter = -1
    letters = [line[0], line[1], line[2], line[3]]
    for i in range(len(line)):
        counter += 1
        letters[counter % 4] = line[i]
        if len(letters) == len(set(letters)):
            print(i + 1)
            break