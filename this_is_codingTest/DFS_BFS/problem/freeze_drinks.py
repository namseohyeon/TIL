N,M=map(int,input().split())

#DFS로 특정 노드를 방문하고, 연결된 모든 노드들도 방문
def dfs(x,y):
    #주어진 범위를 벗어나는 경우 즉시 종료
    if x <= -1 or x >=N or y <= -1 or y >=M:
        return False
    #현재 노드를 아직 방문하지 않았다면 
    if graph[x][y] == 0:
        #해당노드 방문처리
        graph[x][y] = 1
        #상하좌우 위치들도 모두 재귀적으로 호출
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False 
#2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(0,N):
    graph.append(list(map(int,input())))

#모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(N):
    for j in range(M):
        #현재 위치에서 DFS 수행
        if dfs(i,j) == True:
            result += 1
print(result)

