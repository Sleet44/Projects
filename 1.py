import networkx as nx
import collections


def transformWord(graph, start, goal):
    paths=collections.deque([ [start] ])
    extended=set()
    while len(paths)!=0:
        currentPath=paths.popleft()
        currentWord=currentPath[-1]
        if currentWord==goal:
            return currentPath
        elif currentWord in extended:
            continue
        extended.add(currentWord)
        transforms=graph[currentWord]
        for word in transforms:
            if word not in currentPath:
                #avoid loops
                paths.append(currentPath[:]+[word])
    #no transformation
    return []

G=nx.read_gpickle('test.gpickle')
print(transformWord(G,'time','space'))
