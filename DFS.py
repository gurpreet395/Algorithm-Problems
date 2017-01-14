graph = {'A': [ 'C','G','B'],
             'B': ['D'],
             'C': ['G'],
             'D': ['C','F'],
             'F': ['G']}
path=[]
visited={}
def DFS(start,end,path):
	p=[1]
	if(start==end):
		print "got it"
		return True,list(path)+[start]
		
	if(start in graph and start not in visited):
		
		path.append(start)
		print path
		visited[start]=True
				
		for i in graph[start]:
			print "starting DFS on", i
			p=DFS(i,end,path)
			if p[0]==True:
				return p
			else:
				path=set(path)-set(graph[start])
				path=list(path)
				print "in for loop",set(graph[start])

		
		else:
			return False,1
		#if p==None:
		#	print "in none"
		#	path=set(path)-set([start])-set(graph[start])
		#	print path,graph[start]
	return False,1
			
	
	
	
p=DFS('B','F',path)
print "from here",p
		
	
	
	
		
		
		