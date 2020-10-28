## A simple cp environment setup script, inclined towards my purposes slightly, but is definitely hackable to suit anyones! ##


from datetime import datetime
import os
from math import ceil

num=int(input("Number of questions: "))
cp_path="D:\Competitive Programming"

x=str(datetime.now(tz=None))

date,time=x.split()
year,month,day=date.split(sep="-")
hours,minutes,sec=time.split(sep=":")
sec=str(ceil(float(sec)))

datef=f"{day}-{month}-{year}"
timef=f"{hours}-{minutes}-{sec}"

string=(f"{datef}___{timef}")

if os.getcwd() != cp_path: os.chdir(cp_path)

os.mkdir(string)

os.chdir(f"{cp_path}\{string}")


for x in range(1,num+1):
    os.mkdir(str(x))
    os.chdir(f"{cp_path}\{string}\{x}")
    current_folder=f"{cp_path}/{string}/{x}"
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
    os.chdir(f"{cp_path}\{string}")


