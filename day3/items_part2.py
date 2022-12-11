with open("input.txt", "r") as f:
    score = 0
    idx = 0
    letters_dictionary = {}
    repeated_letter = ""
    for line in f:
        already_counted = {}
        print(line.strip())
        idx += 1
        for letter in line.strip():
            if letter not in letters_dictionary:
                letters_dictionary[letter] = 1
                already_counted[letter] = True
            else:
                if letter not in already_counted:
                    letters_dictionary[letter] += 1
                    already_counted[letter] = True
                    if letters_dictionary[letter] == 3:
                        repeated_letter = letter
        if idx % 3 == 0:
            if repeated_letter.islower():
                score += ord(repeated_letter) - 96
            else:
                score += ord(repeated_letter) - 38
            print(repeated_letter)
            letters_dictionary = {}
            repeated_letter = ""
    
    print(score)