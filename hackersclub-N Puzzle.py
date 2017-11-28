import heapq
import copy


def heurestic(p):
    h = 0
    l = len(p)
    for i in range(l):
        for j in range(l):
            if p[i][j] == 0:
                continue
            h += abs(i - int((p[i][j])/l)) + abs(j - (p[i][j]%l))
    return h
class Frontier:
    def __init__(self):
        self.e = []

    def empty(self):
        return len(self.e) == 0
    def put(self, cost, item,move):
        heapq.heappush(self.e,((cost,item),move))


    def get(self):
        return heapq.heappop(self.e)
def end(l):
    m =[]
    for i in range(l):
        r = []
        for j in range(l):
            r.append( (i * l) + (j))
        m.append(r)
    return m


def move(m):

    output = []
    i = 0
    while 0 not in m[i]:
        i += 1
    j = m[i].index(0)
    if i > 0:                                   
        m[i][j], m[i-1][j] = m[i-1][j], m[i][j];  

        output.append(('UP',copy.deepcopy(m)))
        m[i][j], m[i-1][j] = m[i-1][j], m[i][j]; 
    
      
    if i < (len(m)-1):                                   
        m[i][j], m[i+1][j] = m[i+1][j], m[i][j]   

        output.append(('DOWN',copy.deepcopy(m)))
    
        m[i][j], m[i+1][j] = m[i+1][j], m[i][j]
        
    if j > 0:                                                      
        m[i][j], m[i][j-1] = m[i][j-1], m[i][j]   
        output.append(('LEFT',copy.deepcopy(m)))
        m[i][j], m[i][j-1] = m[i][j-1], m[i][j]

    if j < (len(m)-1):                                   
        m[i][j], m[i][j+1] = m[i][j+1], m[i][j]   
        output.append(('RIGHT',copy.deepcopy(m)))
        m[i][j], m[i][j+1] = m[i][j+1], m[i][j]
                 
    return output

def astar(p):
    tree = Frontier()
    moves = []
    tree.put(heurestic(p),[p],moves)
    goal =  end(len(p))
    expanded = []
    
    while True:
        a, current_moves = tree.get()
        cost , current_path = a
        current_node = current_path[-1] 
        
        if current_node == goal :
            print(len(new_moves))
            for m in new_moves:
                print(m)
            break
        
        
        nexts = move(current_node)

        for m,n in nexts:
            if n in expanded:
                continue
            new_cost = cost - (heurestic(current_node)) + heurestic(n)

            expanded.append(current_node)
            new_path = copy.deepcopy(current_path)

            new_path = new_path + [n]
            new_moves = copy.copy(current_moves)
            new_moves = new_moves + [m]
            tree.put(new_cost,new_path,new_moves)
            
puzze = []
n = int(input())
for i in range(n):
    row = []
    for j in range(n):
        row.append( int(input()))
    puzze.append(row)
astar(puzze)