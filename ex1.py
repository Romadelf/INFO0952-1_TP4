def binarysearch(val, l):
    return -1


def mergesort(l):
    return l


if __name__ == "__main__":
    l = [3, 5, 6, 19, 40, 41, 50, 90]

    print(l)
    print("50 trouvé à la position ", binarysearch(50, l))
    print("4 trouvé à la position ", binarysearch(4, l))
    print("5 trouvé à la position ", binarysearch(5, l))

    l = [3, 41, 50, 90, 10, 5, -2, 15]

    l2 = mergesort(l)

    print("Avant le tri: ", l, "\nAprès le tri: ", l2)
