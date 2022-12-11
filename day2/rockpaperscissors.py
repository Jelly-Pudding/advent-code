with open("input.txt", "r") as f:
    score = 0
    for line in f:
        if line[0] == "A":
            if line[2] == "X":
                score += 4
            elif line[2] == "Y":
                score += 8
            elif line[2] == "Z":
                score += 3
        elif line[0] == "B":
            if line[2] == "X":
                score += 1
            elif line[2] == "Y":
                score += 5
            elif line[2] == "Z":
                score += 9
        elif line[0] == "C":
            if line[2] == "X":
                score += 7
            elif line[2] == "Y":
                score += 2
            elif line[2] == "Z":
                score += 6
    print(score)
    
