s = int(input())

n = 0
temp = 0 # n개 까지의 숫자 합

while True:
    n += 1
    temp += n     
    if temp > s:
        break
    
print(n-1)