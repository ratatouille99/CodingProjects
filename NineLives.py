import string
from random import choice

words = ['pizza', 'watermelon', 'coin', 'money', 'mother', 'nigger']
heart_symbol = u'\u2764 '

def palabra(array, lives):

	band = False
	win = False
	contador = 0
	initial_array = ['?']

	for i in range(len(array)-1):
		initial_array.append('?')

	print(initial_array)
	print('Lives left: ', heart_symbol * lives)
	print('\n')

	while(lives != 0 and win == False):
		ans = (input('Guess a letter or the whole word: '))

		if ans == array or contador == len(array):
			print('You won the secret word is', array)
			win = True
			break

		for i in range(len(array)):
			if ans.lower() == array[i]:
				initial_array[i] = ans.lower()
				contador = contador + 1
				band = True

		if band:
			print(initial_array)
			print('Lives left: ', heart_symbol * lives)
		
		else:
			lives = lives - 1
			print('Incorrect. You lose a life')
			print(initial_array)
			print('Lives left: ', heart_symbol * lives)

		band = False
		print('\n')

	if(lives == 0):
	 print('You lost')
		

array = choice(words)
vidas = 9;

palabra(array,vidas)