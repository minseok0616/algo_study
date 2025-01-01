n = input()
m = 0
max_result = ''
min_result = ''
cnt = 0
for i in n:
    if i == 'K':
        if m > 0:
            max_result += str(5 * 10 ** m)
            min_result += str(1 * 10 ** m + 5)
            m = 0
        else: 
            max_result += '5'
            min_result += '5'

    else:
        m += 1
if m > 0: 
    max_result += '1' * (m)
    min_result += str(1*10**(m-1))
print(max_result)
print(min_result)