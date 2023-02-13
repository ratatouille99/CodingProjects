guess = 'Which bear lives at the North Pole?'
guess1 = 'Which is the largest animal?'
guess2 = 'Which is the fastest land animal?'
guess3 = 'Which is the most lazy land animal?'

diccionario = {
	'polar bear' : guess,
	'blue whale' : guess1,
	'cheetah' : guess2,
	'cat' : guess3
}


score = 0
chance = 3
answer = ''

print(f'Guess the anima! ')

for key, value in diccionario.items():

	print(f'Score: {score} \nChances: {chance}')
	print(f'\n{value}')
	answer = input('What is your answer?: ')

	while (answer.lower() != key and chance != 0):
		chance -= 1

		if chance != 0:
			print('Wrong answer. Try again\n')
			print(f'Score: {score} \nChances: {chance}')
			print(f'\n{value}')
			answer = input('What is your answer?: ')
			
		else:
			break	
		

	if(chance == 0):	
		print(f'The correct answer is {key} \nYour score is: {score}')
		break;

	else:
		print('Correct answer\n')
		score += 1


if(score == 4):
	print('Congratulation!! you complete the game. Your awesome')



