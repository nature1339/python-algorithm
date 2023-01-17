n = int(input())
Ai = list(map(int, input().split()))
B, C = map(int, input().split())

answer = n

for i in Ai:
     i = i - B
     if i > 0:
       if i % C:
          answer += (i // C) + 1
       else:
           answer = (answer + (i//C))

print(answer)