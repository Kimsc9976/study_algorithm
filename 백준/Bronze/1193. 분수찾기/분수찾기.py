target = int(input())

# n = math.ceil(math.sqrt(target))

n = 0
cnt = 0
while n < target:
    n += cnt
    cnt += 1

depth = cnt - 1
is_n_0 = True if depth % 2 else False
# if True start at array[n][0]
# if False start at array[0][n]

pref = sum([i for i in range(1,depth)])
to_walk = target - pref - 1 ## 몇칸 나아가야하나

div = f'{depth - to_walk}/{to_walk + 1}' if is_n_0 else f'{to_walk + 1}/{depth - to_walk}'

print(div)