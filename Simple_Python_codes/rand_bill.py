import random
names=input("friends names : ")
list=names.split(",")
print(list)
count=len(list)
print(count)
choice=random.randint(0,count-1) 
print( f"{list[choice]} will pay the bill")