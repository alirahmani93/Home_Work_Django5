from typing import Dict,List


class Graph:
    def __init__(self):
        self.adj_matrix: Dict["str", list] = {}

    def add_node(self, node_name: str) -> None:
        if node_name in self.adj_matrix:
            print(f"{node_name} exists")
        else:
            self.adj_matrix[node_name] = []

    def add_vertice(self, start: str, end: str) -> None:
        if start not in self.adj_matrix or end not in self.adj_matrix:
            print("yeki az nodeha da graph nist")
        else:
            if end not in self.adj_matrix[start]:
                self.adj_matrix[start].append(end)
            if start not in self.adj_matrix[end]:
                self.adj_matrix[end].append(start)

    def is_conected(self, start: str, end: str) -> bool:
        self.start  = start
        self.end    = end
        if (self.end in self.start) :
            return print(1)
        else: return print(0)

    # def short_path(self, start, end,path=[]) -> List:
    #     path = path + [start]
    #     if start == end:
    #         return path
    #     if not self.has_key(start):
    #         return None
    #     shortest = None
    #     for node in self[start]:
    #         if node not in path:
    #             newpath = short_path(graph, node, end, path)
    #             if newpath:
    #                 if not shortest or len(newpath) < len(shortest):
    #                     shortest = newpath
    #     return shortest
    #
    #
    # def all_path(self, start, end,path=[]):
    #     path = path + [start]
    #     if start == end:
    #         return [path]
    #     if not self.has_key(start):
    #         return []
    #     paths = []
    #     for node in self[start]:
    #         if node not in path:
    #             newpaths = all_path(self, node, end, path)
    #             for newpath in newpaths:
    #                 paths.append(newpath)
    #     return paths

    def __str__(self):
        return str(self.adj_matrix)

    def has_key(self, start):
        pass


g = Graph()
g.add_node("a")
g.add_node("b")
g.add_node("c")
g.add_node("d")
g.add_node("e")
g.add_node("f")

g.add_vertice("a", "b")
g.add_vertice("a", "e")
g.add_vertice("b", "c")
g.add_vertice("d", "f")
g.add_vertice("d", "e")

print("Graph Matrix is: ",g)
print("Is Connected? ", g.is_conected('a','b'))
print("Is Connected? ", g.is_conected('b','a'))
# g.all_path('a','b',['b'])
