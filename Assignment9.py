#QUESTION 1
try:
    a=3
    if a<4:
        a=a/(a-3)
        print(a)
except ZeroDivisionError:
    print("it is ZeroDivisionError as you can not divide a number by zero")

#Question 2
l=[1,2,3]
try:
    print(l[3])
except:
    print("It is IndexError.")

#Question 3
print("""An exception
'after this error occur'""")

#Question 4
print("""Output:
-5.0
a/b result in 0"""

#Question 5
try:
    import xyz
except ImportError:
    print("It is import error because no such module is present")
try:
    z=int(input("Enter number"))
except ValueError:
    print("Please enter  number not string")
try:
    l=[1,2,3]
    i=int(input("Enter the index"))
    print(l[i])
except IndexError:
    print("Invalid index")
