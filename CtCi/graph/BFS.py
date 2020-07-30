graph = {"a": ["c"],
         "b": ["c", "e"],
         "c": ["a", "b", "d", "e"],
         "d": ["c"],
         "e": ["c", "b"],
         "f": []
         }


def bfs(visited, graph, node):
    visited.append(node)
    queue = []

    queue.append(node)
    while queue:
        s = queue.pop(0)
        print(s, end="")

        for neighbor in graph[s]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

    return visited


print(bfs([], graph, 'a'))
