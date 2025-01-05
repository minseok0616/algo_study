#알바생 강호
#총 팁 - 인덱스 번호의 합 => 이게 팁인데
# 고려 해야될게 음수가 나와서 팁이 0원이 되는 경우를 고려해야한다.
#내림차순 정렬해서 계산해서 음수일때 팁 0원으로 바꿔서 더하면 끝인듯.
n = int(input())
tip = []
for i in range(n):
    tip.append(int(input()))

tip.sort(reverse=True)
result = 0
for j in range(n):
    if tip[j] - j >0:
        result += tip[j] - j 

print(result)