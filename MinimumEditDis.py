

def MinimumEditDistance(str1,str2):

	len_str1=len(str1)
	len_str2=len(str2)
	T=[[ 0 for i in xrange(0,len_str2+1)] for j in xrange(0,len_str1+1)]
	
	for i in xrange(0, len_str1+1):
		for j in xrange(0,len_str2+1):
			if i==0:
				T[i][j]=j
				
			elif j==0:
				T[i][j]=i
				
			elif  str1[i-1]==str2[j-1]:
				T[i][j]=T[i-1][j-1]
			
			else:
				T[i][j]=min(T[i][j-1],T[i-1][j],T[i-1][j-1])+1
			
	print "min edit distance", T[len_str1][len_str2]

MinimumEditDistance("abcdkjkj","abee")