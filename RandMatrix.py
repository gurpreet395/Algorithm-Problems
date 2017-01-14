from random import randint
import numpy as np
	
def getInt():
	return randint(1,4)

def generateMatrix(n):
	a =np.array([n,n],np.double)
	temp=0
	count=0
	for r in xrange(0,n):
		for c in xrange(0,n):
			a[r][c]=getInt()
			if r<2 and c<2:
				continue
			elif r<2 and c>=2:
				if a[r][c-1]==a[r][c] and a[r][c-2]==a[r][c]:
					temp=getInt()
					while(temp==a[r][c]):
						temp=getInt()
					a[r][c]=temp
					continue
			elif r>=2 and c<2:
				if a[r-1][c]==a[r][c] and a[r-2][c]==a[r][c]:
					temp=getInt()
					while(temp==a[r][c]):
						temp=getInt()
					a[r][c]=temp
					continue

			elif r>=2 and c>=2:
				first_check=(a[r][c-1]==a[r][c] and  a[r][c-2]==a[r][c])
				second_check=( a[r-1][c]==a[r][c] and  a[r-2][c]==a[r][c])
				
				while  (first_check or second_check):

					#print "fist check",a[r][c-1],a[r][c-2],a[r][c]
					#print "second check",a[r-1][c],a[r-2][c],a[r][c]
					temp=getInt()
					while(temp==a[r][c]):
						temp=getInt()
						
					a[r][c]=temp
					first_check=(a[r][c-1]==a[r][c] and a[r][c-2]==a[r][c])
					second_check=(a[r-1][c]==a[r][c] and a[r-2][c]==a[r][c])
					count=count+1
				
					
					
						
	return a,count
	
for n in xrange(1,1000):
	
	print "---------------------------"
	a,b=generateMatrix(n)
	print b
	for r in xrange(0,n):
		for c in xrange(0,n):
			if r<2 and c<2:
				continue
			elif r<2 and c>=2:
				if a[r][c-1]==a[r][c] and a[r][c-2]==a[r][c]:
					print "bug found"
			elif r>=2 and c<2:
				if a[r-1][c]==a[r][c] and a[r-2][c]==a[r][c]:
					print "bug here"
			elif r>=2 and c>=2:
				first_check=(a[r][c-1]==a[r][c]and a[r][c-2]==a[r][c])
				second_check=(a[r-1][c]==a[r][c] and a[r-2][c]==a[r][c])
				if first_check or second_check:
					print "bug lolo"
			
		