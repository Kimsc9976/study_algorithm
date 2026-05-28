from collections import deque

def sliding_min(arr, k):
    """
    [슬라이딩 윈도우 + Monotonic Deque]

    길이 k인 창이 한 칸씩 이동할 때,
    매번 창 안의 최솟값(min)을 O(1) amortized로 구한다.

    ---

    처음 시도했던 방식 (maxlen + min):
        window = deque(maxlen=k)
        window.append(x)
        res.append(min(window))   # ← 창 전체를 매번 훑음 → O(k)

    이 방식도 '슬라이딩 윈도우' 아이디어는 맞지만,
    w나 h가 크면 O(m * n * (w + h))라 Python에서 TLE 날 수 있다.

    ---

    Monotonic Deque를 쓰는 이유:
        deque 자체가 min을 자동으로 해주는 게 아니다.
        우리가 '앞으로 최솟값 후보가 될 수 있는 인덱스'만 남기도록
        규칙을 직접 만들어 주는 것이다.

        - popleft(): 창 밖으로 나간(만료된) 인덱스 제거
        - pop()    : 지금 값보다 크거나 같아서, 앞으로 min이 될 일 없는 인덱스 제거
        - append() : 새 후보 등록

        dq[0]이 항상 현재 창의 최솟값 인덱스가 되므로,
        min(window)처럼 매번 O(k) 탐색할 필요가 없다 → 전체 O(n)
    """
    dq = deque()  # 인덱스 저장 (값이 아닌 인덱스! arr[dq[i]]는 증가 순서)
    res = []

    for i, x in enumerate(arr):
        # 1) 창 밖으로 나간 인덱스 제거
        #    현재 i 기준 창은 [i-k+1, i]
        #    i-k 보다 작거나 같으면 이미 창 밖
        while dq and dq[0] <= i - k:
            dq.popleft()

        # 2) 최솟값 후보가 될 수 없는 인덱스 제거
        #    뒤에서부터 보며, arr[dq[-1]] >= x 이면
        #    x가 창 안에 있는 동안 절대 최솟값이 될 수 없음
        while dq and arr[dq[-1]] >= x:
            dq.pop()

        # 3) 현재 인덱스를 후보로 등록
        dq.append(i)

        # 4) 창이 k개 채워졌을 때부터 결과 기록
        if i >= k - 1:
            res.append(arr[dq[0]])  # dq[0] = 현재 창에서 가장 작은 값의 인덱스

    return res


def solution(m, n, h, w, drops):
    """
    [핵심 아이디어]

    문제: h x w 선인장 구역을 어디에 두면
         가능한 한 늦게(또는 아예 안) 비를 맞을까?

    ---

    1단계) 각 칸에 '몇 번째 빗방울'이 떨어졌는지 기록
        - drops[i] = [r, c]  →  grounds[r][c] = i + 1
        - 비 안 맞은 칸     →  inf

    2단계) 선인장 좌상단 (top_r, top_c)마다 '처음 젖는 순서' 계산
        - h x w 영역 안 칸들 중 가장 빠른(작은) drop 순서 = first_wet
        - 영역 안에 inf가 하나라도 있으면 → 영원히 안 젖음 (최우선)
        - first_wet이 클수록 좋음 (늦게 젖음)
        - 동점이면 → 행 작은 것 → 열 작은 것

    3단계) 2D 구간 min을 슬라이딩 윈도우로 구하기
        - 한 번에 h x w 전체를 min()하면 O(h * w) → 너무 느림
        - 가로 w min → 세로 h min 으로 2-pass 분리 (분리 가능!)
        - 각 pass는 sliding_min()으로 O(m * n)

    ---

    예시 직관:
        first_wet(top_r, top_c)
            = min( grounds[r][c] for r in [top_r..top_r+h-1],
                              c in [top_c..top_c+w-1] )

        이 min을 모든 (top_r, top_c)에 대해 구한 뒤,
        row-major 순회로 score가 가장 큰 위치를 고른다.
    """
    INF = float('inf')
    grounds = [[INF for _ in range(n)] for _ in range(m)]

    # drops 순서대로 각 칸에 빗방울 번호 기록
    for i, drop in enumerate(drops):
        a, b = drop
        grounds[a][b] = i + 1

    # --------------------------------------------------
    # Pass 1) 각 행에서 가로 w 구간의 min
    #
    # row_min[r][c] = grounds[r][c : c+w] 의 최솟값
    #
    # 슬라이딩 윈도우가 가로로 w칸씩 밀리며 min을 구한다.
    # --------------------------------------------------
    row_min = [sliding_min(grounds[r], w) for r in range(m)]

    rows = m - h + 1  # 선인장 좌상단 row 후보 수
    cols = n - w + 1  # 선인장 좌상단 col 후보 수

    # --------------------------------------------------
    # Pass 2) row_min 결과에 대해 세로 h 구간의 min
    #
    # window_first_wet[r][c]
    #   = (top_r=r, top_c=c)에 h x w 선인장을 뒀을 때
    #     처음 비를 맞는 순서
    #
    # 가로 min 결과를 세로로 h칸씩 슬라이딩하면
    # 2D h x w 구간 min이 된다.
    # --------------------------------------------------
    window_first_wet = [[INF for _ in range(cols)] for _ in range(rows)]

    for c in range(cols):
        # 같은 열 c에서, 각 행의 가로-w-min 값들을 모음
        column = [row_min[r][c] for r in range(m)]
        col_mins = sliding_min(column, h)

        for r in range(rows):
            window_first_wet[r][c] = col_mins[r]

    # --------------------------------------------------
    # Pass 3) 정답 위치 선택
    #
    # - score가 클수록 좋음 (inf = 안 젖음 = 최우선)
    # - for r → for c 순서 = tie-break (위쪽 행, 왼쪽 열)
    #   동점이면 먼저 만난 (r, c)가 더 위·더 왼쪽이므로
    #   별도 처리 없이 row-major 순회만으로 충분
    # --------------------------------------------------
    best_score = -1
    answer = [0, 0]

    for r in range(rows):
        for c in range(cols):
            score = window_first_wet[r][c]
            if score > best_score:
                best_score = score
                answer = [r, c]

    return answer
# 더 많은 코드들은...
# https://kimsc9976.github.io/algorithm/프로그래머스/