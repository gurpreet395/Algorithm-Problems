

def LCS(str1,str2):
	
	# initialize the array

	T=[[0 for j in range(0,len(str2)+1)] for k in range(len(str1)+1)]
	len_str1=len(str1)
	len_str2=len(str2)

	for i in xrange(len_str1+1):
		for j in xrange(len_str2+1):
			if i == 0 or j == 0 :
                		T[i][j] = 0
			# If the elements of two strings match, New longest seq=previous+1

			elif(str2[j-1]==str1[i-1]):

				T[i][j]=T[i-1][j-1]+1
				print "Table value is ", T[i][j]
				print "matched", str2[j-1], str1[i-1] 
			else:
				# If they dont match, take into account maximum length of previous found LCS 
				T[i][j]=max (T[i][j-1],T[i-1][j])
	
	## The last element in the Table will give the length of longest sequence seen
	
	print T[len_str1][len_str2]
	

LCS("abdabgabcdfegabcabcd","abcabcdfgab")
#LCS("helloooooo","hell")
	