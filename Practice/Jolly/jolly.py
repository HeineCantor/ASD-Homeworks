def buildDifferenceMarker(sequence, markerArray, start, end):
    if(start == end):
        return sequence[start]
    
    mid = (start + end) // 2
    buildDifferenceMarker(sequence, markerArray, start, mid)
    buildDifferenceMarker(sequence, markerArray, mid+1, end)
    difference = abs(sequence[mid]-sequence[mid+1])
    if(difference > 0 and difference <= len(markerArray)):
        markerArray[difference-1] = True

def checkJollySequence(sequence):
    markerArray = [False for _ in range(len(testSequence)-1)]

    buildDifferenceMarker(sequence, markerArray, 0, len(testSequence)-1)

    isJolly = True
    for element in markerArray:
        if(element is False):
            isJolly = False
            break

    return isJolly

if __name__ == "__main__":
    testSequence = [1, 4, 2, 3]

    if(checkJollySequence(testSequence)):
        print("Jolly")
    else:
        print("Not jolly")

