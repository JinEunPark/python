
def dfs(computers,net, vtx, visited):
    if vtx not in visited:
        visited.add(vtx)
        net.append(vtx)
        for i in range(len(computers)):
            if i in visited:
                computers[vtx][i] = 0
        for i in range(len(computers)):
            if computers[vtx][i] == 1:
                dfs(computers,net,i,visited)
    return net



def solution(n, computers):
    answer = 0
    vtx = set(x for x in range(n))   
    visited = set()
    netList = []

    for v in vtx:
        if v not in visited:
            net = dfs(computers,[],v,visited)
            netList.append(net)
    answer = len(netList)
    return answer


  