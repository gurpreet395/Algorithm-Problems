import time
start_time= time.time()
# Merge two sorted arrays
def merge(arr1,arr2):
	length=len(arr1)


	if length==0:
		return "Arguments with empty arrays"
	i=0
	j=0
	mergedlist=[]
	mergedlength=0
	while i<length:
		while j<length:
			if arr1[i]<arr2[j]:
				mergedlist.append(arr1[i])
				mergedlength+=1
				i+=1
				break
			else:
				mergedlist.append(arr2[j])
				mergedlength+=1
				j+=1
				break
		if mergedlength>length:
			break
	median=(mergedlist[mergedlength-1]+mergedlist[mergedlength-2])/2
	return median

arr1=[1,12,15,26,38,50,51,52,53,54,55,56,67,76,87,98,100,122,123,124,125,126,127]
arr2=[2,13,17,30,45,46,47,48,78,89,90,122,123,144,145,146,167,178,189,190,290,280	]

print merge(arr1,arr2)
print("--- %s seconds ---" % (time.time() - start_time))

def medianinlog(arr1,arr2):
	length=len(arr1)
		
	if length==0:
		return "Arguments with empty arrays"

	if length==2:
		#print max(arr1[0],arr2[0]), min(arr1[1],arr2[1])
		return (max(arr1[0],arr2[0])+min(arr1[1],arr2[1]))/2

	mid=length/2
	
	if mid==0:
		median1=(arr1[mid-1]+arr1[mid])/2
		median2=(arr2[mid-1]+arr2[mid])/2
	else:
		median1=(arr1[mid])
		median2=(arr2[mid])
	
	
	if median1==median2:
		return median1
		
	if median1<median2:
		return medianinlog(arr1[mid:],arr2[:mid+1])
		
	elif median1>median2:
		return medianinlog(arr1[:mid+1],arr2[mid:])

			
		

arr1=[1,12,15,26,38]
arr2=[2,13,17,30,45]

print medianinlog(arr1,arr2)


# find median in  log(n)



				