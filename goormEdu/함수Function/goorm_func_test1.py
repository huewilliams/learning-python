sum = 0

def my_func(*num):
	for i in num:
		global sum
		sum = sum + i
my_func(1,2,3,4,5)
print(sum)