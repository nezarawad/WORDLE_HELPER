path_words = "/Users/nezarawad/Code_Git/WORDLE_HELPER/words.txt"
path_letters = "/Users/nezarawad/Code_Git/WORDLE_HELPER/letters.txt"

def get_data(p):
    with open(p,'r') as path:
        l = [line.strip() for line in path]
    return l

def count_lets(w_list):
    
    output_list = []

    for i in range(5):
        pos_string = ""
        for w in w_list:
            pos_string += w[i]
        count_list = []
        for l in letters:
            c = pos_string.count(l)
            count_list.append(c)
        output_list.append(count_list)
    
    return output_list

def score_words(w_list):
    l_count = count_lets(w_list)
    all_words = "".join(w_list)
    w_totals = []
    for w in w_list:
        points = 0
        for i in range(5):
            word_no_dupes = ''.join(set(w))
            index = letters.index(w[i])
            points += l_count[i][index]
        for i in range(len(word_no_dupes)):
            points += all_words.count(word_no_dupes[i])
        w_totals.append(points)
    return w_totals

def t5_words(w_list):
    w_scores = score_words(w_list)

    sorted_paired = sorted(zip(w_scores, w_list), key=lambda x: x[0], reverse=True)

    sorted_numbers, sorted_words = zip(*sorted_paired)

    sorted_numbers = list(sorted_numbers)
    sorted_words = list(sorted_words)
    
    x = 5
    
    if len(w_list) < 5:
        x = len(w_list)

    for i in range(x):
        print("\n",i+1,") Sorted Numbers:", sorted_numbers[i], sorted_words[i])

def get_valid_word(words):
    guess = input().lower()
    while guess not in words or len(guess) != 5:
        guess = input("Invalid word: ")
    return guess

def valid_color(color):
    return color < 4 and color > 0

def gray_check(letter,words):
    new_words = []
    for w in words:
        if letter not in w:
            new_words.append(w)
    return new_words

def green_check(letter,words,index):
    new_words = []
    for w in words:
        if w[index] == letter:
            new_words.append(w)
    return new_words

def yellow_check(letter,words,index):
    new_words = []
    for w in words:
        if w[index] != letter and letter in w:
            new_words.append(w)
    return new_words

def main(words):
    words_left = words
    t5_words(words_left)

    for i in range(6):
        print(f"Guess #{i+1}:")
        guess = get_valid_word(words_left)

        print("1 - green | 2 - yellow | 3 - gray")

        for i in range(5):
            l_color = int(input(f"What color was the {guess[i]}: "))

            while not valid_color(l_color):
                l_color = int(input(f"Invalid color, try again for {guess[i]}: "))

            if l_color == 1:
                words_left = green_check(guess[i],words_left,i)
            elif l_color == 3:
                words_left = gray_check(guess[i],words_left)
            elif l_color == 2:
                words_left = yellow_check(guess[i],words_left,i)

        t5_words(words_left)

raw_words = get_data(path_words)
letters = get_data(path_letters)

print("Welcome to WORDLE HELPER!!")
main(raw_words)