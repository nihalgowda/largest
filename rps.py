
import random

di={'r':"rock",'p':"paper",'s':"scissor"}

l=['r','p','s']
uscore = 0 
cscore = 0

while True:

	u = input("enter your choice ")
	print("you chose",di[u])
	c = random.choice(l)
	print("Computer chooses",di[c])

	if u == c:
		print("It's a tie")
	if c == 'r' and u == 'p':
		print("You win")
		uscore=uscore+1
	if c == 'r' and u == 's':
		print("C wins")
		cscore=cscore+1
	if c  == 'p' and u == 'r':
		print("you win")
		uscore=uscore+1
	if c == 'p' and u == 's':
		print("you win")
		uscore=uscore+1
	if c == 's' and u == 'r':
		print("C wins")
		cscore=cscore+1
	if c == 's' and u == 'p':
		print("C wins")
		cscore=cscore+1

	print("score")
	print("computer",cscore,"user",uscore)

	if cscore==3:
		print("computer is a champion")
		exit()
	elif uscore==3:
		print("you is champion")
		exit()

	
