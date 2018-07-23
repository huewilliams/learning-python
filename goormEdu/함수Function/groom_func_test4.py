def oper(a,b):
    a = int(a)
    b = int(b)
    result=[a+b,a-b,a*b]
    return result
a = input()
b = input()
print(oper(a,b))