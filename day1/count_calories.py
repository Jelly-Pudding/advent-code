with open("input1.txt", "r") as f:
    biggest_count = 0
    current_count = 0
    for line in f:
        if line.strip() == "":
            if current_count >= biggest_count:
                biggest_count = current_count
            current_count = 0
        else:
            current_count += int(line.strip())
    print(biggest_count)