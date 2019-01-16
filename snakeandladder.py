import os
import time
import random
os.system("cls")
os.system("color 3")
print("\n\n\n\n")
print("WELCOME TO THE GAME".center(70,' '))
time.sleep(1)
print("\n\n")
print("#####SNAKE AND LADDER#####".center(70,' '))
time.sleep(3)
os.system("cls")
rules="""
			Rules and Instruction
		1. There are 100 boxes,The player who reach to last box 
		   first is the winner.
		2. present * for player1 and O for player2.
		3. press y or Y for playing your dice.
		4. on getting 6 you get an extra chance.
		5. Only on when player get 1 he enter into the boxes.
		6. The snake or danger points increase your distance and 
		   ladder or help point decrease your distance to winning 
		   point.
		
		
		Read The Rules Carefully,You have 10 Seconds
"""
print(rules.center(10,' '))
time.sleep(10)
os.system("cls")
print("\n\n\n\n\n","#####Lets Start#####".center(70,' '))
print("\n\n","Loading...".center(70,' '))
time.sleep(2)
os.system("cls")
print("\n\n")
player1=input("\n\t\t\tEnter Name Of Player1:").strip().capitalize()

while player1=='' or player1=='\n':
	print("You Enter Wrong Name".center(70,' '))
	print("Please Enter Correct Name".center(70,' '))
	player1=input("\n\t\t\tEnter Name Of Player1:").strip().capitalize()
player2=input("\n\t\t\tEnter Name Of Player2:").strip().capitalize()

while player2=='' or player2=='\n' or player2==player1:
	print("You Enter Wrong Name".center(70,' '))
	print("Please Enter Correct Name".center(70,' '))
	player2=input("\n\t\t\tEnter Name Of Player2:").strip().capitalize()

print("\n  ",f"Match:{player1} v\s {player2}".center(70,' '))
print("\n","Loading...".center(70,' '))
time.sleep(3)
os.system("cls")
value1=0
value2=0
li=[]
for var in range(100,0,-1):
	if var<10:
		string=' '+str(var)+' '
		li.append(string)
	elif var>=10 and var<100:
		string=' '+str(var)
		li.append(string)
	else:
		li.append(str(var))
danger=[random.randint(21,99) for var in range(7)]
help=[]
i=0
while i<7:
	x=random.randint(2,80)
	if x not in danger:
		help.append(x)
		i+=1
dict1={}
dict2={}
for var in danger:
	dict1[var]=random.randint(5,15)
for var in help:
	dict2[var]=random.randint(5,15)
danger.sort()
help.sort()
copy=li.copy()

print("_"*61)
count=0
for var in copy:
	if count==0:
		print("|     "*10,"|",sep='')
	print("|",var,end=" ")
	count+=1
	if count==10:
		count=0
		if var==' 1 ':
			print("|<-Start")
		else:
			print("|")
		print("|_____"*10,"|",sep='')

count1=0
winner=0
remain1=100
remain2=100
while value1<=100 and value2<=100:
	while count1==0:
		print("\n",f"{player1} Turn".center(70,' '))
		print("\n","Helful Points:".center(70,' '),*help)
		print("\n","Danger Points:".center(70,' '),*danger)
		choice=input("			press y for your dice point:").strip().lower()
		luck=0
		if choice!='eof':
			luck=random.randint(1,6)
			if value1==0 and luck==1 and remain1>=luck:
				value1+=luck
				count1=1
			elif value1==0 and luck>1 and remain1>=luck:
				count1=1
			elif value1>=1 and luck<=5 and remain1>=luck:
				value1+=luck
				count1=1
			elif value1>=1 and luck==6 and remain1>=luck:
				value1+=luck
			
			if value1 in danger:
				value1=value1-dict1[value1]
				if value1<0:
					value1=0
			if value1 in help:
				value1=value1+dict2[value1]
				if value1>100:
					value1=100
			reamin1=remain1-value1
			os.system("cls")
			print("\n",f"{player1} get {luck} point".center(70,' '))
			print(f"{player1} present at {value1} position".center(70,' '))
			print(f"{player2} present at {value2} position".center(70,' '))
		else:
			winner=1
			print("\n\n",f"According to the rules {player2} is winner".center(70,' '))
			break
		print("_"*61)
		copy=li.copy()
		if value1>=1:
			copy[100-value1]=' * '
		if value2>=1:
			copy[100-value2]=' O '
		if value1==value2 and value1>0:
			copy[value1-1]='*,O'
		count=0
		for var in copy:
			if count==0:
				print("|     "*10,"|",sep='')
			print("|",var,end=" ")
			count+=1
			if count==10:
				count=0
				if var==' 1 ':
					print("|<-Start")
				else:
					print("|")
				print("|_____"*10,"|",sep='')
		if value1==100:
			winner=1
			print("\n",f"{player1} is the winner")
		
	if winner==1:
		break
		
	while count1==1:
		print("\n",f"{player2} Turn".center(70,' '))
		print("\n","Helful Points:".center(70,' '),*help)
		print("\n","Danger Points:".center(70,' '),*danger)
		choice=input("			press any key(except eof) for your dice point:").strip().lower()
		luck=0
		if choice!='eof':
			luck=random.randint(1,6)
			if value2==0 and luck==1 and remain2>=luck:
				value2+=luck
				count1=0
			elif value2==0 and luck>1 and remain2>=luck:
				count1=0
			elif value2>=1 and luck<=5 and remain2>=luck:
				value2+=luck
				count1=0
			elif value2>=1 and luck==6 and remain2>=luck:
				value2+=luck
			
			if value2 in danger:
				value2=value2-dict2[value2]
				if value2<0:
					value2=0
			if value2 in help:
				value2=value2+dict2[value2]
				if value2>100:
					value2=100
			remain2=remain2-value2
			os.system("cls")
			print("\n",f"{player2} get {luck} point".center(70,' '))
			print(f"{player1} present at {value1} position".center(70,' '))
			print(f"{player2} present at {value2} position".center(70,' '))
		else:
			winner=1
			print("\n\n",f"According to the rules {player1} is winner".center(70,' '))
			break
		print("_"*61)
		copy=li.copy()
		if value1>=1:
			copy[100-value1]=' * '
		if value2>=1:
			copy[100-value2]=' O '
		if value1==value2 and value1>0:
			copy[value1-1]='*,O'
		count=0
		for var in copy:
			if count==0:
				print("|     "*10,"|",sep='')
			print("|",var,end=" ")
			count+=1
			if count==10:
				count=0
				if var==' 1 ':
					print("|<-Start")
				else:
					print("|")
				print("|_____"*10,"|",sep='')
		if value2==100:
			winner=1
			print("\n",f"{player2} is the winner")
		
	if winner==1:
		break
