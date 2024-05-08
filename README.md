# Random Walk Stimulation on Undirected Graph - L1 Distance between Normalized Degree Vector and Empirical Frequency Vector
This is to stimulate a random walk on an undirected grapph and calculate the ℓ1-distance between normalized degree vector and empirical frequency vector during the random walk.
### Parameters
- **graph** : networkx.classes.graph.Graph   
&emsp;&emsp;&emsp;An undirected nxGraph with at least one edge for all node
- **steps** : integer    
&emsp;&emsp;&emsp;Number of steps to walk in random walk stimulation

### Returns
- **distance** : float    
&emsp;&emsp;&emsp;ℓ1-distance between normalized degree vector and empirical frequency vector


### Preprocessing Examples
We have to convert the undirected graph to a nxGraph before apply **random_walk**  
If the undirected graph is presented in a dictionary
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