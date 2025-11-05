def fibonacci(n, a=0, b=1):
    if n == 0:
        return
    print({a})
    fibonacci(n-1, b, a+b)

# Main part
n = int(input("Enter the number of terms: "))
print("Fibonacci Sequence :")
fibonacci(n)


def fibo(a,b,n):
    a=0
    b=1

    if n==0:
        return
    print({a})
    fibo(n-1,b,a+b)
