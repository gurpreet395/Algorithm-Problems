class Heap:
	
	def __init__(self):
		self.heapsize=0
		self.currentheap=[0]

def insert(currentheap,i):
		print currentheap
		currentheap.append(i)
		length=len(currentheap)-1
		l=(len(currentheap))/2
		while length!=0 and currentheap[l]<currentheap[length]:
			
			temp=currentheap[length]
			currentheap[length]=currentheap[l]
			currentheap[l]=temp
			length=l
			l=(length)/2

		print currentheap


	
		length=len(currentheap)-1
		l=(len(currentheap))/2
		while length!=0 and currentheap[l]<currentheap[length]:
			
			temp=currentheap[length]
			currentheap[length]=currentheap[l]
			currentheap[l]=temp
			length=l
			l=(length)/2

def deleteMax(currentheap):
		swap(currentheap[1], currentheap[length-1])
		downheapify(currentheap[1])	
	
def buildHeap(arr):
		j=((len(arr))-1)//2
		while(j>=0):
			
			heapify(arr,j)
			j-=1
			
		return arr
def heapify(args,j):
		
		greatest=j
		if j*2+1<len(args) and args[j*2+1]> args[greatest]:
			greatest=j*2+1

		if j*2+2<len(args) and args[j*2+2]> args[greatest]:
			greatest=j*2+2
		
		if greatest!=j:
			temp=args[j]
			args[j]=args[greatest]
			args[greatest]=temp
			
			heapify(args,greatest)
		#return args
	
def getMinimum(currentheap):
		return currentheap[1]

h=Heap()
current=buildHeap([1,3,4,0,6,2,9,7,5])
#print current
insert(current,10)
insert(current,11)