numbers = []
for _ in range(7):
    num = int(input())
    if num % 2 == 1:
        numbers.append(num)
    

if len(numbers) == 0:
    print(-1)
else:
    print(sum(numbers))
    print(min(numbers))