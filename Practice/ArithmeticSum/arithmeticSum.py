testProgression = [1, 3, 5, 9]
testProgression2 = [2, 4, 8, 10, 12]

def recursiveMissingValue(progression, difference, start, end):
    if(start == end): # non ci sono elementi mancanti
        return -1
    
    mid = (start + end) // 2

    if(progression[mid] - progression[mid-1] != difference):
        return progression[mid] - difference
    
    if(progression[mid+1] - progression[mid] != difference):
        return progression[mid] + difference
    
    if(progression[start] != progression[mid] - difference * mid):
        return recursiveMissingValue(progression, difference, start, mid-1)
    
    if(progression[end] != progression[mid] + difference * len(progression) - mid):
        return recursiveMissingValue(progression, difference, mid+1, end)

def findMissingValue(progression):
    difference = (progression[-1] - progression[0]) / len(progression)
    return recursiveMissingValue(progression, difference, 0, len(progression)-1)

if __name__ == "__main__":
    print(findMissingValue(testProgression))