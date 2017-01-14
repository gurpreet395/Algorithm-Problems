import math

def printspiral(matrix):
	size=len(matrix)
	print size
	if size%2==0:
		mid=size/2
	else:
		mid=int(math.ceil(size/2+1))
	print "mid is", mid
	size-=1
	
	n=size-1

	for layer in xrange(0,mid):
		print "running it"
		
		#print upper row of the matrix
		for uprow in xrange(layer,size-layer):
			print matrix[layer][uprow]

		# print right column
		for rightcol in xrange(layer, size-layer):
			print matrix[rightcol][size-layer]
	
		#print lower row
		for bottom in xrange(layer,size-layer):
			print matrix[size-layer][size-bottom]
		
		#print left column of matrix
		for left in xrange(layer,size-layer):
			print matrix[size-left][layer]
	



matrix=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
printspiral(matrix)