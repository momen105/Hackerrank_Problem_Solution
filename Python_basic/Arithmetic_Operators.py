def print_rangoli(size):

    k = 2 * size - 2
    for i in range(0, size):
        for j in range(0, k):
            print(end="-")
        k = k - 1
        for j in range(0, i + 1):
            print("* ", end="")
        print("")

    k = size - 2

    for i in range(size, -1, -1):
        for j in range(k, 0, -1):
            print(end=" ")
        k = k + 1
        for j in range(0, i + 1):
            print("* ", end="")
        print("")


if __name__ == "__main__":
    n = int(input())
    print_rangoli(n)
