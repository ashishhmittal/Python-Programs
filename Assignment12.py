#Question 1

import datetime 
date=datetime.datetime.now()
print(date.day)


#Question 2

import webbrowser as web
web.open("https://www.youtube.com/watch?v=FAlWb1i0ZrQ")


#Question 3

import os
os.chdir("F:\changedirectory")#Used to change working directory
path =  os.getcwd()#Returns current working directory
filenames = os.listdir(path)#Returns list of files in the current directory
i=1
print(filenames)

for filename in filenames:
    os.rename(filename,str(i)+'.jpg')
    i=i+1


