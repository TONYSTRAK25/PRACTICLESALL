n = int(input("enter a number"))
a,b=0,1

for i in range(n):
    print(f"the fibonanci number is : {a}")
    a,b=b,a+b
