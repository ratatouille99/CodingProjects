score = 0
def checkGuess(guess,answer):
	attemps = 0
	global score

	while(attemps != 3):
		if answer.lower() == guess.lower():
			score += 1
			print('Correct answer!!')
			break

		else:
			attemps += 1
			answer = input('Wrong answer. Try again: ')

	else:
		print(f'\nThe correct answer is {guess} \nYour score is: {score}')


answer = input('Which is the largest animal?:\n\
A)Blue whale \nB)Elephant \nC)Mice \nD)Jaguar\
Type A, B, C or D: ')
checkGuess('A', answer)
