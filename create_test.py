import random

x = raw_input("please input a number \n")
y = raw_input("please input another number \n")
f = open("input.txt","w")
f.write(x+",\n")
f.write(y+",\n")
for i in range(0,int(x)):
	for j in range(0,int(y)):
		f.write(str(random.randint(-50,100)))
		if j< (int(y)-1) :f.write(",")
	f.write("\n")
f.close()
