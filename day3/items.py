with open("input.txt", "r") as f:
    score = 0
    for line in f:
        item_num = int(len(line.strip()) / 2) 
        first_half = line[:item_num]
        second_half = line[item_num:]
        repeated_letter = ""
        letters_dict = {}
        for letter in first_half:
            if letter not in letters_dict:
                letters_dict[letter] = 1
        for letter in second_half:
            if letter in letters_dict:
                repeated_letter = letter
                break
        if letter.islower():
            score += ord(letter) - 96
        else:
            score += ord(letter) - 38
    print(score)