# creating gcd computing program as practise
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

num1=int(input("enter first value:"))
num2=int(input("enter second value:"))

print(gcd(num1,num2))