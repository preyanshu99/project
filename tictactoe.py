import os
import time
from itertools import permutations
os.system("cls")
print("\n\n\n\n")
print("WELCOME TO TIC TAC TOE".center(70,' '))
time.sleep(1)
print("\n\n")
print("Loading...".center(75,' '))
time.sleep(3)
os.system("cls")
rules="""
				Rules
		1. choose location from 1 to 9 
		location representation=>
			1	2	3
			4	5	6
			7	8	9
		2. present O for user1 and * for user2.
		3. Keys for playing->1 to 9
		4. 0 for end the game.
		5. Interruption will help to win opposition.
		
		Read The Rules Carefully,You have 10 Seconds
"""
print(rules.center(10,' '))
time.sleep(10)
os.system("cls")
print("\n\n\n\n\n")
print("#####Lets Start#####".center(70,' '))
time.sleep(1)
os.system("cls")
user1=input("			Enter Name of User1:")
print("\n")
user2=input("			Enter Name OF User2:")
print("\n",f"Match:{user1} v\s {user2}".center(72,' '))
print("\n","Loading...".center(75,' '))
print("\n")
time.sleep(3)
os.system("cls")
use=[1,2,3,4,5,6,7,8,9]
win=['147','741','258','852','369','963','123','321','456','654','789','987','159','951','357','753']
li=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
print('\t\t\t',"-"*19)
print('\t\t\t','|     |     |     |')
print('\t\t\t',f'|  {li[0]}  |  {li[1]}  |  {li[2]}  |')
print('\t\t\t','|     |     |     |')
print('\t\t\t',"-"*19)
print('\t\t\t','|     |     |     |')
print('\t\t\t',f'|  {li[3]}  |  {li[4]}  |  {li[5]}  |')
print('\t\t\t','|     |     |     |')
print('\t\t\t',"-"*19)
print('\t\t\t','|     |     |     |')
print('\t\t\t',f'|  {li[6]}  |  {li[7]}  |  {li[8]}  |')
print('\t\t\t','|     |     |     |')
print('\t\t\t',"-"*19)
time.sleep(2)
result1=[]
result2=[]
user1_choice=[]
user2_choice=[]
winner=0
while use:
	if winner==1:
		break
	if len(use)%2:
		print(f"{user1} Turn".center(70,' '))
		print("\n\n")
		choice1=int(input("		Enter Your Position(fill O) :"))
		if choice1==0:
			print(f"		According To Interruption Rule {user2} is win")
			winner=1
			break
		elif choice1 in use:
			li[choice1-1]='O'
			use.remove(choice1)
			user1_choice.append(str(choice1))
		else:
			print("You Entered Wrong Position Which is already filled".center(40,' '))
		os.system("cls")
		print('\t\t\t',"-"*19)
		print('\t\t\t','|     |     |     |')
		print('\t\t\t',f'|  {li[0]}  |  {li[1]}  |  {li[2]}  |')
		print('\t\t\t','|     |     |     |')
		print('\t\t\t',"-"*19)
		print('\t\t\t','|     |     |     |')
		print('\t\t\t',f'|  {li[3]}  |  {li[4]}  |  {li[5]}  |')
		print('\t\t\t','|     |     |     |')
		print('\t\t\t',"-"*19)
		print('\t\t\t','|     |     |     |')
		print('\t\t\t',f'|  {li[6]}  |  {li[7]}  |  {li[8]}  |')
		print('\t\t\t','|     |     |     |')
		print('\t\t\t',"-"*19)
		time.sleep(2)
		if len(use)<5:
			result1=list(permutations(user1_choice,3))
			for var in result1:
				string=''
				for var1 in var:
					string+=var1
				result2.append(string)
			for var in result2:
				if var in win:
					print(f"{user1} is winner".center(70,' '))
					winner=1
					break
			result1=[]
			result2=[]
	
	
	else:
		print(f"{user2} Turn".center(70,' '))
		print("\n\n")
		choice1=int(input("		Enter Your Position(fill *):"))
		if choice1==0:
			print(f"		According To Interruption Rule {user1} is win")
			winner=1
			break
		elif choice1 in use:
			li[choice1-1]='*'
			use.remove(choice1)
			user2_choice.append(str(choice1))
		else:
			print("You Entered Wrong Position Which is already filled".center(40,' '))
		
		os.system("cls")
		print('\t\t\t',"-"*19)
		print('\t\t\t','|     |     |     |')
		print('\t\t\t',f'|  {li[0]}  |  {li[1]}  |  {li[2]}  |')
		print('\t\t\t','|     |     |     |')
		print('\t\t\t',"-"*19)
		print('\t\t\t','|     |     |     |')
		print('\t\t\t',f'|  {li[3]}  |  {li[4]}  |  {li[5]}  |')
		print('\t\t\t','|     |     |     |')
		print('\t\t\t',"-"*19)
		print('\t\t\t','|     |     |     |')
		print('\t\t\t',f'|  {li[6]}  |  {li[7]}  |  {li[8]}  |')
		print('\t\t\t','|     |     |     |')
		print('\t\t\t',"-"*19)
		time.sleep(2)
		if len(use)<5:
			result1=list(permutations(user2_choice,3))
			for var in result1:
				string=''
				for var1 in var:
					string+=var1
				result2.append(string)
			for var in result2:
				if var in win:
					print(f"{user2} is winner".center(70,' '))
					winner=1
					break
			result1=[]
			result2=[]
	
if winner==0:
	print("Match Tie".center(70,' '))
time.sleep(2)
print("\n\n")
print("Thank You For Playing".center(70,' '))
time.sleep(3)
os.system("cls")