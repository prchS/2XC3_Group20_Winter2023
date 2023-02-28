from collections import deque
import random
import matplotlib.pyplot as plot

#Undirected graph using an adjacency list
class Graph:
    def __init__(self, n):
        self.adj = {}
        self.n2 = n
        for i in range(n):
            self.adj[i] = []
    def get_size(self):
        return self.n2
    def are_connected(self, node1, node2):
        return node2 in self.adj[node1]

    def adjacent_nodes(self, node):
        return self.adj[node]

    def add_node(self):
        self.adj[len(self.adj)] = []

    def add_edge(self, node1, node2):
        if node1 not in self.adj[node2]:
            self.adj[node1].append(node2)
            self.adj[node2].append(node1)

    def number_of_nodes():
        return len()


#Breadth First Search
def BFS(G, node1, node2):
    Q = deque([node1])
    marked = {node1 : True}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if node == node2:
                return True
            if not marked[node]:
                Q.append(node)
                marked[node] = True
    return False


#Depth First Search
def DFS(G, node1, node2):
    S = [node1]
    marked = {}
    for node in G.adj:
        marked[node] = False
    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            for node in G.adj[current_node]:
                if node == node2:
                    return True
                S.append(node)
    return False

#Use the methods below to determine minimum vertex covers

def add_to_each(sets, element):
    copy = sets.copy()
    for set in copy:
        set.append(element)
    return copy

def power_set(set):
    if set == []:
        return [[]]
    return power_set(set[1:]) + add_to_each(power_set(set[1:]), set[0])

def is_vertex_cover(G, cover):
    for start in G.adj:
        for end in G.adj[start]:
            if not(start in cover) and not(end in cover):
                return False
    return True

def MVC(G):
    nodes = [i for i in range(G.get_size())]
    subsets = power_set(nodes)
    min_cover = nodes
    for subset in subsets:
        if is_vertex_cover(G, subset):
            if len(subset) < len(min_cover):
                min_cover = subset
    return min_cover

def contain_adjacent(G,cover):
    if (len(cover) == 0):
        return True
    for each in cover:
        for each2 in cover:
            if G.are_connected(each,each2):
                return False
    return True

def MIS(G):
    nodes = [i for i in range(G.get_size())]
    powerSet = power_set(nodes)
    MIS = set()
    if (G.get_size() == 0):
        return MIS
    for subset in powerSet:
        if contain_adjacent(G,subset):
            if len(subset) >= len(MIS):
                MIS = subset
    return MIS
def create_random_graph(i,j): # i is nodes, j is edges
    G1 = Graph(i)
    edges = []
    e = 0
    while e < j:
        node1 = random.randint(0,i-1)
        node2 = random.randint(0,i-1)
        if node1 != node2 and (node1,node2) not in edges and (node2,node1) not in edges:
            G1.add_edge(node1,node2)
            edges += [(node1,node2)]
            e = e + 1
        #print("running")
    return G1

def main():
    node = 12
    runs = 250
    edge = 0
    mvc = []
    mis = []
    edge_list = []
    for i in range(node):
        edge+= i   # assume we have 4 nodes, the max number of edges we could have is 3 * 2 * 1 = 6
    print(edge)
    for i in range (edge):
        mvc_run = 0
        mis_run = 0
        print("im here")
        for q in range(runs):
            G = create_random_graph(node,i)
            mvc_run += len(MVC(G))
            mis_run += len(MIS(G))
        mvc.append(mvc_run / runs)
        mis.append(mis_run/ runs)
    plot.plot(mvc)
    plot.plot(mis)
    plot.legend(['MVC','MIS'])
    plot.xlabel("Number of edges")
    plot.ylabel("Size")
    plot.show()


main()

