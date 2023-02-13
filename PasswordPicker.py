import random #We need this module to get a random number in our code
import string

band = True
adjectives = ['red', 'big', 'little','dead','faint', 'deep', 'crazy','huge','fat']
nouns = ['cat', 'dog', 'whale','bee','book','man','women','child','space']
#ASCCI code characters: 33-47

def passwordPicker(adjectives, nouns):
	password = ''
	adject = random.choice(adjectives)
	noun = random.choice(nouns)
	number = random.randrange(0, 100)
	#We use the ASCII values for create a random character
	character = chr(random.randrange(33,47))#string.punctuation() this is another way to create a character 

	password = adject + noun + str(number) + character

	return password

print('Welcome to password picker')
result = passwordPicker(adjectives,nouns)
print(result)
while(band):
	res = input('Do you want to create another password? (y/n): ')
	if res.lower() == 'y':
		result = passwordPicker(adjectives,nouns)
		print(result)
	
	elif res.lower() == 'n':
		break

	else:
		print('This option cannot be considered\n')