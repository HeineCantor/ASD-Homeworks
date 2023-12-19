def countVowelStrings(n : int) -> int:
    counters = [1, 1, 1, 1, 1]

    for i in range(1, n):
        counters[1] *= 2
        counters[2] *= 3
        counters[3] *= 4
        counters[4] *= 5

    return sum(counters)

print(countVowelStrings(33))