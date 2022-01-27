n = int(input("Enter an Integer:", ))
i = int(input("Enter 0 or 1:", ))

if i == 0:
    b = False
else:
    b = True

if b:
    l = 1
    while n!=0:
        m = l
        n-=1
        while m!=0 :
            print("*", end = "")
            m-=1
        l+=1
        print()
else:
    while n!=0:
        m = n
        n-=1
        while m!=0 :
            print("*", end = "")
            m-=1
        print()