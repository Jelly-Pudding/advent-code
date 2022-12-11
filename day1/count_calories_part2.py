with open("input1.txt", "r") as f:
    biggest_count = [0, 0, 0]
    current_count = 0
    for line in f:
        if line.strip() == "":
            # find smallest item in biggest_count list
            min_value = min(biggest_count)
            min_index = biggest_count.index(min_value)
            if current_count >= biggest_count[min_index]:
                biggest_count[min_index] = current_count
            current_count = 0
        else:
            current_count += int(line.strip())
    print(sum(biggest_count))