# 최대 공약수 구하기
a = 10
b = 12

for i in range(min(a, b), 0, -1):
    if(a % i ==0) and (b % i == 0):
        print(i)
        break

while(b>0):
    a, b = b, a%b
print(a)

# 최소 공배수 구하기
a = 100
b = 84

def GCD(a, b):
    while(b>0):
        a, b = b, a%b
    return a
result = (a*b) // GCD(a, b)
print(result)
print(GCD(a,b))


