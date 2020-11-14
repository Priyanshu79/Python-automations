import os
import subprocess

path1='C:\Program Filea\SumatraPDF'  ##path of sumatra pdf, bruh
path2='C:\Program Files (x86)\PDFlite'  ##Path of pdflite

path3='C:/Users/HP/Desktop/Folder'  ##path where your folders whose files are to be opened exist

Folder1_name="PDF_list_2"  ##Folder_name
Folder2_name="PDF_list_1"  ##Folder_name

x=int(input("Enter:\n 1 to open all files in PDF_list_2 with Sumatra PDF\n 2 to open all files in PDF_list_1 with PDFlite\n 3 to open all files in a folder in PDF_list_1 with PDFlite\n"))

if x==1:
    os.chdir(path1)
    for file in os.listdir(f"{path3}/PDF_list_2"):
        subprocess.Popen(['SumatraPDF.exe',f'{path3}/{Folder1_name}/file'])  
elif x==2:
    os.chdir(path2)
    for root, dirs, files in os.walk(f"{path3}/{Folder2_name}",topdown=False):
        for file in files:
            subprocess.Popen(['PDFlite.exe',os.path.join(root, file)])  
elif x==3:
    os.chdir(path2)
    #input("Enter the folder name"
    i=1
    dicti={}
    for root, dirs, files in os.walk(f"{path3}/{Folder2_name}",topdown=False):
        for dir in dirs:
            dicti[i]=dir
            i+=1
    string=""
    for item in dicti:
        string+=f"{item} :- {dicti[item]}\n"
    y=int(input(f"\nEnter the corresponding number to the directory whose files you wanna open:\n{string}"))
    for file in os.listdir(f"{path3}/{Folder2_name}/{dicti[y]}"):
        subprocess.Popen(['PDFlite.exe',f'{path3}/{Folder2_name}/{dicti[y]}/{file}'])  

    

        





