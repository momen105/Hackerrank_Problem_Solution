import itertools

if __name__ == "__main__":
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    result = [
        [i, j, k]
        for i, j, k in itertools.product(range(x + 1), range(y + 1), range(z + 1))
        if i + j + k != n
    ]
    # ________________another answer_____________________
    # result = []
    # for i in range(x+1):
    #     for j in range(y+1):
    #         for k in range(z+1):
    #             if i+j+k == n:
    #                 continue
    #             result.append([i,j,k])
    print(result)
