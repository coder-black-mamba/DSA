from collections import deque

graph={}
graph["sayed"]=["alice","bob","claire"]
graph["bob"]=["anuj","peggy"]
graph["alice"]=["peggy"]
graph["claire"]=["thom","jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


# implementing the algorithm
def bfs(graph , search_item , root_node):
    search_queue=deque()
    search_queue+=graph[root_node]
    # track the item that searched previously.Otherwise it will Run Into An Endless loop
    searched_items=[]
    # itertae through the search que until it gets empty array a.k.a "[]"
    while search_queue:
        left_item = search_queue.popleft()
        if left_item not in searched_items:
            if left_item[-1]=='m':
                print(" left_item[-1]=='m'", left_item)
                print("Hey We Found What You Are Looking For : ",search_item)
                return True
            else:
                # update the search item
                search_queue+=graph[left_item]
                # save the left popped item for tracking 
                searched_items.append(left_item)
    return False



# 4th try
bfs(graph,"peegy","sayed")
# Ok Done Right Now