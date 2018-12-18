import time
print("Enter month and year to show the calender")
year=int(input("Enter Year:"))
month=int(input("Enter month:"))
if year<=0 or month<=0 or month>12:
    print("Enter Valid Year and Month")
    exit(0)

if year%4==0 and year%100==0 and year%400==0:
    feb=29
elif year%4==0 and year%100!=0:
    feb=29
else:
    feb=28

month_day=[31,feb,31,30,31,30,31,31,30,31,30,31]
li=[100,4,1]
year1=year-1
year1=year1//400
year1=year-400*year1
extra=[]
for var in li:
    num=year1//var
    year1=year1-var*num
    if var==100:
        extra.append(num*5)
    elif var==4:
        extra.append(num*5)
    elif var==1:
        extra.append(num*1)
first_day=0
for var in range(1,month):
    first_day=first_day+month_day[var]
for var in range(len(extra)):
    first_day=first_day+extra[var]
first_day=first_day%7
day_list=[0,1,2,3,4,5,6]
first_day=day_list[first_day]
dic={0:'Sunday',1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday'}
print("Month Start with:",dic[first_day])
print("S  M  T  W  T  F  S ")
space=first_day
print("__ "*space,end="")
for var in range(1,month_day[month-1]+1):
    if space==7:
        print("")
        space=0
    if var<10:
        print("0",end="")
    print(var,end=" ")
    space=space+1

time.sleep(20)    