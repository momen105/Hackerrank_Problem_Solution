n = int(input())
t = tuple(list(map(int, input().split()))[:n])
print(hash(t))
