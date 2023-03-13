n,k = map(int, input().split())

answer = 0

while n != 1:
    
#    if k == 1:
#        answer = n-1
#        break

    answer += 1
    
    if n % k == 0:
        n //= k
    else:
        n -= 1

print(answer)