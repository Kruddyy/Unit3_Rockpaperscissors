import time
import random

print('I am rock, paper, scissors Bot!')
time.sleep(0.6)
user = input('What do you choose? ')
time.sleep(0.6)
print('Rock!')
time.sleep(0.6)
print('Paper!')
time.sleep(0.6)
print('Scissors!')
time.sleep(0.6)
print('Say Shoot!')


comp = random.randint(1,4)

if comp == 1:
	comp = 'Rock'
	time.sleep(0.6)
	print('Rock')
elif comp == 2:
	comp = 'Paper'
	time.sleep(0.6)
	print('Paper')

else comp == 3:
	comp = 'Scissors'
	time.sleep(0.7)
	print('Scissors')


if user == 'Rock' or 'rock' and comp == 'Rock':
	print('Go again')
elif user == 'Scissors'  or 'scissors' and comp == 'tie':
	print('You tied.')
elif user == 'Rock' or 'rock' and comp == 'tie':
	print('You tied.')
elif user == 'Paper' or 'paper' and comp == 'tie':
	print('You tied.')
elif user == 'Rock' or 'rock' and comp == 'Paper':
	print('You Lost sorry.')
elif user == 'Rock' or 'rock' and comp == 'Scissors':
	print('You Won!')
elif user == 'Paper' or 'paper' and comp == 'Paper':
	print('Go again.')
elif user == 'Paper' or 'paper' and comp == 'Rock':
	print('You Won!')
elif user == 'Paper' or 'paper' and comp == 'Scissors':
	print('You Lost sorry.')
elif user == 'Scissors' or 'scissors' and comp == 'Paper':
	print('You Won!')
elif user == 'Scissors' or 'scissors' and comp == 'Rock':
	print('You Lost sorry.')

else:
	print('Go again')