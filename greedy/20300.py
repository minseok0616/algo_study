#서강근육맨
#운동기구를 2개까지만 선택할 수 있다.
# 헬스장에 N개의 기구가 있는데, 매번 다른거 써보고 싶어서 전에 쓴건 안씀, 그리고 비용절감을 위해 되도록이면
# 한 번갈때 2개를 사용함, 10개가 잇다고 하면 5번가면 다써볼수 있음
#근손실정도가 M을 넘지않게 하고 싶다

# 리스트 입력받기
n = int(input())
stress = list(map(int,input().split()))
stress.sort(reverse=True)# 내림차순 정렬하기
result = 0
stress_sum = list()
if n % 2 == 0: #n의 개수가 짝수 일 때
    for i in range(n//2):
        stress_sum.append(stress[i]+stress[-(i+1)])
    print(max(stress_sum))
else:
    for i in range(n//2):
        stress_sum.append(stress[i+1]+stress[-(i+1)])
    print(max(max(stress),max(stress_sum)))
