# bingo online lottery game

n=[7,9,-3,8,6,-7,8,10]
n.sort()
p1=n[-1]*n[-2]
p2=n[0]*n[1]
if p1>p2:
    print(n[-1]+n[-2])
else:
    print(n[0]+n[1])


# digital secure data transfer solutions

char="d"
k=3
lower='abcdefghijklmnopqrstuvwxyz'
upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
if char in lower:
    idx=lower.index(char)
    out=lower[(idx+k)%26]
elif char in upper:
    idx=upper.n(char)
    out=upper[(idx+k)%26]
else:
    out=char
print(out)


# pooled cab service:

a,b=30,50
l=[29,38,12,48,39,55]
for i in l:
    if a<=i and b>=i:
        print(i,end=" ")


# kth shortest processing queue

n=[9,-3,8,-6,-7,18,10]
n.sort()
pos=n[5]
print(pos)


# converting graph input into adjacency list

from collections import defaultdict
edges=[['A','B'],['B','D'],['A','C'],['C','E'],['E','F']]
adj_list=defaultdict(list)
for u,v in edges:
    adj_list[u].append(v)
    adj_list[v].append(v)
print(adj_list)


# bfs traversal

def bfs(graph,start):
    visited=set()
    q=[start]
    while q:
        n=q.pop(0)
        if n not in visited:
            print(n,end=" ")
            visited.add(n)
            q.extend(graph[n])
graph={'a':['b'],
       'b':['d','e'],
       'c':['a'],
       'd':['c','g'],
       'e':['f'],
       'f':['d'],
       'g':[]}
print(bfs(graph,'a'))


# dfs traversal

def dfs(graph,start,v=set()):
    if start not in v:
        print(start,end=" ")
        v.add(start)
        for i in graph[start]:
            dfs(graph,i,v) 
graph={'a':['b'],
'b':['d','e'],
'c':['a'],
'd':['c','g'],
'e':['f'],
'f':['d'],
'g':[]
}
print(dfs(graph,'a'))




