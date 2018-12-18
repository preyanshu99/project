from getpass import getpass
import os
import random
x=random.randint(1,9)
os.system("cls")
import time
os.system(f"color {x}")
print("\n\n\t\t\t***Rock Paper Scissor***")
time.sleep(3)
print("\n\t\t\t\t***Game Start***")
time.sleep(1)
os.system("cls")
y=random.randint(1,9)
os.system(f"color {y}")
player1=input("\n\t\tEnter name of player1:")
player2=input("\n\t\tEnter name of player2:")
os.system("cls")
print("\n\t\tChoices:\n\t\t1.Rock\n\t\t2.Paper\n\t\t3.scissor")
a1=eval(getpass("\n\tEnter choice of player1(this is hidden):"))
time.sleep(2)
a2=eval(getpass("\n\tEnter choice of player2(this is hidden):"))
choice={1:'rock',2:'paper',3:'scissor'}
choice1=choice[a1]
choice2=choice[a2]
if (choice1==choice2):
    print("\n\t\tMatch Tie")
elif choice1=='rock' and choice2=='scissor':
    print("\n\t\t",player1," Win")
elif choice1=='rock' and choice2=='paper':
    print("\n\t\t",player2, "Win")
elif choice1=='paper' and choice2=='scissor':
    print("\n\t\t",player2," Win")
elif choice1=='paper' and choice2=='rock':
    print("\n\t\t",player1," Win")
elif choice1=='scissor' and choice2=='paper':
    print("\n\t\t",player1," Win")
elif choice1=='scissor' and choice2=='rock':
	print("\n\t\t",player2," Win")