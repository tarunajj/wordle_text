# Name: Tarun Ajjarapu
# UTEID: ta24625
#
# On my honor, Tarun Ajjarapu, this programming assignment is my own work
# and I have not provided this code to any other student.

import random


def main():
    """ Plays a text based version of Wordle.
        1. Read in the words that can be choices for the secret word
        and all the valid words. The secret words are a subset of
        the valid words.
        2. Explain the rules to the player.
        3. Get the random seed from the player if they want one.
        4. Play rounds until the player wants to quit.
    """
    secret_words, all_words = get_words()
    welcome_and_instructions()
    game(secret_words, all_words)


def game(secret_words, all_words):
    """ Plays a game of wordle
        1. Gives a player six incorrect valid word guesses
        until they guess the secret word
        2. Shows player how close a guess is to the actual word.
        3. Keeps track of letters guessed during the game.
    """
    curr = random.choice(secret_words)
    guess = ''
    history = list()
    print()
    letters_guessed = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                       'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
                       'W', 'X', 'Y', 'Z']
    rounds = 0
    while guess != curr and rounds < 6:
        guess = input('Enter your guess. A 5 letter word: ').upper()
        print()
        if guess in all_words:
            temp = list(curr)
            word = list('-----')
            for index, chr in enumerate(guess):
                if chr in letters_guessed:
                    letters_guessed.remove(chr)
                if curr[i] == chr:
                    word[i] = 'G'
                    temp.remove(c)
            for index, chr in enumerate(guess):
                if word[index] == '-' and chr in curr and chr in temp:
                    word[index] = 'O'
                    temp.remove(chr)
            history.append(''.join(word))
            history.append(guess)
            print(*history, sep='\n')
            print()
            print('Unused letters:', *letters_guessed, sep=' ')
            print()
            rounds += 1
        else:
            print(guess, 'is not a valid word. Please try again.\n')
    result(curr, guess, rounds, secret_words, all_words)


def result(curr, guess, rounds, secret_words, all_words):
    """ Deals with the result of a game
        1. Tells player if they won or lost
        2. Allows the player the chance to play again
    """
    results = (
        'Genius', 'Magnificent', 'Impressive', 'Splendid', 'Great', 'Phew')
    if guess == curr:
        print(f'You win. {results[rounds - 1]}!\n')
    else:
        print(f'Not quite. The secret word was {curr}.\n')
    play = input('Do you want to play again? Type Y for yes: ')
    if play == 'y' or play == 'Y':
        game(secret_words, all_words)


def welcome_and_instructions():
    """
    Print the instructions and set the initial seed for the random
    number generator based on user input.
    """
    print('Welcome to Wordle.')
    instructions = input('\nEnter y for instructions, anything else to skip: ')
    if instructions == 'y':
        print('\nYou have 6 chances to guess the secret 5 letter word.')
        print('Enter a valid 5 letter word.')
        print('Feedback is given for each letter.')
        print('G indicates the letter is in the word and in the correct spot.')
        print('O indicates the letter is in the word but not that spot.')
        print('- indicates the letter is not in the word.')
    set_seed = input(
        '\nEnter y to set the random seed, anything else to skip: ')
    if set_seed == 'y':
        random.seed(int(input('\nEnter number for initial seed: ')))


def get_words():
    """ Read the words from the dictionary files.
        We assume the two required files are in the current working directory.
        The file with the words that may be picked as the secret words is
        assumed to be names secret_words.txt. The file with the rest of the
        words that are valid user input but will not be picked as the secret
        word are assumed to be in a file named other_valid_words.txt.
        Returns a sorted tuple with the words that can be
        chosen as the secret word and a set with ALL the words,
        including both the ones that can be chosen as the secret word
        combined with other words that are valid user guesses.
    """
    temp_secret_words = []
    with open('secret_words.txt', 'r') as data_file:
        all_lines = data_file.readlines()
        for line in all_lines:
            temp_secret_words.append(line.strip().upper())
    temp_secret_words.sort()
    secret_words = tuple(temp_secret_words)
    all_words = set(secret_words)
    with open('other_valid_words.txt', 'r') as data_file:
        all_lines = data_file.readlines()
        for line in all_lines:
            all_words.add(line.strip().upper())
    return secret_words, all_words


if __name__ == '__main__':
    main()
