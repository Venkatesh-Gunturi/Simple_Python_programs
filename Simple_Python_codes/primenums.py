n=int(input("enter a number :"))
if n>1:
    for i in range(2,n):
        if n%i==0:
            print("not a prime")
            break
    else:
        print("prime")
elif n==1:
    print("neither composite nor prime")
elif n==0:
    print("zero")
elif n<0:
    print("-ve")