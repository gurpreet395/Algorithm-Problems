
def matchpatternkey(string, pattern):
	map={}
	reversemap={}
	string=string.split()

	if len(string)!=len(pattern):
		return False

	for index in xrange(0,len(pattern)):
		try:
			if pattern[index] not in map.keys() and string[index] not in reversemap.keys():

				map[pattern[index]]=string[index] 
				reversemap[string[index]]=pattern[index]
	
			else:
				if map[pattern[index]]!=string[index] or \
				reversemap[string[index]]!=pattern[index]:
					return False
		except:
			return False
	return True

print matchpatternkey('',['a'])
#print matchpatternkey("dog dog cat bitch mehfil",['a','a','b','c','e'])

	

	