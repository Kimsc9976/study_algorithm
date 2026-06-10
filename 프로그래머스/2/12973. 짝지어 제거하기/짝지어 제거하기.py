def solution(s):
    """
    [Stack]

    문자열을 왼쪽부터 순서대로 확인한다.

    현재 문자와 바로 이전 문자가 같으면 제거해야 하는데,
    이전 문자가 이미 제거되었을 수도 있기 때문에
    단순히 인덱스로 이전 문자만 비교해서는 처리하기 어렵다.

    따라서 '현재까지 제거되지 않고 남아있는 문자들'을
    Stack으로 관리한다.

    예)
    baabaa

    b -> [b]
    a -> [b, a]
    a -> [b]      (aa 제거)
    b -> []       (bb 제거)
    a -> [a]
    a -> []       (aa 제거)

    최종적으로 Stack이 비어있으면 모든 문자를 제거할 수 있는 것이고,
    문자가 남아있다면 제거하지 못한 문자가 존재하는 것이다.

    시간복잡도 : O(N)
    각 문자는 최대 1번 push, 1번 pop 된다.
    """

    stack = list()
    for c in s:
        
        # 스택이 비어 있는 경우
        # 비교 대상이 없으므로 현재 문자를 그대로 저장
        if len(stack) == 0:
            stack.append(c)
        # 스택의 가장 위 문자와 현재 문자가 같다면
        # 두 문자가 짝을 이루므로 제거
        elif stack[-1] == c:
            stack.pop()
        # 스택의 가장 위 문자와 현재 문자가 다르다면
        # 아직 제거할 수 없으므로 현재 문자를 저장
        else:
            stack.append(c)
    
    return 1 if len(stack) == 0 else 0 # stack에 남은게 없으면 1 있으면 0 출력하기
# 더 많은 코드들은...
# https://kimsc9976.github.io/algorithm/프로그래머스/
