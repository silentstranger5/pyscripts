from collections import deque
from itertools import chain


graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}


def find_path(graph, start, end, path=[]):
    path = path + list(start)
    if start == end:
        return path
    if not start in graph:
        return None
    for node in graph[start]:
        if node not in path:
            if (newpath := find_path(graph, node, end, path)):
                return newpath
    return None


def find_all_paths(graph, start, end, path=[]): 
    path = path + [start] 
    if start == end: 
        return [path] 
    if not start in graph: 
        return [] 
    paths = [] 
    for node in graph[start]: 
        if node not in path: 
            newpaths = find_all_paths(graph, node, end, path) 
            for newpath in newpaths: 
                paths.append(newpath) 
    return paths 


def find_shortest_path(graph, start, end):
    dist = {start: [start]}
    q = deque(start)
    while len(q):
        at = q.popleft()
        for next in graph[at]:
            if next not in dist:
                dist[next] = dist[at] + [next]
                q.append(next)
    return list(chain.from_iterable(dist.get(end)))


print(find_path(graph, 'A', 'D'))
print(find_all_paths(graph, 'A', 'D'))
print(find_shortest_path(graph, 'A', 'D'))
