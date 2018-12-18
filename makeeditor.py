"""This is a editor to creating file and stored in specified location by User."""
import time
import os
import random
os.system("cls")
os.system("color 3")
print("\n\t\t\t-#-#-Welcome To The Make Editor-#-#-")
print("\n\t\t\tInstruction Read Carefully:")
s="""
			1.Enter data line by line
			2.For Finish file type eof
			3.After Finishing Specify the file name either with location which is not mandatory
"""
print(s)
time.sleep(10)
os.system("cls")
print("\n\t\t\t#####Let's Write Content Carefully#####")
para=''
print("\n\n\t\t\t-*-*-Enter Line By Line-*-*-")
time.sleep(2)
os.system("cls")
while True:
	string=input()
	if string.strip().lower()=='eof':
		break
	para=para+string+'\n'
file=input("Enter File Name(location not mandatory):")
if os.path.exists(file) or os.path.exists(file+'.txt'):
	file=file+str(random.randint(100,99999999))
if file.find('.')==-1:
	file+='.txt'
f=open(file,"w")
f.write(para)
print(f"\n\t\tFile {file} Successfully Created")
f.close()