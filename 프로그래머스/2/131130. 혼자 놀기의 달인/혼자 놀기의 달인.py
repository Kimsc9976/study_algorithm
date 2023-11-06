from itertools import combinations

def dfs(now, is_visited, cards, counts):
    if is_visited[now]: return counts
    
    is_visited[now] = True
    _next = cards[now]
    
    return dfs(_next, is_visited, cards, counts+1)

def solution(cards):
    answer = 0
    cards = [0] + cards
    
    
    for a, b in combinations(range(1, len(cards)), 2):
        is_visited = [False for _ in range(len(cards))]
        
        count1 = dfs(a, is_visited, cards, 0)
        count2 = dfs(b, is_visited, cards, 0)
        
        answer = max(answer, count1*count2)
    
    return answer