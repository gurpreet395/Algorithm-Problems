from llist import sllist

list1=sllist([1,2,3,4])
list2=sllist([1,12,9,4])

next1=list1.first
next2=list2.first
list3=sllist()
carry=0
for next in list1:
	
	print next1
	sum= next1.value+next2.value
	if carry==1:
		sum+=1
		carry=0
	if sum > 10:
		sum=sum%10
		carry=1
	next1.value=sum
	list3.appendright(sum)
	
	next1=next1.next
	next2=next2.next
print list1
print list3
	
		
