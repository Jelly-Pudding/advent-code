import re

pattern_monkey = re.compile(r"Monkey (\d*):")
pattern_items = re.compile(r"Starting items: (.*)")
pattern_operations = re.compile(r"Operation: new = old (\*|\+) (old*|\d*)")
pattern_divisible_by = re.compile(r"Test: divisible by (\d*)")
pattern_true = re.compile(r"If true: throw to monkey (\d*)")
pattern_false = re.compile(r"If false: throw to monkey (\d*)")
dic = {}

# Simply get input
with open("input.txt", "r") as f:
    for line in f:
        match_monkey = re.match(pattern_monkey, line.strip())
        if match_monkey:
            dic[int(match_monkey.group(1))] = []
        
        match_items = re.match(pattern_items, line.strip())
        if match_items:
            str_items = match_items.group(1).replace(" ", "")
            lst_items = list(map(int, str_items.split(",")))
            dic[max(dic)] = [[], [], [], [], [], [0]]
            dic[max(dic)][0] = lst_items

        match_operations = re.match(pattern_operations, line.strip())
        if match_operations:
            lst = [match_operations.group(1), match_operations.group(2)]
            dic[max(dic)][1] = lst

        match_divisible_by = re.match(pattern_divisible_by, line.strip())
        if match_divisible_by:
            dic[max(dic)][2] = [match_divisible_by.group(1)]

        match_true = re.match(pattern_true, line.strip())
        if match_true:
            dic[max(dic)][3] = [match_true.group(1)]

        match_false = re.match(pattern_false, line.strip())
        if match_false:
            dic[max(dic)][4] = [match_false.group(1)]

# Now comes the calculation
modulo = 1
for value in dic.values():
    modulo *= int(value[2][0])

for i in range(10000):
    for key in dic.keys():
        minus_when_popped = 0
        for idx in range(len(dic[key][0])):
            worry_level = dic[key][0][idx - minus_when_popped]
            if dic[key][1][0] == "*":
                if dic[key][1][1] == "old":
                    worry_level = (worry_level * worry_level) % modulo
                else:
                    worry_level = (worry_level * int(dic[key][1][1])) % modulo
            elif dic[key][1][0] == "+":
                if dic[key][1][1] == "old":
                    worry_level = (worry_level + worry_level) % modulo
                else:
                    worry_level = (worry_level + int(dic[key][1][1])) % modulo

            if worry_level % int(dic[key][2][0]) == 0:
                dic[int(dic[key][3][0])][0].append(worry_level)
                dic[key][0].pop(idx - minus_when_popped)
                minus_when_popped += 1
            else:
                dic[int(dic[key][4][0])][0].append(worry_level)
                dic[key][0].pop(idx - minus_when_popped)
                minus_when_popped += 1

            dic[key][5][0] += 1

lst = []
for key, value in dic.items():
    lst.append(value[5][0])

answer = sorted(lst)[-1] * sorted(lst)[-2]
print(answer)
#print(dic)