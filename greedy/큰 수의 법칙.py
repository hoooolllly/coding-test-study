n,m,k = map(int, input().split())
num_list = list(map(int,input().split()))

num_1 = max(num_list)
num_list.remove(num_1)
num_2 = max(num_list)

answer = 0
cnt = 0

for i in range(m):
    cnt += 1
    
    if cnt <= k:
        answer += num_1
    
    else :
        answer += num_2
        cnt = 0

print(answer)