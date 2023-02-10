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
    curr = random.choice(secret_words)
    guess = ''
    history = '\n'
    print()
    lettersGuessed = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                      'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    rounds = 0
    while guess != curr and rounds != 6:
        guess = input('Enter your guess. A 5 letter word: ').upper()
        if guess in all_words:
            temp = curr
            word = ''
            for i, c in enumerate(guess):
                if c in lettersGuessed:
                    lettersGuessed.remove(c)
                if curr[i] == c:
                    word += 'G'
                elif c in temp:
                    temp = temp[1:]
                    word += 'O'
                else:
                    word += '-'
            history += word + '\n' + guess + '\n'
            print(history)
            print('Unused letters: ', *lettersGuessed, sep=' ')
            print()
            rounds += 1
        else:
            print()
            print(guess, 'is not a valid word. Please try again.\n')
    results = ('Genius', 'Magnificent', 'Impressive', 'Splendid', 'Great', 'Phew')
    if rounds < 6:
        print(f'You win. {results[rounds]}!\n')
    else:
        print(f'Not quite. The secret word was {curr}.\n')
    play = input('Do you want to play again? Type Y for yes: ')
    if (play == 'y' or play == 'Y'):
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