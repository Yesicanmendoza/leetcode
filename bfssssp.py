from collections import deque

def bfs(dic, start, end):
    queue = deque()
    queue.append([start])
    while queue:
        path = queue.popleft()
        print('p', path)
        node = path[-1]
        if node == end:
            return path
            
        for n in dic.get(node, []):
            print('n', n)
            npath = list(path)
            print('np', npath)
            npath.append(n)
            queue.append(npath)
            print('q', queue)
        print()
        

dic = ({"a": ["b", "c"],
        "b": ["d", "g"],
        "c": ["d", "e"],
        "d": ["f"],
        "e": ["f"],
        "g": ["f"]
        })

        
print(bfs(dic,"a", "e"))