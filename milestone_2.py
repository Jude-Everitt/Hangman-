'''
import random module which is one of pythons built-in modules
'''

import random

'''
define a list of my 5 favorite fruits and assign it to the variable: word_list
'''

word_list = ["Mango", "Lime", "Pineapple", "Coconut", "Banana"]

'''
create a random.choice method and pass through word_list variable into the choice
method. assigng the randomly generated word to a variable called word. and print word
'''

word = random.choice(word_list)

print(word)

'''
using the imput function, ask the user to enter a single letter and assign the input to a
variable called guess. Create an if statement to see if the input character is a letter
within the alphebet and also if the input is only one charcter in length
'''

guess = input("Enter a letter.\n")

if ((guess.isalpha() == True) and (len(guess) == 1)):
   print("Good guess!")
else:
   print("Oops! That is not a valid input.")

