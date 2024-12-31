#정수 a를 정수 b로 변환하려고 하는데, 가능한 연산은 다음과 같이 두가지이다.
# 2를 곱하는 연산
# # 1을 수의 가장 오른족에 추가하는 연산
A,B = map(int,input().split())
while(B ==A):
    if B % 2 == 0:
        B //= 2
    else: # 홀수일때
        B = str(B)
        B.replace(B[-1],'')






# B = 123
# B = str(B)
# print(B.replace(B[-1],''))
# print(B,type(B))
# # print(B[0],B[1])
# # B =int(B)
# # print(B,type(B))