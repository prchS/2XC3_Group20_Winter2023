from collections import deque
import random
import matplotlib.pyplot as plot
import timeit

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
    def get_size(self):
        return len(self.adj)
    


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
def find_highest_degree_vertex(adj_list):
    max_degree = -1
    max_vertex = -1
    
    for vertex, neighbors in adj_list.items():
        degree = len(neighbors)
        if degree > max_degree:
            max_degree = degree
            max_vertex = vertex
    
    return max_vertex
def remove_incident_edges(adj_list, node):
    # remove all edges incident to the given node
    for neighbor in adj_list[node]:
        adj_list[neighbor].remove(node)
    adj_list[node] = []
def print_graph(g):
 
    for v in g.adj:
        print(v, end=" -> ")
        for u in g.adj[v]:
            print(u, end=" ")
        print()

########################################################################################################################################
                                                      #  PART 2

def approx1(G):
    cover=[]
    edges ={}
    for node in G.adj.keys():
        edges[node] = G.adj[node].copy()
    while not is_vertex_cover(G,cover):
        node = find_highest_degree_vertex(edges)
        cover.append(node)
        remove_incident_edges(edges, node)
    return cover
def find_highest_degree_vertex(adj_list):
    max_degree = -1
    max_vertex = -1
    
    for vertex, neighbors in adj_list.items():
        degree = len(neighbors)
        if degree > max_degree:
            max_degree = degree
            max_vertex = vertex
    
    return max_vertex
def remove_incident_edges(adj_list, node):
    # remove all edges incident to the given node
    for neighbor in adj_list[node]:
        adj_list[neighbor].remove(node)
    adj_list[node] = []
############################################################################################################################################
                                                    #APPROX2(G)



def random_vertex(adj_list):
    return random.choice(list(adj_list.keys()))
def approx2(G):
    cover=[]
    edges={}
    for node in G.adj.keys():
        edges[node] = G.adj[node].copy()
    while not is_vertex_cover(G,cover):
        node = random_vertex(edges)
        cover.append(node)
    return list(set(cover))




############################################################################################################################################
                                                        #Approx3(G)
def approx3(G):
    cover=[]
    local={}
    a=()
    for node in G.adj.keys():
        local[node] = G.adj[node].copy()
    while not is_vertex_cover(G,cover):
        
        u,v = select_random_edge(local)
        
        cover.append(u) 
        
        cover.append(v) 
        
        if local[u] == []  and local[v]==[]:
            continue
        elif local[u] != [] :
            remove_incident_edges(local,u)
        elif local[v]!= [] :
            remove_incident_edges(local,v)
        else :
            continue

    return list(set(cover))    



def select_random_edge(adj_list):
    # Get all nodes that have adjacent edges
    nodes_with_edges = [node for node in adj_list if adj_list[node]]
    if not nodes_with_edges:
        return None  # No edges available
    
    # Randomly select a node with edges
    node = random.choice(nodes_with_edges)
    # Randomly select an edge from the node's adjacent edges
    neighbor = random.choice(adj_list[node])
    
    return (node, neighbor)


############################################################################################################################################

                                                        #EXPERIMENT
def random_graph(n, m):
    
    graph = Graph(n)
    edges = [(i, j) for i in range(n) for j in range(i+1, n)]
    random.shuffle(edges)
    edges_n = 0
    for edge in edges:
        if edges_n == m:
            break
        if edge[0] == edge[1]:
            continue
        graph.add_edge(edge[0], edge[1])
        edges_n += 1

    return graph

def Exp1(runs) :
    sumMVC=0
    sumapp1=0
    sumapp2=0
    sumapp3=0
    appr1 = []
    appr2 = []
    appr3 = []
    m=0
    edges=[]
    for i in range(runs):
        percent= (i/1000) * 100
        print("The percent is  :"  , percent)
        edges.append(m)

        if( i%33==0 and m<=30):
            m=m+1
        
        g1 = random_graph(8,m)
        a = MVC(g1)
        sumMVC += len(a)
        b= approx1(g1)
        sumapp1 += len(b)
        appr1.append(sumapp1/sumMVC)
        c = approx2(g1)
        sumapp2 += len(c)
        appr2.append(sumapp2/sumMVC)
        d= approx3(g1)
        sumapp3 += len(d)
        appr3.append(sumapp3/sumMVC)
    ax = plot.gca()
    ax.set_xlim([0,30])
    # ax.set_ylim([0,0.0025])
    plot.plot(edges,appr1, label="Approx 1") 
    plot.plot(edges,appr2 , label = "Approx 2") 
    plot.plot(edges, appr3, label = " Approx 3 ")
    plot.legend(loc="upper left")
    plot.xlabel("Number of edges")
    plot.ylabel("Expected performance ")
    plot.title("Part 2  - Experiment 1 ")
    plot.show()
