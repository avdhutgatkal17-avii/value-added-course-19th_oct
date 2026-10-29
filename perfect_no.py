#check for perfect no:

def isPerfectNumber(n):
    # Write your code here
    if n <=1:
        return False
    sum=1

    i=2
    while i*i<=n:
        if n%i==0:
            sum+=i 
            if i*i != n:
                sum+=n//i 

        i +=1
    return sum == n