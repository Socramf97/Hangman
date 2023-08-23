import random

word_list = ["rule", 'didactic', 'gate', 'selective', 'coach', 'fat', 'enchanting', 'tiger', 'hand', 'damp', 'lame', 'table', 'education', 'teeny',
             'impolite', 'gather', 'unit', 'talk', 'disgusted', 'bat', 'teaching', 'circle', 'aback', 'scribble', 'attempt', 'afford', 'veil',
             'snakes', 'berry', 'fuzzy', 'guess', 'needy', 'poised', 'nut', 'open', 'flight', 'remind', 'bore']

alphabet = "abcdefghijklmnopqrstuvwxyz"

game_status = 'stop'
chosen_word = ''
guessed = ''
lives = 6
correct_guesses = 0
letter_tracker = []


def start_game():
    game_status = 'start'

def select_word():
    if game_status == "stop":
        rand_word = random.choice(word_list)  # choses random array number in word_list and returns the word of the word_list
        chosen_word = rand_word    
    return chosen_word

def user_guess():
    guess=input("Guess a letter: ")
    if guess not in alphabet:
        input("You didn't enter a letter. Please try again: ")
    guessed = guess
    return guessed

def check_guess():
    if guessed not in chosen_word:
        lives -= 1
        draw_part()
        if lives == 0: 
            end_game()
    else:
        print("You guessed the letter correctly!")
        correct_guesses += 1
        # need to figure out how to display blank spaces. THinking of 2 dictionaries. One to keep track of the entire word and one to keep track of the empty spaces.
        if lives != 0:
            user_guess
        else:
            if correct_guesses == len(chosen_word):
                end_game() 
            
def draw_board():
    for i in range(len(chosen_word)):
        letter_tracker.append("_")
    return letter_tracker 

def draw_word():
    return

def draw_part():
    return
def end_game():
    return
def generate_blank_spaces():
    return
def replace_with_letter(): 
    return



print(select_word())
print(letter_tracker)