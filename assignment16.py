#Question 1

import pymongo
client=pymongo.MongoClient()
database=client['Students']
collection=database['student']
#Question 2

for i in range(10):
    try:
        name = input("Enter the name: ") 
        marks = int(input('Enter your Marks: '))
        if(marks<0 or marks >100):  
            raise ValueError('Invalid entry of marks')
            i=i-1
        else:#Question 3
            collection.insert_one({'Name':name,'Marks':marks})  
            i=i+1
    except  ValueError as msg:
        print(msg)
        
#Question 4
db=collection.find({"Marks":{"$gt":80}})
for data in db:
    print(data)
