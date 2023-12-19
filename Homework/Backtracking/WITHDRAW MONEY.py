def backtrack(menh_gia, S, current, result):
    if S == 0:
        result.append(current[:])  
        return
    if S < 0 or len(menh_gia) == 0:
        return
    for i in range(len(menh_gia)):
        if menh_gia[i] <= S:
            current.append(menh_gia[i])
            backtrack(menh_gia[i:], S - menh_gia[i], current, result)
            current.pop()

def rut_tien(menh_gia, S):
    menh_gia.sort()  
    result = []
    current = []
    backtrack(menh_gia, S, current, result)
    return result

n, S = map(int, input().split())
menh_gia = list(map(int, input().split()))

result = rut_tien(menh_gia, S)
print(len(result))
for r in result:
    print(' '.join(map(str, r)))