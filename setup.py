from datetime import datetime
import os
from math import ceil

num=int(input("Number of questions: "))

x=str(datetime.now(tz=None))

date,time=x.split()
year,month,day=date.split(sep="-")
hours,minutes,sec=time.split(sep=":")
sec=str(ceil(float(sec)))

datef=f"{day}-{month}-{year}"
timef=f"{hours}-{minutes}-{sec}"

string=(f"{datef}___{timef}")

if os.getcwd() != "D:\Competitive Programming": os.chdir("D:\Competitive Programming")

os.mkdir(string)

os.chdir(f"D:\Competitive Programming\{string}")



for x in range(1,num+1):
    os.mkdir(str(x))
    os.chdir(f"D:\Competitive Programming\{string}\{x}")
    current_folder=f"D:/Competitive Programming/{string}/{x}"
    stri=f'''
import sys
sys.stdout = open(f'{current_folder}/out.txt', 'w')
sys.stdin = open(f'{current_folder}/in.txt', 'r')

##-----------------------------------------##

#for _ in range(int(input())):

'''
    open("in.txt","w")
    open("out.txt","w")
    with open("code.py","w") as c:
        c.write(stri)
    os.chdir(f"D:\Competitive Programming\{string}")


