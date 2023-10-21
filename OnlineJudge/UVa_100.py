minimumValue = 201
maximumValue = 210

maxCount = 0

for i in range(minimumValue, maximumValue + 1):
    n = i

    counter = 1

    while n > 1:
        counter += 1
        if n%2 != 0:
            n = 3*n + 1
        else:
            n = n/2

    maxCount = max(maxCount, counter)

print(f"MAX COUNT IS: {maxCount}")