#첫째 줄에 빈 칸을 사이에 두고 x(1 ≤ x ≤ 12)와 y(1 ≤ y ≤ 31)이 주어진다. 
# 참고로 2007년에는 1, 3, 5, 7, 8, 10, 12월은 31일까지, 4, 6, 9, 11월은 30일까지, 
# 2월은 28일까지 있다

x, y = map(int, input().split())

list_answer = [
    "SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"
    ]

month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

diff = 0

for i in range(x - 1):    
    diff = diff + month[i]  
    
diff += y

print(list_answer[diff % 7])
        


#print( "2007년 x월 y일은 {}요일".format())
