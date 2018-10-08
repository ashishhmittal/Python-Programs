#Question 1

li=[]
n=int(input("Enter number of elements you want"))
for i in range(0,n):
    a=int(input("Enter elements of the list"))
    li.append(a)
li.reverse()
print(li)



#Question 2

s=input("Enter a string")
for i in s:
    if(i.isupper()):
        print(i)



#Question 3

s2=input("Enter string of numbers")
s3=s2.split(",")
print(s3)
li2=[]
for i in s3:
    li2.append(int(i))
print(li2)


#Question 4

s4=input("Enter a string")
s6=s4
s5=s4[::-1]
if(s5==s6):
    print("String is Palindromic")
else:
    print("String is not Palindromic")
    


#Question 5

import copy
li3=[1,2,3,[4,5]]
li4=[]
li4=copy.deepcopy(li3)
li4[3][0]='a'
li4[1]='b'
print(li3)
print(li4)

#In case of shallow copy, a reference of object is copied in other object. It means that any changes made to a copy of object do reflect in the original object.
#In case of deep copy, a copy of object is copied in other object. It means that any changes made to a copy of object do not reflect in the original object.



        
