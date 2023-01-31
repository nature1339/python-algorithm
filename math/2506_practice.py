n = int(input())
score = list(map(int, input.split()))
expect_number = 0
answer = 0
 
 
for i in score:
    if i == 1:
        expect_number += 1
        answer += expect_number
            
    else: 
        expect_number = 0

print(answer)
          
 