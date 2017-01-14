list=[10,22,9,33,50,60, 6, 7, 0, 5, 7, 9, 80 ]

greatest=list[0]
count=1
i=1
m=0
num=[]
previous=[]
while(i<len(list)):
	
	if(list[i-1]-list[i]<0):
	
		count=count+1
		#print list[i-1],list[i]
		if(list[i-1] not in num):
			num.append(list[i-1])
		num.append(list[i])
		i=i+1		
		#print num
	else:
		print previous
		
		
		count=1
		i=i+1
	if(len(previous)<len(num)):
			previous=num
			num=[]
			m=max(count,m)
print previous
print m
		
	