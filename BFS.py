from collections import deque
graph = {'A': [ 'C','G'],
             'B': ['D'],
             'C': ['G'],
             'D': ['C','F'],
             'F': ['G'],
	     }
q=deque()
visited={}

def checkNode(node,end):
	if node==end:
		return True
	else:
		return False

def BFS(start,end,graph):
	
		visited[start]=True
		if start==end:
			return True
		path=False
		q.append(start)
		
		while(len(q)>0 and not path):
			node=q.popleft()
			path=checkNode(node,end)
			
			if(path):
				print "path found"
				return True
			if node in graph:

				for i in graph[node]:
					if i not in visited:
						print i
						visited[i]=True
						print visited
						q.append(i)
			
		if(not path):
			print "no path found"
	
p=BFS('A','D',graph)
		
	