def Exp2(number_of_nodes) :
    runs=2000
    sumMVC=0
    sumapp1=0
    sumapp2=0
    sumapp3=0
    appr1 = []
    appr2 = []
    appr3 = []
    m=1
    m_max= (number_of_nodes*(number_of_nodes-1))/2
    temp = runs/m_max
    edges=[]
    for i in range(runs):
        percent= (i/runs) * 100
        print("The percent is  :"  , percent)
        edges.append(m)

        if( i%int(temp))==0 and m<=m_max :
            m=m+1
        
        g1 = random_graph(10,m)
        a = MVC(g1)
        sumMVC += len(a)
        b= approx1(g1)
        sumapp1 += len(b)
        appr1.append(sumapp1/sumMVC)
        c = approx2(g1)
        sumapp2 += len(c)
        appr2.append(sumapp2/sumMVC)
        d= approx3(g1)
        sumapp3 += len(d)
        appr3.append(sumapp3/sumMVC)
    ax = plot.gca()
    ax.set_xlim([0,m_max])
    # ax.set_ylim([0,0.0025])
    plot.plot(edges,appr1, label="Approx 1") 
    plot.plot(edges,appr2 , label = "Approx 2") 
    plot.plot(edges, appr3, label = " Approx 3 ")
    plot.legend(loc="upper left")
    plot.xlabel("Number of edges")
    plot.ylabel("Expected performance ")
    plot.title("Part 2  - Experiment 2 ")
    plot.show()
def Exp3(number_of_nodes) :
    runs=2000
    sumMVC=0
    sumapp1=0
    sumapp2=0
    sumapp3=0
    appr1 = []
    appr2 = []
    appr3 = []
    m_max= (number_of_nodes*(number_of_nodes-1))/2
    m=20
    node_count=1
    temp= runs/number_of_nodes
    nodes=[]
    for i in range(runs):
        percent= (i/runs) * 100
        print("The percent is  :"  , percent)
        nodes.append(node_count)

        if( i%int(temp))==0 :
            node_count+=1
        
        g1 = random_graph(node_count,m)
        a = MVC(g1)
        sumMVC += len(a)
        b= approx1(g1)
        sumapp1 += len(b)
        appr1.append(sumapp1/sumMVC)
        c = approx2(g1)
        sumapp2 += len(c)
        appr2.append(sumapp2/sumMVC)
        d= approx3(g1)
        sumapp3 += len(d)
        appr3.append(sumapp3/sumMVC)
        
    
    ax = plot.gca()
    ax.set_xlim([0,number_of_nodes])
    ax.set_ylim([0,10])
    plot.plot(nodes,appr1, label="Approx 1") 
    plot.plot(nodes,appr2 , label = "Approx 2") 
    plot.plot(nodes, appr3, label = " Approx 3 ")
    plot.legend(loc="upper left")
    plot.xlabel("Number of nodes")
    plot.ylabel("Expected performance ")
    plot.title("Part 2  - Experiment 3 ")
    plot.show()

def Exp4():
    runs=1000
    nodes=5
    edges=1
    edge=[]
    time=[]
    total=0
    for i in range(runs):
        percent= (i/runs) * 100
        print("The percent is  :"  , percent)
        edge.append(edges)
        if(i%int(runs/edges))==0 : 
            edges+=1
        g1=random_graph(nodes,10)
        start=timeit.default_timer()
        approx1(g1)
        end=timeit.default_timer()
        total+=((end-start)*100)
        time.append(total)
        ax = plot.gca()
    ax.set_xlim([0,10])
    plot.plot(edge,time,label="Approx 1") 
    plot.legend(loc="upper left")
    plot.xlabel("Number of edges")
    plot.ylabel("runtime")
    plot.title("Part 2  - Experiment 4")
    plot.show()










