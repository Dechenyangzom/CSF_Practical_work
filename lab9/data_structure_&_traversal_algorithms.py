
# Step 1: Implement the Graph Class

from collections import deque
class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, vertex1, vertex2):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)  # For undirected graph
    
    def print_graph(self):
        for vertex in self.graph:
            print(f"{vertex}: {' '.join(map(str, self.graph[vertex]))}")



    def dfs(self, start_vertex):
            visited = set()
            self._dfs_recursive(start_vertex, visited)
        
    def _dfs_recursive(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=' ')
            
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self._dfs_recursive(neighbor, visited)


    def bfs(self, start_vertex):
        visited = set()
        queue = deque([start_vertex])
        visited.add(start_vertex)

        while queue:
            vertex = queue.popleft()
            print(vertex, end=' ')

            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    def find_all_paths(self, start_vertex, end_vertex, path=[]):
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in self.graph:
            return []
        paths = []
        for neighbor in self.graph[start_vertex]:
            if neighbor not in path:
                new_paths = self.find_all_paths(neighbor, end_vertex, path)
                for new_path in new_paths:
                    paths.append(new_path)
        return paths
    
    def is_connected(self):
        if not self.graph:
            return True
        start_vertex = next(iter(self.graph))
        visited = set()
        self._dfs_recursive(start_vertex, visited)
        return len(visited) == len(self.graph)
    
# Test the Graph class
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.print_graph()
# Test DFS
print("\nDFS starting from vertex 0:")
g.dfs(0)
# Test BFS
print("\nBFS starting from vertex 0:")
g.bfs(0)

# Test finding all paths
print("\nAll paths from vertex 0 to vertex 3:")
all_paths = g.find_all_paths(0, 3)
for path in all_paths:
    print(' -> '.join(map(str, path)))

# Test if the graph is connected
print("\nIs the graph connected?", g.is_connected())

# Add a disconnected vertex and test again
g.add_vertex(4)
print("After adding a disconnected vertex:")
print("Is the graph connected?", g.is_connected())



# Exercise 


# 1.to find the shortest path between two vertices using BFS.

from collections import deque

def bfs_shortest_path(graph, start, goal):
    queue = deque([(start, [start])])  
    visited = set()  

    while queue:
        current_vertex, path = queue.popleft()

        if current_vertex == goal:
            return path
        
        visited.add(current_vertex)

        for neighbor in graph[current_vertex]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    return None

# Example usage:
if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    start_vertex = 'A'
    goal_vertex = 'F'
    shortest_path = bfs_shortest_path(graph, start_vertex, goal_vertex)

    if shortest_path is not None:
        print("Shortest path from {} to {}: {}".format(start_vertex, goal_vertex, shortest_path))
    else:
        print("No path found from {} to {}".format(start_vertex, goal_vertex))



# 2.to detect cycles in the graph.
def has_cycle_graph(graph):
    visited = set()
    rec_stack = set()

    def dfs(vertex):
        if vertex in rec_stack:
            return True  # Cycle found
        if vertex in visited:
            return False  # Already visited, no cycle from this vertex

        visited.add(vertex)
        rec_stack.add(vertex)

        for neighbor in graph[vertex]:
            if dfs(neighbor):
                return True

        rec_stack.remove(vertex)  # Backtrack
        return False

    for v in graph:
        if v not in visited:
            if dfs(v):
                return True

    return False

# Example usage for graph
if __name__ == "__main__":
    cycle_graph = {
        'A': ['B'],
        'B': ['C'],
        'C': ['A'],  # Cycle here
        'D': ['E'],
        'E': []
    }

    print("Cycle detected in graph:", has_cycle_graph(cycle_graph))



# 3.Dijkstra's algorithm to find the shortest path in a weighted graph.
import heapq

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    priority_queue = [(0, start)]  # (distance, vertex)

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Example usage
if __name__ == "__main__":
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }

    start_vertex = 'A'
    shortest_paths = dijkstra(graph, start_vertex)

    print("Shortest paths from vertex {}: {}".format(start_vertex, shortest_paths))



# 4. to determine if the graph is bipartite.
from collections import deque

def is_bipartite(graph):
    color = {}
    
    # Function to perform BFS
    def bfs(start):
        queue = deque([start])
        color[start] = 0  

        while queue:
            current_vertex = queue.popleft()

            for neighbor in graph[current_vertex]:
                if neighbor not in color:  
                    color[neighbor] = 1 - color[current_vertex]
                    queue.append(neighbor)
                elif color[neighbor] == color[current_vertex]:
                    return True

    for vertex in graph:
        if vertex not in color: 
            if not bfs(vertex):
                return False

    return True

# Example usage
if __name__ == "__main__":
    bipartite_graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': ['A', 'D'],
        'D': ['B', 'C']
    }

    non_bipartite_graph = {
        'A': ['B', 'C'],
        'B': ['A', 'C'],
        'C': ['A', 'B']
    }

    print("Is the first graph bipartite?", is_bipartite(bipartite_graph))  # Should return True
    print("Is the second graph bipartite?", is_bipartite(non_bipartite_graph))  # Should return False