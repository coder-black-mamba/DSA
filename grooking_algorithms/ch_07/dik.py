# WoooOOOoooo
# Dijkstra's Algorithm
# holding the main graph data structure
graph={}
# adding one node
graph["start"]={}
# subnode to the finish
graph["start"]["a"]=6
graph["start"]["b"]=2

# print(graph["start"].keys())
# now adding a,b nodes
graph["a"]={}
graph["b"]={}

graph["a"]["fin"]=1
graph["b"]["a"]=3
graph["b"]["fin"]=5
graph["fin"]={}
# print(graph)

# create a hash table for costs
# infinity ∞
infinity = float("inf")

costs={}
costs["a"]=6
costs["b"]=2
costs["fin"]=infinity

# hash table for parents
parents={}
parents["a"]="start"
parents["b"]="start"
parents["fin"]=None

# print(costs)
# print(parents)

# for having things tracked up 
processed=[]

def find_lowest_cost_node(costs):
    lowest_cost=float("inf")
    lowest_cost_node=None

    for node in costs:
        cost=costs[node]
        if cost<lowest_cost and node not in processed:
            lowest_cost=cost
            lowest_cost_node=node
    return lowest_cost_node


# print(find_lowest_cost_node(costs))

node = find_lowest_cost_node(costs)
shortest_path=[]
while node is not None:
    cost=costs[node]
    neighbours=graph[node]
    print("cost" , cost)
    print("neighbours",neighbours)
    for n in neighbours.keys():
        print("neighbours[n]",neighbours[n])
        new_cost=cost+neighbours[n]
        if costs[n]>new_cost:
            costs[n]=new_cost
            parents[n]=node
        shortest_path.append(node)
    processed.append(node)
    node=find_lowest_cost_node(costs)


print(shortest_path)