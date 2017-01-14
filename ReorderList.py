from llist import sllist

list1=sllist([1,2,3,4])
list2=sllist([1,12,9,4])
sum


list3=sllist()
carry=0

def getMidandEnd(list):
	slowpointer=list1.first
	fastpointer=slowpointer.next
	while True:
	
		#print "slowpointer is",slowpointer
		#print "fastpointer is",fastpointer
		if fastpointer.next is not None:
			slowpointer= slowpointer.next

			fastpointer=fastpointer.next.next
		else:
			return slowpointer, fastpointer

def reverseList(list, mid):
	print "processing"
	start=None
	a=list.first
	b=a.next
	current=list.first
	while current is not mid:
	
		next=current.next
		current.next=start
		start=current
		current=next
	
	
	print list
			
mid, end = getMidandEnd(list1)
reverseList(list1,mid)



	
	
	