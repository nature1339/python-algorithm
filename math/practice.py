n = int(input())
Ai = list(map(int, input().split()))
B, C = map(int,input().split())#총감독수 b, 부감독수 c

answer = n # 총감독수

for i in Ai:
    i = i - B # i는 총감독수 - 총감독관b =나머지 감독관수
    if i > 0: # 나머지 감독관수 > 0
        if i % C:   #나머지 감독관수를 부감독으로 나눈수    
            answer = answer + (i // C) + 1
        else:
            answer = (answer + (i//C))

print(answer)
