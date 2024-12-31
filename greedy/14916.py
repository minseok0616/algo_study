# #거스름돈의 종류
# change = [5,2]
# total = int(input())

# count = 0
# for coin in change:
#     count += total //coin
#     total %= coin

# if total == 0 :
#     print(count)
# else:
#     print('-1')

# 개선된 버전
total = int(input())
count = 0
while total>0:
    if total % 5 == 0:
        count += total //5 #5로 나누어 떨어질 경우에 5원을 최대한 사용하기
        total =0
    else: # 5로 나누어 떨어지지않는 경우에 2원을 하나 사용하기
        total -= 2
        count += 1

if total ==0:
    print(count)
else:
    print(-1)        
        