n_m = raw_input()
n_m = list(n_m.split())
n = int(n_m[0])
m = int(n_m[1])
# print n, m
l = list(map(int, list(raw_input().split())))
# print contest
a = set(map(int, set(raw_input().split())))
# print A_list

b = set(map(int, set(raw_input().split())))
# print B_list

# processing
result = 0
for i in l:
    if i in a:
        result += 1
    if i in b:
        result += -1
print(result)

