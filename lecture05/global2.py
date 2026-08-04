# This program simulates 10 tosses of a coin
import random

# Constants
HEADS = "1"
TAILS = "2"
TOSSES = 10

def toss_coin():
    for toss in range(TOSSES):
        # Simulate a coin toss
        if random.randint(HEADS, TAILS) == 0:
            print('Heads')
        else:
            print('Tails')

# Call the main function.
toss_coin()