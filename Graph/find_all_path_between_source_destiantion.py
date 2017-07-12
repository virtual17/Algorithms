# Python program to print all paths from a source to destination.

from collections import defaultdict
import copy  

final_path=[] 

fl=0
def lists_overlap(a, b):
    for i in a:
        if i in b:
            return True
    return False

class Graph:
  
    def __init__(self,vertices):
        self.V= vertices 
         
        self.graph = defaultdict(list) 
  
    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
  

    def printAllPathsUtil(self, u, d, visited, path):
 
        visited[u]= True
        path.append(u)
 
        if u ==d:
            #print(path)
            final_path.append(path[:])
        else:
            for i in self.graph[u]:
                if visited[i]==False:
                    self.printAllPathsUtil(i, d, visited, path)
                     
        path.pop()
        #visited[u]= False
  
  
    def printAllPaths(self,s, d): 
        visited =[False]*(self.V)
        path = []
 
        self.printAllPathsUtil(s, d,visited, path)
  
 



