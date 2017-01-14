
def printhashMap(employeemap,record, key,space):
	
		
		if key not in record:
			if space==0:
				record[key]=0
			else:
				record[key]=record[space]+1
							
		else:
			record[key]+=1
		str=[' ' for space in xrange(0,record[key])]
		print ''.join(str),'-',key
		
		if key not in employeemap.keys():
			return
		
		for value in employeemap[key]:

			printhashMap(employeemap,record,value,key)

def printEmployee(employeemap, record):
	space=0
	start= employeemap.keys()[0]
	printhashMap(employeemap,record,start,space)	

record={}
employeemap={'AAA':['BBB','CCC','EEE'],'CCC':['DDD'],'DDD':['FFF']}
printEmployee(employeemap, record)
	



		