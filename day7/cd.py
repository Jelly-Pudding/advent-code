import re 

pattern_1 = re.compile(r"\$ cd ([a-z/]+)")
pattern_2 = re.compile(r"\$ cd \.\.")
pattern_3 = re.compile(r"([0-9]+).*")
pattern_4 = re.compile(r"dir ([a-z]+)")

with open("input.txt", "r") as f:
    current_directory = []
    all_directories = {}
    for line in f:
        match = re.match(pattern_1, line.strip())
        if match:
            directory = match.group(1).strip()
            current_directory.append(directory)
            if "/".join(current_directory) in all_directories:
                pass
            else:
                all_directories["/".join(current_directory)] = [0, []]

        match_2 = re.match(pattern_2, line.strip())
        if match_2:
            current_directory.pop()

        match_3 = re.match(pattern_3, line.strip())
        if match_3:
            number = int(match_3.group(1).strip())
            all_directories["/".join(current_directory)][0] += number

        match_4 = re.match(pattern_4, line.strip())
        if match_4:
            dir = "/".join(current_directory) + "/" + match_4.group(1).strip()
            all_directories["/".join(current_directory)][1].append(dir)

# python 3.7 - dictionaries are ordered
total_score = 0
for key, value in reversed(list(all_directories.items())):
    score = value[0]
    for directory in value[1]:
        score += all_directories[directory][0]
    all_directories[key][0] = score
    if score <= 100000:
        total_score += score

print(total_score)