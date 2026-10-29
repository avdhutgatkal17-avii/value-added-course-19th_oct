#Lowest Common Multiple (LCM) of Two Numbers :

def findLcm(n1, n2):
    # Write your code here
    if n1 == 0 or n2 == 0:
        return 0 

    a,  b = n1, n2
    while b:
        a, b= b, a%b

    return abs(n1 * n2) //a