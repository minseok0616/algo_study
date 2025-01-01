A,B = map(int,input().split())
count = 0
check = 0
while B != A and B>=A:
    if B % 10 == 1: # 1이 나온경우를 뜻함.
        B //= 10
        count += 1
    elif B % 2 == 0:
        B //= 2
        count +=1
    else:
        check = 1
        break

if not check and A==B:
    print(count + 1)
else:
    print(-1)

