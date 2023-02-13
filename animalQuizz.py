number = int(input('Introduce the number of questions: '))
answers = []
questions = []
diccionario = {}

for i in range(number):
	questions.append(input(f'\n{i+1})Introduce your question: '))
	answers.append(input('   Introduce your answer: '))

for i in range(number):
	diccionario[answers[i]] = questions[i]

#Start the game
score = 0
chance = 3
answer = ''

print(f'Guess the anima! ')

for key, value in diccionario.items():

	print(f'Score: {score} \nChances: {chance}')
	print(f'\n{value.upper()}')
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


if(score == number):
	print('Congratulation!! you complete the game. Your awesome')



