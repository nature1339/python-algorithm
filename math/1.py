n = int(input())
Ai = list(map(int, input().split()))
B, C = map(int, input().split())

answer = n #총감독관

for i in Ai:
    i = i - B           
    if i > 0:
        if i % C:  # 나누어 떨어지지 않을때
            answer = answer + (i//C)+1
    
        else:     #나누어 떨어질때
            answer = answer + (i//C)

print(answer)        

# list(map(int, str(1023)))
    