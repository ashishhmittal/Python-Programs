#Question 1
dic=eval(input('Enter the dictionary'))
e=int(input("Enter the value"))
for i in dic.items():
    if(e==i[1]):
        print(i[0])


        
#Question 2
dic1={}
for i in range(2):
    s=input("Enter student name")
    for j in range(2):
        sub=input("Enter the subject ")
        marks=input("Enter marks")
        dic1[s,sub]=[sub,marks]
print(dic1)
name=input("Enter name of the student to check marks")
for j in dic1.items():
    for r in range(2):
        if(j[r][0]==name):
            print(j[1])
