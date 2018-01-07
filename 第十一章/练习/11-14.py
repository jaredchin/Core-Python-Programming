def fbnq(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fbnq(n-1) + fbnq(n-2)

print(fbnq(6))