def countNumbersWithUniqueDigits(n: int) -> int:
        if n == 0:
            return 1
        
        dp = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        counter = 10

        newDp = []

        for i in range(2, n+1):
            for num in dp:
                for j in range(1, 10):
                    if str(j) not in num:
                        newDp.append(str(j) + num)
                        counter+=1
            dp = newDp
            newDp = []

        #print(dp)

        return len(dp)

print(countNumbersWithUniqueDigits(3))