import re
pattern = re.compile("(\d*)-(\d*),(\d*)-(\d*)")

with open("input.txt", "r") as f:
    overlaps = 0
    for line in f:
        numbers = re.search(pattern, line.strip())
        first_number = int(numbers.group(1))
        second_number = int(numbers.group(2))
        third_number = int(numbers.group(3))
        fourth_number = int(numbers.group(4))

        if first_number <= third_number and second_number >= fourth_number:
            overlaps += 1
        elif third_number <= first_number and fourth_number >= second_number:
            overlaps += 1
    print(overlaps)