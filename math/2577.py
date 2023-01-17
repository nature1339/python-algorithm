A = int(input())
B = int(input())
C = int(input())

# 1, 3, 5, 7, 0, 0, 2, 3
list_number = list(map(int, str(A*B*C)))

list_9 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in list_number:
    list_9[i] += 1
for i in [1,7,0,3,7,3,0,0 ]:
    list_9[i] += 1    

for i in list_9:
    print(i)
   
    
    
        


