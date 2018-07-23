def maxFunc(num):
    max = 0
    for i in num:
        if max<i:
            max=i
    return max

A = [1, 2, 3, 4, 5, 6, 73, 8, 10, 54]
maxNum = maxFunc(A)
print(maxNum)