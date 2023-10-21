def mergeAndCount(array, start, mid, end):
    pass

def inversionCount(array, start, end):
    inversions = 0

    if start < end:
        middle = (start + end) // 2

        inversionCount(array, start, middle)
        inversionCount(array, middle+1, end)
        mergeAndCount(array, start, middle, end)

    return inversions


if __name__ == "__main__":
    pass
