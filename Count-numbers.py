#Count of Prime Numbers till N:

def countPrimes(n):
    # Write your code here
    if n < 2:
        return 0

    pr=[True] * (n+1)
    pr[0]=pr[1]=False

    i = 2
    while i * i<=n:
        if pr[i]:
            for j in range (i*i,n+1,i):
                pr[j]=False

        i+=1

    return sum(pr)