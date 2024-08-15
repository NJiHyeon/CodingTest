def solution(n, s, a, b, fares):
    import heapq
    graph = {}
    for fare in fares:
        aa, bb, cc = fare[0], fare[1], fare[2]
        if aa not in graph:
            graph[aa] = [(bb, cc)]
        else:
            graph[aa].append((bb, cc))
        if bb not in graph:
            graph[bb] = [(aa, cc)]
        else:
            graph[bb].append((aa, cc))
    
    distances = [[float('inf')] * (n+1) for _ in range(3)]
    distances[0][s] = distances[1][a] = distances[2][b] = 0
    
    for i, start_v in enumerate([s, a, b]):
        pq = [(0, start_v)]
        while pq:
            cur_dist, cur_v = heapq.heappop(pq)
            if distances[i][cur_v] < cur_dist:
                continue
            for next_v, cost in graph[cur_v]:
                next_dist = distances[i][cur_v] + cost
                if next_dist < distances[i][next_v]:
                    distances[i][next_v] = next_dist
                    heapq.heappush(pq, (next_dist, next_v))
        
    answer = float('inf')
    for i in range(1, n+1):
        answer = min(answer, distances[0][i]+distances[1][i]+distances[2][i])
    return answer