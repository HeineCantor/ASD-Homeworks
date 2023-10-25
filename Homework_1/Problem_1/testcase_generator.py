import random

MAX_RAND_GENERATION = 999999999

TESTCASE_PATH = "./personal_testcase_temp.txt"
LENGTH = 10

file = open(TESTCASE_PATH, "w")

file.write(str(LENGTH) + "\n")

for i in range(LENGTH):
    value = random.randint(0, MAX_RAND_GENERATION)
    file.write(str(value) + "\n")