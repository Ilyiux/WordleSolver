# BUGS:
# None :)

def main():
    words = filter_words()
    knows = [False, False, False, False, False]
    values = ["", "", "", "", ""]
    not_values = [[], [], [], [], []]
    min_letters = {}
    max_letters = {}
    previous_guesses = 0
    while True:
        guess = ""
        if previous_guesses == 0:
            guess = "TARES"
        else:
            valid_words = get_valid_words(words, knows, values, not_values, min_letters, max_letters)
            guess = get_best_word(valid_words)
        print(f"Guess {previous_guesses + 1}: {guess}")
        result = input("Formatted Result String, uppercase letter and then # 0-2, 0 is gray, 1 is yellow, 2 is green (Ex: T0A1R2E2S0): ")
        letters = list(result[0::2])
        data = list(result[1::2])
        for i in range(len(data)):
            if data[i] == "0":
                c = 0
                for l in range(len(letters)):
                    if letters[l] == letters[i]:
                        if data[l] == "1" or data[l] == "2":
                            c += 1
                max_letters[letters[i]] = c
            if data[i] == "1":
                not_values[i].append(letters[i])
                c = 0
                for l in range(len(letters)):
                    if letters[l] == letters[i]:
                        if data[l] == "1" or data[l] == "2":
                            c += 1
                min_letters[letters[i]] = c
            if data[i] == "2":
                knows[i] = True
                values[i] = letters[i]
        #print(f"{min_letters} {max_letters}")
        previous_guesses += 1

def filter_words():
    # read words.txt
    words = [""]
    with open('words.txt') as f:
        words = f.readlines()[0].split(" ")
    return words

def get_valid_words(words, knows, values, not_values, min_letters, max_letters): # NEEDS REWORK
    valid_words = []
    for word in words:
        is_valid = True
        #implement min_letters and max_letters
        for k in min_letters.keys():
            if list(word).count(k) < min_letters[k]:
                is_valid = False
        for k in max_letters.keys():
            if list(word).count(k) > max_letters[k]:
                is_valid = False
        for i in range(len(word)):
            if knows[i]:
                if list(word)[i] is not values[i]:
                    is_valid = False
            else:
                if list(word)[i] in not_values[i]:
                    is_valid = False
        if is_valid:
            valid_words.append(word)
    return valid_words

def score_word(query):
    score = 0
    for word in filter_words():
        q_split = list(query)
        w_split = list(word)
        i = 0
        while True:
            if i < len(w_split):
                if q_split[i] == w_split[i]:
                    score += 2
                    del q_split[i]
                    del w_split[i]
                i += 1
            else:
                break
        for l in w_split:
            if l in q_split:
                score += 1
    return score

def get_best_word(words):
    scores = []
    for word in words:
        print(f"{word}: {words.index(word) + 1}/{len(words)}")
        scores.append(score_word(word))
    return words[scores.index(max(scores))]

def test():
    print(get_best_word(filter_words()))
    
if __name__ == "__main__":
    main()