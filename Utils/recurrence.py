from math import log2

def logSquared(number):
    return log2(number)**2

def function_1_4_2(number):
    if(number == 1):
        return 1
    
    return function_1_4_2(number//2) + log2(number)

N = 1e300

print(logSquared(N) / function_1_4_2(N))