numbers = []
for _ in range(5):
    num = int(input())
    numbers.append(num)
    
print(sum(numbers)//5)
numbers.sort()
print(numbers[2])