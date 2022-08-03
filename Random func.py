import random
n=random.randbytes(3)
print(n)
print(random.randrange(1,8))
print(random.randint(100,211))
mylist=["Jadeja","MS Dhoni","Virat Kohli","KL Rahul"]
mylist1=["Jadeja","MS Dhoni","Virat Kohli","KL Rahul"]
print(random.choice(mylist))
print(random.choice(mylist1))
random.shuffle(mylist)


