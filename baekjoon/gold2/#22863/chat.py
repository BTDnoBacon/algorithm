import sys
input = sys.stdin.readline

n, k = map(int, input().split())
p = list(map(int, input().split()))
d = [0] + list(map(int, input().split()))

visited = [False] * (n+1) # 방문 여부를 저장할 리스트
res = [0] * n # 최종 결과를 저장할 리스트

for i in range(1, n+1):
    if not visited[i]: # i번 노드를 방문하지 않았을 경우
        cycle = [] # 사이클을 저장할 리스트
        j = i # 시작 노드
        while not visited[j]:
            visited[j] = True # 현재 노드를 방문했다고 표시
            cycle.append(j) # 현재 노드를 사이클에 추가
            j = d[j] # 다음 노드로 이동
        for idx, node in enumerate(cycle):
            res[(idx+k) % len(cycle)] = p[node-1] # 해당 노드의 값을 res에 저장

print(' '.join(map(str, res)))

