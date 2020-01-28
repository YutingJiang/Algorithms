import sys
import re
from collections import defaultdict

visit= defaultdict(bool)
state = defaultdict(bool)
special = set()
result = set()

sys.setrecursionlimit(100000) # for large graph

def DFS_1(graph, node):
    visit[node] = True
    for i in graph[node]:
        if visit[i] == True and state[i] == state[node]:
            special.add(i)
            continue
        if visit[i] == False:
            state[i] = not state[node]
            DFS_1(graph, i)
    return

def DFS_2(graph, node, sign):
    visit[node] = True
    for i in graph[node]:
        if visit[i] == True:
            continue
        if sign == True and not(i in special):
            state[i] = not state[node]
            if state[i] == True:
                result.add(i)
            DFS_2(graph,i,True)
        else:
            result.add(i)
            DFS_2(graph,i,False)
    return


if __name__ == "__main__":
    adj_list = defaultdict(list)
    with open("input.txt","r") as f:
        contents = f.readlines()
        n = int(contents[0])
        edges = contents[1:n+1]
        start= int(re.findall(r"\d+",contents[-1])[0])
        for line in edges:
            x = re.findall(r"\d+",line)
            for i in range(1,len(x)):
                adj_list[int(x[0])].append(int(x[i]))
    state[start] = True
    for i in range(n):
        visit[i+1] = False
        state[i+1] = True
    DFS_1(adj_list, start)
    for i in visit.keys():
        visit[i] = False
    DFS_2(adj_list,start,True)
    with open("output.txt","w") as f:
        f.write(str(len(result)+1)+"\n")
        f.write("v"+str(start))
        for i in result:
            f.write(","+"v"+str(i))
    
