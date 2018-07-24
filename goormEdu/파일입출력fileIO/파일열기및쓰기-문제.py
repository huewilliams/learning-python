my_list = [1,7,3,6]
my_list = sorted(my_list)
F = open("data/out.txt",'w')
for i in my_list:
	F.write(str(i))
F.close()