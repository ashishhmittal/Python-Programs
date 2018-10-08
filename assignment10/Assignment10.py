
#Question 1
f=open('test.txt')
lines=f.readlines()
print(lines)
x=int(input("ENTER: "))
for i in range(x):
    print(lines[i])
f.close()



#Question 2
li=[]
dic={}
f=open('test2.txt')
data=f.read()
print(data)
li=(data.split())
for i in li:
    dic[i]=li.count(i)
print(dic)
f.close()


#Question 3
f=open('test2.txt')
g=open('test1.txt','w')
data=f.read()
g.write(data)
g.close()
g=open('test1.txt')
data2=g.read()
print(data2)
g.close()
f.close()


#Question 4
with open('test.txt') as f1,open('test1.txt') as f2 ,open('combine.txt','w') as f3:
    for i,j in zip(f1,f2):
        f3.write(i+j)


#Question 5
li3=[]
f=open('test3.txt','w')
for i in range(10):
    a=input('Enter the numbers in the file')
    f.write(a)
    f.write('\n')
f.close()
f=open('test3.txt')
data=f.read()
data2=data.split()
print(data2)
for i in data2:
    li3.append(int(i))
li3.sort()
data3=','.join(map(str,li3))
f2=open('test4.txt','w')
f2.write(data3)
f2.close
f2=open('test4.txt')
data4=f2.read()
print(data4)



