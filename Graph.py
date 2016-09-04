class Graph(object):
    def __init__(self, graph={}):
        self.__graph = graph

    def get_vertices(self):
        vertices = [k for k in self.__graph.keys()]
        return vertices

    def add_vertex(self, v):
        if v not in self.__graph:
            self.__graph[v] = []
        else:
            raise KeyError('Specified vertex already exists in graph')

    def add_edge(self, v1, v2):
        if v2 not in self.__graph[v1]:
            self.__graph[v1].append(v2)
            self.__graph[v2].append(v1)
        else:
            raise ValueError('Edge already exists between specified vertices')

    def show_connections(self, v):
        if v in self.__graph:
            return self.__graph[v]
        else:
            raise KeyError('The specified node does not exist in this graph')
            return None

    def get_path(self, start, finish, path=[]):
        path = path + [start]
        graph = self.__graph
        if start == finish:
            return path
        if start not in graph:
            return None
        for vertex in graph[start]:
            if vertex not in path:
                new_path = self.get_path(vertex, finish, path)
                if new_path: return new_path
        return None

    def dfs(self, root):
        visited = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.append(node)
                stack.extend([x for x in self.__graph[node] if x not in visited])
        return visited

    def bfs(self, root):
        visited = []
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.append(node)
                queue.extend([x for x in self.__graph[node] if x not in visited])
        return visited


graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}
g = Graph(graph)

print g.get_path('A', 'E')
print g.dfs('A')
print g.bfs('A')
