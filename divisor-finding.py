#Find Divisors of a Number:

def findDivisors(n):
    # Write your code here
    l=[]
    for i in range(1,n+1):
        if n%i ==0:
            l.append(i)

    return l