
# 1. 필요한 n, point, p 입력
# 2. n이 0인지 아닌지 체크
# 3. n이 0이 아닐때, ranking_list 입력

# 4. 랭킹리스트에 등록된 점수의 개수 = 랭킹 리스트에 최대로 등록될수있는 수, 점수가 랭킹리스트 끝값보다 작거나 같으면, -1
# 5. 반복문을 통해서 ranking_list 조회

N,T,P = map(int, input().split())

if N == 0 : print(1)
else:
    current_ranking = list(map(int, input().split()))
    if N == P and T <= current_ranking[-1]: print(-1)
    else:
        rank = N + 1
        for i in range(len(current_ranking)):
            if current_ranking[i] <= T:
                rank = i + 1
                break
        print(rank)

# for i in ranking_list:
#     if N == 0:
#         T = 1

#     else:
#         ranking_list.append()

# print(ranking_list[i])

# if P == len(ranking_list):
#     print(-1)






    
    