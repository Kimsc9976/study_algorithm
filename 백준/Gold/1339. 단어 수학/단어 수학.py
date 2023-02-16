N = int(input())

r = []
temp = 0
for _ in range(N):
    txt = list(input())
    if len(txt) > temp:
      temp = len(txt)
    r.append(txt)

for i in range(N):
  r[i] = ['0']*(temp - len(r[i])) + r[i]
  
num_dic = dict()
for j in range(temp):
  for i in range(N):
    if r[i][j] == '0': continue
    if not num_dic.get(r[i][j]):
      num_dic.setdefault(r[i][j], 0)# [first_find ,cnt]
      num_dic[r[i][j]] += 10**((temp-1)-j)
    else:
      num_dic[r[i][j]] += 10**((temp-1)-j)

# print(num_dic)
x = list(num_dic.items())
x.sort(key = lambda x: (-x[1]))
# print(x)
ans = 0
for i in range(len(x)):
  ans += (9-i)*x[i][1]
print(ans)