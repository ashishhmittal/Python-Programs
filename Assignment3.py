#Assignment 3

#Question 1

li = []
x = int(input("enter the the number of elementss you want to add in the list "))
for i in range(x):
    li.append(input("enter the value you want to add in the list"))
print(li)


#Question 2

li2 = ['google','apple','facebook','microsoft','tesla']
li.extend(li2)
print(li)

#Question 3

li1 = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,3,5,6,4,6,4,64,5]
print(li1.count(1))


#Question 4

li4 = [5,3,6,3,6,3,6,2345,2,426,663,16,31,6,34]
li4.sort()
print(li4)

#Question 5

li5 = [1,2,3,4,5]
li6 = [6,7,8,9]
li7=[]
li5.extend(li6)
li7=li5
li7.sort()
print(li7)


#Question 6

e=0
o=0
for i in li5:
    if(i%2==0):
        
        
        e=e+1
    else:
      
        o=o+1
    
print("Count of even numbers in the list =",e)
print("Count of odd numbers in the list =",o)





#TUPLES

#Question 1
t=(1,2,3,4)
print(t[::-1])


#Question 2
t2=(1,2,3,4)
print("Largest element is =",max(t2))
print("Smallest element is =",min(t2))




#STRINGS

#Question 1
s='abc'
s1=s.upper()
print(s1)


#Question 2
s2='1234'
s4='12abc'
s3=s2.isdigit()
s5=s4.isdigit()
print(s3)
print(s5)


#Question 3
s6='hello world'
s7=s6.replace('world','Ashish')
print(s7)





