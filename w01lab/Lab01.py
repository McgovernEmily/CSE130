# 1. Name:
#    Emily McGovern
# 2. Assignment Name: 
#    Lab 01: Python Review
# 3. Assignment Description:
#    This program is meant to be a number guessing game. The player will pick a maximum 
#    number that will determine the difficulty of the game. The player will continually guess a number
#    until they guess right. At the end, the program will give out how many guesses were used and what
#    numbers they used to guess.
# 4. What was the hardest part? Be as specific as possible.
#    At first this assignment was a bit of a struggle. I have not used Python in about 8 months. 
#    Before I started this assignment I went back and looked at all of my notes and projects I worked on
#    in class 110. After a good review I was able to handle with assignment with ease. I will say that 
#    trying to figure out how to make "too high" and "too low" message have a tab before 'too' was a bit of
#    a challenge. After looking back in my notes again and thinking hard, I remembered a friend telling me that
#    using "\t" was a way to add a tab. I thought the instructions were very clear and easy to follow. I also 
#    thought the template was a great help and guide. I struggle with making comments, so it was nice to see
#    how to properly use comments. I want to try my hardest at adding comments to my code. 
# 5. How long did it take for you to complete the assignment?
#    It took me about 25 mins reading and complete the assignment without adding the time I used to review
#    for this assignment. If I did add the time I used to review for Python, then including the review and 
#    the assignment time, it took about 1 hour and 35 mins   

import random

# Intro to Game.
print('\nThis is the "Guess a Number Challenge".')
print('You will try to guess a random number in the smallest number of attempts.')
print('Good luck!')

# Prompting the user for how difficult the game will be and the integer
print('\nPlease insert the rage of difficult you want the game to be.')
value_max = int(input('Pick a positive integer: '))

# Generating a random number between 1 and the users value.
value_random = random.randint(1, value_max)

# Giving the user instructions on what to do.
print(f'\nGuess a number between 1 and {value_max}')

# Initialize the sentinal and the array of guesses.
numb_guess = ''
numb_list = []
guess_total = 0

# Play the guessing game.
while numb_guess != value_random:

    # Prompt the user for a number.
    numb_guess = int(input('> '))

    # Store the number and guessing amount.
    numb_list.append(numb_guess)
    guess_total = guess_total + 1

    # Make a decision if it was the guess too high, too low, or just right.
    if numb_guess > value_random:
        print('\tToo high!')
    elif numb_guess < value_random:
        print('\tToo low!')
    elif numb_guess == value_random:
        print('\tCongratulations!!')

# Give the user a report of how they did.
print(f'\nThe correct number is {value_random}!')
print(f'It took you {guess_total} times to guess the correct number.')
print(f'Here is the list of numbers you guessed:{numb_list}')
