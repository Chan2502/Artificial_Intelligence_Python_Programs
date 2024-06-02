romania_map ={
    'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},     
    'Bucharest': {'Urziceni': 85, 'Pitesti': 101, 'Giurgiu': 90, 'Fagaras': 211},
    'Craiova': {'Drobeta': 120, 'Rimnicu': 146, 'Pitesti': 138},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Eforie': {'Hirsova': 86},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Pitesti': {'Rimnicu': 97, 'Bucharest': 101, 'Craiova': 138},
    'Rimnicu': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
    'Urziceni': {'Vaslui': 142, 'Bucharest': 85, 'Hirsova': 98},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Sibiu': {'Arad': 140, 'Fagaras': 99, 'Oradea': 151, 'Rimnicu': 80},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Giurgiu': {'Bucharest': 90}, 
    'Mehadia': {'Drobeta': 75, 'Lugoj': 70},
    'Vaslui': {'Iasi': 92, 'Urziceni': 142},
    'Neamt': {'Iasi': 87}
}

H = {
    'Arad':366,
    'Bucharest':0,
    'Craiova':160,
    'Drobeta':242,
    'Eforie':161,
    'Fagaras':176,
    'Giurgiu':77,
    'Hirsova':151,
    'Iasi':226,
    'Lugoj':244,
    'Mehadia':241,
    'Neamt':234,
    'Oradea':380,
    'Pitesti':100,
    'Rimnicu':193,
    'Sibiu':253,
    'Timisoara':329,
    'Urziceni':80,
    'Vaslui':199,
    'Zerind':374
}

class priorityQueue:
    def __init__(self):
        self.queue = []
    def push(self,obj,cost):
        self.queue.append((cost,obj))
        self.queue.sort()
    def pop(self):
        return self.queue.pop(0)
    def Print(self):
        print(self.queue)

class node:
    def __init__(self,name,parent,Depth):
        self.name = str(name)
        self.hn = int(H.get(name))
        self.parent = parent
        self.Depth = Depth
        if parent != None:
            self.path = parent.path + [name]
            map = romania_map.get(parent.name)
            self.gn = int(parent.gn) + int(map.get(self.name))
            self.fn = self.hn + self.gn
        else:
            self.path = [name]
            self.fn = int(self.hn)
            self.gn = 0

    def Print(self):
        print(self.name,self.gn,self.hn,self.fn)
        print(self.path)
        print(self.Depth)

    def explore(self):
        M = []
        map = romania_map.get(self.name)
        M = list(map.keys())
        return M

def notVisited(i,Visited):
    for j in Visited:
        if i == j:
            return False
    return True
def Astar():
    Queue = priorityQueue()
    Initial = 'Arad'
    Goal = 'Bucharest'
    start = node(Initial,None,0)
    Queue.push(start,start.fn)
    N = 0

    while True:
        tup = Queue.pop()
        curr = tup[1]
        # curr.Print()
        if curr.name == Goal:
            print(curr.path,curr.Depth)
            print(curr.gn)
            print(f"number of nodes = {N}")
            print('Done using Astar')
            print("__"*50)
            return
        E =[]
        E = curr.explore()

        for name in E:
            d = curr.Depth + 1
            new_node = node(name,curr,d)
            N +=1
            # if name == Goal:
            #     flag = False
            #     new_node.Print()
            #     print('done')
            #     break
            Queue.push(new_node,new_node.fn)

def dfs(start, visited=None,parent=None):
    goal='Bucharest'
    if visited is None:
        visited = set()
    visited.add(start)
    if parent is None:
        d = 0
    else:
        d = parent.Depth + 1
    state = node(start,parent,d)
    
    if start == goal:
        print(state.path,state.Depth)
        print(state.gn)
        print("Done using DFS w/ leftmost first")
        print("__"*50)
        return 

    for next in romania_map[start]:
        if next not in visited:
            if goal not in visited:
                dfs(next, visited, state)
                

def DFS():
    Goal = 'Bucharest'
    Initial = "Arad"
    start = node(Initial,None,0)
    Visited = []
    Stack = []
    Stack.insert(0,start)
    while Stack:
        curr = Stack.pop(0)
        Visited.append(curr.name)
        if curr.name == Goal:
            print(curr.path,curr.Depth)
            print(curr.gn)
            print("Done using DFS w/ rightmost first")
            print("__"*50)
        generated = curr.explore()
        for i in generated:
            if notVisited(i,Visited):
                d = curr.Depth + 1
                state = node(i,curr,d)
                Stack.insert(0,state)
        
def iterDFS():
    Goal = 'Bucharest'
    Initial = "Arad"
    start = node(Initial,None,0)
    Depth = 0
    
    while True:
        print(f"iteration {Depth + 1}")
        Visited = []
        Stack = []
        Stack.insert(0,start)
        curr = start
        while Stack:
            curr = Stack.pop(0)
            # print(curr.path,curr.Depth)
            Visited.append(curr.name)
            if curr.name == Goal:
                print(curr.path)
                print(curr.gn)
                print("Done using iterative deepening")
                print("__"*50)
                return
            generated = curr.explore()
            for i in generated:
                if Depth < curr.Depth:
                    pass
                elif notVisited(i,Visited):
                    d = curr.Depth + 1
                    state = node(i,curr,d)
                    Stack.insert(0,state)
        Depth += 1

def BestFirstSearch():
    Queue = priorityQueue()
    Initial = 'Arad'
    Goal = 'Bucharest'
    start = node(Initial, None,0)
    Queue.push(start, start.hn)

    while True:
        tup = Queue.pop()
        curr = tup[1]
        # curr.Print()
        if curr.name == Goal:
            print(curr.path,curr.Depth)
            print(curr.gn)
            print('Done using Best first search')
            print("__"*50)
            return
        E = curr.explore()
        
        for name in E:
            d = curr.Depth + 1
            new_node = node(name, curr, d)
            Queue.push(new_node, new_node.hn)

def DepthLtdS():
    Goal = 'Bucharest'
    Initial = "Arad"
    start = node(Initial,None,0)
    Depth = 2
    
    while True:
        Visited = []
        Stack = []
        Stack.insert(0,start)
        curr = start
        while Stack:
            curr = Stack.pop(0)
            # print(curr.path,curr.Depth)
            Visited.append(curr.name)
            if curr.name == Goal:
                print(curr.path,curr.Depth)
                print(curr.gn)
                print("Done using Depth Limited Search w/ D = 3")
                print("__"*50)
                return
            generated = curr.explore()
            for i in generated:
                if Depth < curr.Depth:
                    pass
                elif notVisited(i,Visited):
                    d = curr.Depth + 1
                    state = node(i,curr,d)
                    Stack.insert(0,state)        
print("__"*50)
DepthLtdS()
BestFirstSearch()
iterDFS()
Astar()
dfs('Arad')
DFS()
