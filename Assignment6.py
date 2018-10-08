#Question 1

def area(r):
    a=(4/3)*3.14*r*r*r
    print("Area of the sphere is",a)
radius=int(input("Enter radius of the sphere"))
area(radius)

#Question 2

def perfect(n):
    s=0
    for i in range(1,(n//2)+1):
        if(n%i==0):
            s=s+i
    if(s==n):
        print(n)
       
for j in range(1,1001):
    perfect(j)


#Question 3

n=int(input("Enter a number to check its multiplication table"))
for i in range(1,11):
    m=n*i
    print("{} * {} = {}".format(n,i,m))


#Question 4

def power(x,y):
    if(y==1):
        return(x)
    if(y!=1):
        return(x*power(x,y-1))
x=int(input("Enter the number "))
y=int(input("Enter the number to be the power "))
print(power(x,y))
