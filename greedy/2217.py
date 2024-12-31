#로프

# 각각의 로프는 굵이 길이가 다르기에 들 수 있는 중량이 서로 다를 수 있다.
# 하지만, 여러개의 로프를 병렬로 연결하면 각각 로프에 걸리는 중량 나누기 가능
# k개의 로프를 사용해서 중량이 w인 물체를 들어올릴때 각 로프마다 w/k의 중량이 걸린다.
# 로프 정보가 주어졌을때 로프들을 사용해서 들어올릴 수 있는 최대 중량을 구하시오
# 모든 로프를 사용할 필요는 없음
# k = int(input()) # 로프 개수
# rope =[]
# for i in range(k):
#     rope_type = int(input())
#     rope.append(rope_type)


# print(min(rope)*k)
# 로프를 쓰지 않아도 되는점을 유의할 것
k = int(input())
rope = []
result = []
for i in range(k):
    rope_type = int(input())
    rope.append(rope_type)#로프 종류를 리스트에 추가함

rope.sort(reverse=True) #내림 차순 정렬을 진행함

for j in range(k):
    result.append(rope[j]*(j+1))

print(max(result))