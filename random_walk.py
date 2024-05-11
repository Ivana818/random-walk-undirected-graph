import networkx as nx
import numpy as np
import random

def random_walk(graph, steps):
    # convert the nodes from nx NodeView to list
    nodes = list(graph.nodes)
    
    # we have to add an attribute to the node to store the visiting times of each node during random walk
    # add an attribute "visit" to every node and set the value as 0
    nx.set_node_attributes(graph, 0, "visit")
    
    # choose a starting node randomly
    node = random.randint(0, len(nodes) - 1)
    
    # add 1 to "visit" of the starting node
    graph.nodes[nodes[node]]["visit"] += 1
    
    for i in range(steps):
        # nodes that linking to the current node
        linked_nodes = list(graph[node])
        
        # choose the next visit node randomly
        next_node_index = random.randint(0, len(linked_nodes) - 1)
        next_node = linked_nodes[next_node_index]
        
        # set "next_node" as current node
        node = next_node
        
        # add 1 to "visit" of the current node
        graph.nodes[node]["visit"] += 1
    
    # L1 distance
    distance = 0
    
    # sum of degree of all nodes
    D = 2 * len(graph.edges)
    
    for i in range(len(nodes)):
        linked_nodes = list(graph[nodes[i]])
        visit_time = graph.nodes[nodes[i]]["visit"]
        
        # add the distance difference between normalized degree vector and empirical frequency vector 
        # normalized degree: number of linked nodes / sum of degree of all nodes
        # empirical frequency vector: number of visited time / number of random walk steps
        distance += np.abs(len(linked_nodes) / D - visit_time / steps)
        
    return distance