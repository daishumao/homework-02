# coding:utf-8
'''
2013-9-17  XTH
'''
import sys


def setglobalvar():
	global max_sum,now_sum,min_x,min_y,num,visited,pointgroup
	max_sum = 0
	now_sum = 0
	min_x = 0
	min_y = 0
	num = []
	visited = {}
	pointgroup = []


def maxsum_h(num,n1,n2):
	line = [0]*n2
	max_sum = 0     #最大和
	now_sum = 0     #当前和
	for l in range (0,n2):
		for i in range(0,n1):
			for j in range(i,n1):
				for k in range(0+l,n2+l):
					k = k % n2
					line[k] += num[j][k]
					if now_sum <0:
						now_sum = 0
					now_sum += line[k]
					if now_sum > max_sum:
						max_sum = now_sum
				now_sum = 0
			now_sum=0
			line = [0]*n2
	return max_sum

def maxsum_v(num,n1,n2):    #水平上相连
	line = [0]*n2
	max_sum = 0     #最大和
	now_sum = 0     #当前和
	for l in range (0,n1):
		for i in range(0,n1):
			for j in range(i+l,n1+l):
				for k in range(0,n2):
					j = j % n1
					line[k] += num[j][k]
					if now_sum <0:
						now_sum = 0
					now_sum += line[k]
					if now_sum > max_sum:
						max_sum = now_sum
				now_sum = 0
			now_sum=0
			line = [0]*n2
	return max_sum


def maxsum(num,n1,n2):
	line = [0]*n2
	max_sum = 0     #最大和
	now_sum = 0     #当前和
	for i in range(0,n1):
		for j in range(i,n1):
			for k in range(0,n2):
				line[k] += num[j][k]
				if now_sum <0:
					now_sum = 0
				now_sum += line[k]
				if now_sum > max_sum:
					max_sum = now_sum
			now_sum = 0
		now_sum=0
		line = [0]*n2
	return max_sum


def maxsum_vh(num,n1,n2):
	line = [0]*n2
	max_sum = 0     #最大和
	now_sum = 0     #当前和
	for l1 in range (0,n1):
		for l2 in range (0,n2):
			for i in range(0,n1):
				for j in range(i+l1,n1+l1):
					for k in range(0+l2,n2+l2):
						j = j % n1
						k = k % n2
						line[k] += num[j][k]
						if now_sum <0:
							now_sum = 0
						now_sum += line[k]
						if now_sum > max_sum:
							max_sum = now_sum
					now_sum = 0
				now_sum=0
				line = [0]*n2
	return max_sum

def searchthrough(x,y,num,now_sum):
	global max_sum,pointgroup,min_x,min_y,visited
	max_sum = max(max_sum, now_sum)
	for i in [[0,-1],[1,0],[0,1],[-1,0]]:
		if x+i[0]>=min_x and x+i[0]<n1 and y+i[1]>=min_y and y+i[1]<n2 and visited[(x+i[0])%n1,(y+i[1])%n2]==0 and [(x+i[0])%n1,(y+i[1])%n2,num[(x+i[0])% n1][(y+i[1])%n2]] not in pointgroup:
			pointgroup.append([(x + i[0]) % n1, (y + i[1]) % n2, num[(x + i[0]) % n1][(y + i[1]) % n2]])
	if pointgroup == []:
		return
	pointgroup = sorted(pointgroup, key=lambda x: x[2])
	nextpoint = pointgroup.pop()
	if now_sum + nextpoint[2] > 0: 
		visited[nextpoint[0], nextpoint[1]] = 1
		searchthrough(nextpoint[0],nextpoint[1],num,now_sum + nextpoint[2])
		visited[nextpoint[0], nextpoint[1]] = 0
	else:
		return

def maxsum_a(num,n1,n2):    #水平上相连
	global min_x,min_y,max_sum,visited
	min_x = 0
	min_y = 0
	max_sum = 0
	now_sum = 0
	startpointx = []
	startpointy = []
	pointgroup = [] 
	for i in range(0,n1):
		for j in range(0,n2):
			visited[i,j] = 0
	for i in range(0,n1):
		for j in range(0,n2):
			if num[i][j] > 0:
				startpointx.append(i)
				startpointy.append(j)
	for pointx in startpointx:
		pointy = startpointy.pop()
		visited[pointx, pointy] = 1
		searchthrough(pointx,pointy,num,num[pointx][pointy])
	return max_sum

def maxsum_vha(num,n1,n2):    #水平上相连
	global min_x,min_y,max_sum,visited
	min_x = -n1
	min_y = -n2
	max_sum = 0
	now_sum = 0
	startpointx = []
	startpointy = []
	pointgroup = [] 
	for i in range(0,n1):
		for j in range(0,n2):
			visited[i,j] = 0
	for i in range(0,n1):
		for j in range(0,n2):
			if num[i][j] > 0:
				startpointx.append(i)
				startpointy.append(j)
	for pointx in startpointx:
		pointy = startpointy.pop()
		visited[pointx, pointy] = 1
		searchthrough(pointx,pointy,num,num[pointx][pointy])
	return max_sum

def main():
	setglobalvar()
	global n1,n2
	max_sum = 0
	V = H = A = False
	if "\\v" in sys.argv[1:]:
		V = True;
	if "\\h" in sys.argv[1:]:
		H = True;
	if "\\a" in sys.argv[1:]:
		A = True;
	filename = sys.argv[-1];	
	try:
		f = open(filename,"r")
	except:
		raise IOError("ERROR:can't open the file")
	try: 
		line = f.readline()
		line = line.strip('\n').strip(',')
		n1 = int(line)
		line = f.readline()
		line = line.strip('\n').strip(',')
		n2 = int(line)
		num=[[]]*int(n1)
		for i in range(0,int(n1)):
			line = f.readline()
			line = line.strip('\n')
			if len(line.split(",")) != n2:
				raise ValueError("ERROR:the format of file is wrong")	
			num[i] = line.split(",")
		num=[[int(x) for x in inner] for inner in num]
	except:
		raise ValueError("ERROR:the format of file is wrong")	
	if V!=True and H!=True and A == True:#连通
		max_sum = maxsum_a(num,n1,n2);
	elif V==True and H!=True and A != True:#水平上相连
		max_sum = maxsum_v(num,n1,n2);
	elif V!=True and H==True and A != True:#垂直上相连
		max_sum = maxsum_h(num,n1,n2);
	elif V==True and H==True and A != True:#水平垂直上相连
		max_sum = maxsum_vh(num,n1,n2);
	elif V==True and H==True and A == True:#水平垂直上相连连通
		max_sum = maxsum_vha(num,n1,n2);
	else:#普通
		max_sum = maxsum(num,n1,n2);
	return max_sum



if __name__ == '__main__':      
    print main()