def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    stack = graph[start] - visited
    print("start %s | visited %s | stack %s" % (start, visited, stack))
    for next in stack:
        dfs(graph, next, visited)
    return visited

graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3'])}

print(dfs(graph, '0'))