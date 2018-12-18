import os
import random
import time
os.system("cls")
x=random.randint(1,9)
os.system(f"color {x}")
print("\n\t\t*-*-*Truth Date Situation Game*-*-*")
time.sleep(1)
d=int(input("\n\t\t\tEnter Date:"))
m=int(input("\n\t\t\tEnter Month:"))
y=int(input("\n\t\t\tEnter Year:"))
print("\n\t",end=" ")
for var in range(10):
    print("_____",end=' ')
    time.sleep(0.5)
	
if y%4==0:
    if y%100==0:
        if y%400==0:
            fabday=29
        else:
            fabday=28
    else:
        fabday=29
else:
    fabday=28

date={1:31,2:fabday,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
if m<=12 and m>0:
	monthday=date[m]

if d<=0 or d>31 or m<=0 or m>12 or y<=0:
    print("\n\n\t\tYour Input Date is Wrong")
elif d>monthday:
    print("\n\n\t\tYour Input Date is Wrong")
elif d<=monthday:
    print(f"\n\n\t\tYour Input Date {d}|{m}|{y} is correct")
	
print("\n\t",end="")	
for var in range(10):
	print("______",end="")
	time.sleep(0.5)
print("\n\n")
	
