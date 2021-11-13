from dijkstra import Graph 
from dijkstra import DijkstraSPF
import json
json = json.load(open('spiritRealmLocations.json'))
nodes = json['nodes']


graph = Graph()

for node in nodes:
    for edge in node['edges']:
        graph.add_edge(str(node['id']), str(edge['destination_node']), edge['time_spent'])


dijkstra = DijkstraSPF(graph, "0")

print(dijkstra.get_path("999"))

path = dijkstra.get_path("999")

result = ""
for n in range(len(path) - 1):
    result += "("+str(path[n])+":"+str(path[n+1])+")"

print(result)