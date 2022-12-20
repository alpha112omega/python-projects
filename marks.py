def var(k):
    """ this is a comment """
n=int(input("enter a number"))
m = int(input("enter second number"))
odd_value = []
odd_count =0
even_value = []
even_count =0
prime_value = []
prime_count =0
for num in range(n, m+1):
    if(num % 2 != 0):
        odd_value.append(num)
        odd_count += 1
    else:
        even_value.append(num)
        even_count += 1
    for x in range(2,num):
        if(num%x==0):
            break
    else:
        prime_value.append(num)
        prime_count+=1
print(f"total odd{odd_count} numbersare{odd_value}")
print(f"total even{even_count} numbers are {even_value}")
print(f"total prime{prime_count} numbers are {prime_value}")
    