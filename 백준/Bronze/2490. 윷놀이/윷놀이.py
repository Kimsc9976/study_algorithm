yut_info = {
    (1,3) : 'A',
    (2,2) : 'B',
    (3,1) : 'C',
    (4,0) : 'D',
    (0,4) : 'E'
}

for _ in range(3):
    yut = list(map(int, input().split()))
    zero = 0
    one = 0
    for item in yut:
        if item == 0:
            zero += 1
        elif item == 1:
            one += 1
    key_item = (zero, one)
    print(yut_info[key_item])