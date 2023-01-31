x,y,w,h = map(int, input().split())

temp_min = 1001

for i in [h-y, w-x, x, y]:
    if i < temp_min:
        temp_min = i

print(temp_min)
