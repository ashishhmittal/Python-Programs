#List Comprehension and generator expression

#Question 1

a=[1,2,3,4]
a=[i**3 for i in a]
print(a)


#Question 2

a=[i for i in range(2,20)  for j in range(2,i) if(i%j==0)  ]
b=[i for i in range(2,20) if(i not in a )]
print(b)


#Question 3

'''
In terms of syntax, the only difference is that you use parenthesis instead of square brackets.

The type of data returned by list comprehensions and generator expressions differs.

The generator yields one item at a time — thus it is more memory efficient than a list.'''

#Lambda and Map

#Question 1

Celsius = [39.2 ,36.5, 37.3, 37.8]
f=list(map(lambda x: 1.8*x+32,Celsius))
print(f)

#Question 2

lst=[1,2,3]
def squ(n):
    return n*n
s=list(map(lambda n:squ(n),lst))
print(s)

#Filter and Reduce


#Question 1

lst=[1,2,3,4,5,6,7,8,9]
def isprime(n):
    flag=1
    if(n>1):
        for i in range(2,n):
        
            if(n%i==0):
                flag=0
                break
        if(flag==1):
            return n
    
p=list(filter(lambda n: isprime(n),lst))
print(p)


#Question 2
lst=[1,2,3,4,5,5]
from  functools import *
m=reduce(lambda x,y:x*y,lst)
print(m)
    
    
