import os
import random
import time
os.system("cls")
#col=random.randint(1,9)
os.system("color 2")
ch='y'
dict=[]
while ch=='y' or ch=='Y':
	print("\n\t\t\t\tStart Game")
	time.sleep(3)
	os.system("cls")
	print("\n\t\tMore Range have Chance to score very high")
	range=int(input("\n\tEnter Last Ranging Number To Guess(minimum 10):"))
	number=random.randint(1,range)
	print(f"\n\tYou Guess Number Between 1 and {range}")
	var=1
	d=0
	chance=range//10
	print(f"\n\t\tYou Have {chance} Chance To guess")
	time.sleep(3)
	os.system("cls")
	while var<=chance:
		c=chance-var+1
		guessnumber=int(input("\n\t\tGuess Number:"))
		if guessnumber>range or guessnumber<1:
			print("\n\t\tYou choose wrong number which is out of range")
			continue
		
		else:
			if guessnumber==number:
				print("\n\t\tWow,You Win The Game")
				score=c*20
				d=1
				os.system("color 2")
				break
			elif guessnumber<=number:
				if var==chance-1:
					os.system("cls")
					print("\n\t\tIt's last Chance")
					dict.append(guessnumber)
					print("\n\t\tYou Write This Number Pastly:",dict)
					os.system("color 4")
				
				if var<=chance-1:	
					os.system("cls")
					print("\n\t\tHint:You Choose lower number so choose greater")
					dict.append(guessnumber)
					print("\n\t\tYou Write This Number Pastly:",dict)
			
			elif guessnumber>=number:
				
				if var==chance-1:
					os.system("cls")
					print("\n\t\tIt's Last Chance")
					dict.append(guessnumber)
					print("\n\t\tYou Write This Number Pastly:",dict)
					os.system("color 4")
				
				if var<=chance-1:
					os.system("cls")
					print("\n\t\tHint:You Choose Greater number so choose lower")
					dict.append(guessnumber)
					print("\n\t\tYou Write This Number Pastly:",dict)
		
		var=var+1
	if d==0:
		score=0
		print("\n\t\tYou Lost")
		print(f"\n\t\tcorrect number is {number}")
	print(f"\n\t\tYour Score is {score}/{20*chance}")
	ch=input("\n\t\tDo You Want TO Continue(y/n):")