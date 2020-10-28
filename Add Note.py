## Simple program to meet my needs of making notes- on click- in wordpad(because it is lite and quick), and naming of the notes done on the basis of date and time ##


import os
from datetime import datetime
import subprocess

path='C:\Program Files\Windows NT\Accessories'  ## the path where wordpad exists

now=str(datetime.now())
date,time=now.split()
hours,mins,secs=time.split(sep=":")
secs=str(int(float(secs)))

time=f'{hours}-{mins}-{secs}'

f=f'{date}---{time}'

with open(f'{f}.rtf','w') as fi: pass

a=str(os.getcwd())  ## The script would make notes in whichever directory it exists in ##
listi=a.split(sep='\\')
se='/'
address=se.join(listi)

os.chdir(path)

subprocess.Popen(['wordpad.exe',f'{address}/{f}.rtf'])






