import random

NB_TURNS = 10

def pick_random_word():

    with open(f"words.txt","r") as file:
        data = file.read()
        words_list = data.split()
        random_num = random.randint(0,len(words_list)-1)
        picked_word = words_list[random_num]

    return picked_word


def reveal_letters(word, letters): 

    underline_word = []
    
    for i in range(len(word)):
        picked_word = word.replace(word[i],"_")
        underline_word.append(picked_word[i])
 
    for letter in letters:
        if letter in word:
            index = word.find(letter)
            while index != -1:
                underline_word[index] = letter
                index = word.find(letter, index + 1)

    return ' '.join(underline_word).upper()

def all_letters_found(word, letters):
    """Returns True if all letters in word are in the list 'letters'"""
    for letter in word:
        if not letter in letters:
            return False
        
    return True
    
def guess_input():
    guess_letter = input("Letter? ")
    if guess_letter.isalpha() and len(guess_letter) == 1:
        return guess_letter
    else:
        print("Invalid input.")

def guess_check(guess, guessed, word):
    if guess in word and guess not in guessed:
        message = "Matched."
    elif guess not in guessed:
        message = "Nothing matched."
    else:
        message = "You already guessed that letter."

    print(message)
    guessed.append(guess)   
    print(reveal_letters(word, guessed))

    return message

def all_letters_found(word, letters):
    for letter in word:
        if letter not in letters:
            return False
        
    return True
    

def main(turns):

    word = pick_random_word()
    print(word)
    guessed = []

    while turns > 0:
        guess_letter = guess_input()
        
        guess_check(guess_letter, guessed, word)
            
        if all_letters_found(word, guessed):
            print("Congrats! You got it!")
            return "won"

        turns -= 1

    print("You lost! No tries left!")
    return "lost"

if __name__ == "__main__":
    main(NB_TURNS)