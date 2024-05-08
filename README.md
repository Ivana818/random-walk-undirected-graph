# Random Walk Simulation on Undirected Graph - L1 Distance between Normalized Degree Vector and Empirical Frequency Vector
This is to simulate a random walk on an undirected graph and calculate the ℓ1-distance between normalized degree vector and empirical frequency vector during the random walk.
### Parameters
- **graph** : networkx.classes.graph.Graph   
&emsp;&emsp;&emsp;An undirected nxGraph with at least one edge for all node
- **steps** : integer    
&emsp;&emsp;&emsp;Number of steps to walk in random walk stimulation

### Returns
- **distance** : float    
&emsp;&emsp;&emsp;ℓ1-distance between normalized degree vector and empirical frequency vector


### Preprocessing Examples
If the undirected graph is not nxGraph, we have to convert it to a nxGraph before apply **random_walk**  
If it is presented in a dictionary
```
>>> print(undirected_graph)
{0:[1, 2, 4], 1:[2, 3], 2:[3], 3:[4], 4:[5, 6]}
```
We can convert it to nxGraph as follows
```
graph = nx.Graph()
number_of_edges = sum([len(undirected_graph[i]) for i in undirected_graph if isinstance(undirected_graph[i], list)])
for i in undirected_graph:
    for j in range(len(undirected_graph[i])):
        graph.add_edge(i,undirected_graph[i][j])
```