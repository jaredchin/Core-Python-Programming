N = int(input('Input a num: '))

def fbnq(N):
    num = [1, 1, 2]
    if N == 1:
        return
    for i in range(3, N):
        num.append(num[i-2] + num[i-1])
    return num[N-1]

print(fbnq(N))
