from typing import Dict,List


class Graph:

    def __init__(self):
        self.adj_matrix: Dict["str", list] = dict()

    def add_node(self, node_name: str) -> None:
        if node_name in self.adj_matrix:
            print(f"{node_name} exists")
        else:
            self.adj_matrix[node_name] = []

    def add_vertice(self, node_a: str, node_b: str) -> None:
        if node_a not in self.adj_matrix or node_b not in self.adj_matrix:
            print("yeki az nodeha dar graph nist")
        else:
            if node_b not in self.adj_matrix[node_a]:
                self.adj_matrix[node_a].append(node_b)
            if node_a not in self.adj_matrix[node_b]:
                self.adj_matrix[node_b].append(node_a)
###___________________________________________________________________________###

    def is_conected(self, node_a: str,node_b: str) -> bool:
        self.node_a  = node_a
        self.node_b    = node_b
        if (self.node_b in self.adj_matrix[node_a]) :
            return True
        else:
            return False

    def short_path(self, node_a,node_b,path=[]) -> List:
        pass

    def all_path(self, node_a,node_b,path=[])-> List:
        path= path + [node_a]

        for node in self.adj_matrix[node_a]:
            if node not  in path:
                newpath = []
        pass
    def find_path(self, node_a, node_b, path=list()):           pass
        # path = path + [node_a]
        # if node_a == node_b:
        #     return path
        # if node_a not in self.adj_matrix[node_a]:
        #     return print("There is no cycle")
        # for node in self.adj_matrix[node_a]:
        #     if node not in path:
        #         new_path = find_path(self, node, node_b, path)
        #         if new_path: return new_path
        # return None

    def node_degree(self,node_a) -> int:
        count=0
        for i in self.adj_matrix[node_a]:
            count+=1
        return print("node_degree is: ",count)

    def is_cycle(self,node_a) -> bool:
        if node_a in self.adj_matrix[node_a]:
            return print('cycle? ',True)
        else:
            return print('cycle? ',False)

    def __str__(self):
        return str(self.adj_matrix)
"""
    ###### geek for geek ####
    def printAllPathsUtil(self, node_a, node_b, visited=[], path=[]):

        # Mark the current node as visited and store in path
        visited[node_a] = True
        path.append(node_a)

        # If current vertex is same as destination, then print
        # current path[]
        if node_a == node_b:
            print
            path
        else:
            # If current vertex is not destination
            # Recur for all the vertices adjacent to this vertex
            for i in self.graph[node_a]:
                if visited[i] == False:
                    self.printAllPathsUtil(i, node_b, visited, path)

        # Remove current vertex from path[] and mark it as unvisited
        path.pop()
        visited[node_a] = False

    # Prints all paths from 's' to 'd'
    # def printAllPaths(self, node_a, node_b):
    #     # Mark all the vertices as not visited
    #     visited = [False] * (self.node_b)
    #     # Create an array to store paths
    #     path = []
    #     # Call the recursive helper function to print all paths
    #     self.printAllPathsUtil(node_a, node_b, visited, path)
######          ######
"""
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
g.add_vertice("d", "d")     # Make cycle

print("Graph Matrix is: ",g)

print("Is Connected? ", g.is_conected('a','b'))
print("Is Connected? ", g.is_conected('b','d'))

print("All path between node_a and node_b is: \n",g.all_path('a','b'))

print(g.node_degree('a'))

print(g.is_cycle('d'))

print(g.find_path('a','a'))
# g.printAllPathsUtil('a', 'd')