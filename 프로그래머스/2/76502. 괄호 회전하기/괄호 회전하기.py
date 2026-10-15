from collections import deque

def solution(s):
    # 왼쪽회전 >> pop-left 후 append-right 시키는 과정 >> deque의 rotate함수를 쓰면 된다
    _lst = deque(s)
    _dict = { "{" :"}", "[" :"]", "(" :")"} # 여는것과 닫는 것은 쌍을 맞춰둔다
    answer = 0
    
    # s바퀴만 돌리면되니까 for _ in range(len(s)) 를 하면 된다    
    for _ in range(len(s)):
        _stk = []
        is_valid = True
        # 여기서부터는 괄호 찾기(?) 문제들과 동일하다, 스택을 찾고 재대로 닫혀있는지 확인하기
        # 프로그래머스 12973-짝지어-제거하기 문제를 확인해보면 좋다 (마침 최근에 푼 문제였다.)
        for c in _lst:
            if c in _dict:
                # 여는 괄호들은 스택에 넣어두기
                _stk.append(c)
            else:
                # 검증하기
                if len(_stk) == 0 : 
                    is_valid = False
                    break # 열린것도 없는데 바로 닫힌게 나온다고? 넘겨버려라
                braket = _stk.pop()
                if _dict.get(braket) != c : 
                    is_valid = False
                    break # 안맞는거니까 그냥 break 시키고 탈출
                    
        # 맞으면 +1 >> 맞는지 안맞는지는 스택이 비어있는지 확인해보면 된다.
        if (len(_stk) == 0) and is_valid:
            answer += 1 
        # rotate 시키기
        _lst.rotate(-1)

    return answer