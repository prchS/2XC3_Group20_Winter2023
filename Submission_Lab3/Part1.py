from collections import deque
import random
import matplotlib.pyplot as plot

#Undirected graph using an adjacency list
class Graph:

    def __init__(self, n):
        self.adj = {}
        for i in range(n):
            self.adj[i] = []

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

def is_vertex_cover(G, C):
    for start in G.adj:
        for end in G.adj[start]:
            if not(start in C or end in C):
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


# ========================================================================
# ******************** Implementations of bfs and dfs ********************
# ========================================================================


# ************************* BFS2 *************************


def BFS2(G, node1, node2):
    Q = deque([node1])
    marked = {node1 : True}
    trace = {}

    for node in G.adj:
        if node != node1:
            marked[node] = False
    
    while len(Q) != 0:
        current_node = Q.popleft()
        if current_node == node2:
            break

        for node in G.adj[current_node]:
            if not marked[node]:
                Q.append(node)
                marked[node] = True
                trace[node] = current_node

    path = [node2]
    while path[-1] != node1:
        last = path[-1]
        next = trace[last]
        path.append(next)
    return path[::-1]


# ************************* DFS2 *************************


def DFS2(G, node1, node2):
    S = [node1]
    marked = {}
    trace = {}

    for node in G.adj:
        marked[node] = False
    marked[node1] = True

    while len(S) != 0:
        current_node = S.pop()
        if current_node == node2:
            break

        for node in G.adj[current_node]:
            if not marked[node]:
                S.append(node)
                marked[node] = True
                trace[node] = current_node

    path = [node2]
    while path[-1] != node1:
        last = path[-1]
        next = trace[last]
        path.append(next)
    return path[::-1]


# ************************* BFS3 *************************


def BFS3(G, node1):
    Q = deque([node1])
    marked = {node1 : True}
    trace = {}

    for node in G.adj:
        if node != node1:
            marked[node] = False
    
    while len(Q) != 0:
        current_node = Q.popleft()

        for node in G.adj[current_node]:
            if not marked[node]:
                Q.append(node)
                marked[node] = True
                trace[node] = current_node
    
    return trace


# ************************* DFS3 *************************


def DFS3(G, node1):
    S = [node1]
    marked = {}
    trace = {}

    for node in G.adj:
        marked[node] = False
    marked[node1] = True

    while len(S) != 0:
        current_node = S.pop()

        for node in G.adj[current_node]:
            if not marked[node]:
                S.append(node)
                marked[node] = True
                trace[node] = current_node

    return trace 


# ********************* Implementation of has_cycle **********************


def has_cycles_aux(G,node1, marked, prev):
    marked[node1] = True
    for node in G.adj[node1]:
        if node != node1:
            if not marked[node]:
                if has_cycles_aux(G, node, marked, node1):
                    return True
            elif prev != node:
                return True
    return False


def has_cycle(G):
    marked = {}

    for node in G.adj:
        marked[node] = False

    for node in G.adj:
        if not marked[node]:
            if has_cycles_aux(G, node, marked, -1) == True:
                return True
    return False


# ******************** Implementation of is_connected ********************


def is_connected(G):
    for node1 in G.adj:
        for node2 in G.adj:
            if not BFS(G,node1,node2):
                return False
    return True


# **************************** Experiment-1 ******************************


def create_random_graph(i,j):
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
    return G1


# i -> number of nodes, j -> number of edges, m -> number of graphs for each number of edges.
def test1(i,j,m):
    probabilities = []
    edges = []
    for e in range(j):
        counter = 0
        for n in range(m):
            G1 = create_random_graph(i,e)
            if has_cycle(G1) == True:
                counter = counter + 1
        probabilities.append(counter/m)
        edges.append(e)
        if (e*100/j) % 10 == 0:
            print(str(int(e*100/j)) + "%" + " completed")
    return probabilities,edges


# **************************** Experiment-2 ******************************


# i -> number of nodes, j -> number of edges, m -> number of graphs for each number of edges.
def test2(i,j,m):
    probabilities = []
    edges = []
    for e in range(j):
        counter = 0
        for n in range(m):
            G1 = create_random_graph(i,e)
            if is_connected(G1) == True:
                counter = counter + 1
        probabilities.append(counter/m)
        edges.append(e)
        if (e*100/j) % 10 == 0:
            print(str(int(e*100/j)) + "%" + " completed")
    return probabilities,edges


# ******************************* Tests **********************************


# tests for BFS/DFS, has_cycle and Is_connected 

'''
G1 = Graph(7)
G1.add_edge(1,2)
G1.add_edge(1,3)
G1.add_edge(2,4)
G1.add_edge(4,3)
G1.add_edge(6,4)
G1.add_edge(5,3)
G1.add_edge(4,5)

print(BFS2(G1,1,6))
print(DFS3(G1,1))
print(has_cycle(G1))
print(is_connected(G1))'''


# test for experiment 1

'''
result = test1(100,100,1_000)
plot.plot(result[1],result[0])
plot.xlabel("Number of edges")
plot.ylabel("cycle probability")
plot.title("Experiment-1")
plot.show()'''


# test for experiment 2

'''
result = test2(60,300,500)
plot.plot(result[1],result[0])
plot.xlabel("Number of edges")
plot.ylabel("cycle probability")
plot.title("Experiment-2")
plot.show()'''