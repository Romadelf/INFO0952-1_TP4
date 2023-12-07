def binarysearch(val, ll):
    return -1


def mergesort(ll):
    return ll


if __name__ == "__main__":
    ll = [3, 5, 6, 19, 40, 41, 50, 90]

    print(ll)
    print("50 trouvé à la position ", binarysearch(50, ll))
    print("4 trouvé à la position ", binarysearch(4, ll))
    print("5 trouvé à la position ", binarysearch(5, ll))

    ll = [3, 41, 50, 90, 10, 5, -2, 15]

    l2 = mergesort(ll)

    print("Avant le tri: ", ll, "\nAprès le tri: ", l2)
