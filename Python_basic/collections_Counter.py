from collections import Counter

X = int(input())
Shoes = Counter(list(map(int, input().strip().split()))[:X])
N = int(input())
income = 0
while N != 0:
    b = list(map(int, input().split()))
    for key, value in Shoes.items():
        if b[0] == key and value:
            Shoes[b[0]] = value - 1
            income = income + b[1]
    N -= 1
print(income)

from collections import Counter


# numShoes = int(input())
# shoes = Counter(map(int, input().split()))
# print(shoes)
# numCust = int(input())

# income = 0

# for _ in range(numCust):
#     size, price = map(int, input().split())
#     if shoes[size]:
#         income += price
#         shoes[size] -= 1

# print(income)
