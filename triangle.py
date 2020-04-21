for i in range(10):
    for j in range(9 - i):
        print(' ', end="")
    for j in range(2 * i + 1):
        print("*", end="")
    print()
