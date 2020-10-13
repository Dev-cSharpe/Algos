n=int(input('Enter a number'))

res=[]
while n>=1:
    res.append(n%2)
    n=n//2

print(res[::-1])