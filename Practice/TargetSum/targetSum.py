#hashmap
dp={}

def targetSum(array,target,temp,i):
    
    if (i,temp) in dp:
        return dp[(i,temp)]

    if i>=len(array):
        if temp==target: return 1
        else: return 0

    a = targetSum(array, target, temp + array[i], i+1)
    b = targetSum(array, target, temp - array[i], i+1)

    dp[(i,temp)]= (a + b)
    return a+b

#first test
array=[1,20,134,23,67,87,43,24,56,77,88,900,1,23,4,443,123,123,21,3123,1231,12,56,7,8,766,5,4,57,78,89,9,9123,14]
target=200
print(targetSum(array,target,0,0))

#second test
dp={} #hashmap "reset" just for simplicity
array=[1,1,1,1,1]
target=3
print(targetSum(array,target,0,0))

#third test
dp={} #hashmap "reset" just for simplicity
array=[1]
target=1
print(targetSum(array,target,0,0))

