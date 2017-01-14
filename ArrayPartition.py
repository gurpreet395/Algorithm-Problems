
def swap(arr,a,b):
	
	temp=arr[a]
	arr[a]=arr[b]
	arr[b]=temp
	
def partition(arr):

	pivot=0
	left=1
	right=len(arr)-1
	
	while left>=right:

		if arr[left]>arr[pivot]:
			swap(arr,left,right)
			left+=1
			continue
		elif arr[right]<arr[pivot]:
			swap(arr,left,right)
			right-=1
			
			continue
	print "shuffling"
	swap(arr,left,pivot)
	
	return arr

print partition([4,3,7,1,9,8,2])
		