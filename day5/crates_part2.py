import re
pattern = re.compile(r"(\s{3}|\[?[A-Z]?\]?) (\s{3}|\[?[A-Z]?\]?) (\s{3}|\[?[A-Z]?\]?) (\s{3}|\[?[A-Z]?\]?) (\s{3}|\[?[A-Z]?\]?) (\s{3}|\[?[A-Z]?\]?) (\s{3}|\[?[A-Z]?\]?) (\s{3}|\[?[A-Z]?\]?) (\s{3}|\[?[A-Z]?\]?)")
pattern_2 = re.compile(r"move (\d*) from (\d*) to (\d*)")
lst = [[],[],[],[],[],[],[],[],[]]

with open("input.txt", "r") as f:
    for line in f:
        match = re.match(pattern, line)
        if match:
            for i in range(9):
                lst[i].append(match.group(i + 1)[1])
        match_2 = re.match(pattern_2, line.strip())
        if match_2:
            first_number = int(match_2.group(1))
            second_number = int(match_2.group(2)) - 1
            third_number = int(match_2.group(3)) - 1
            for i in range(first_number):
                letter_idxs = []
                for idx in range(len(lst[second_number])):
                    if lst[second_number][idx] != " ":
                        letter_idxs.append(idx)
                        if len(letter_idxs) == first_number:
                            break
            for i in range(len(letter_idxs) - 1, -1, -1):
                letter = lst[second_number][letter_idxs[i]]
                found_space = False
                space_idx = 0
                for idx in range(len(lst[third_number]) -1, -1, -1):
                    if lst[third_number][idx] == " ":
                        found_space = True
                        space_idx = idx
                        break
                if found_space:
                    lst[third_number][space_idx] = letter
                else:
                    lst[third_number].insert(0, letter)
                lst[second_number][letter_idxs[i]] = " "

stringer = ""
for lstt in lst:
    for i in range(len(lstt)):
        if lstt[i] != " ":
            stringer += lstt[i]
            break

print(stringer)
