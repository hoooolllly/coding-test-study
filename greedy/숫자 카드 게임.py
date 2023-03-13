n,m = map(int, input().split())

answer = 0
mat = []

for _ in range(n):
    mat.append(list(map(int,input().split())))

for list_ in mat:
    answer = max(min(list_), answer)

print(answer)