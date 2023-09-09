import sys
import math
import time

while True:
    A = int(input('Input the number of numbers to process:'))
    if 2 <= A <= 30:
        break

num_list=[]
bo = True

while bo:
    num_list = list(map(int, input('Input the numbers to be processed:').split()))

    for i in num_list:
        if 0 < i <= 100000:
            bo = False
        else:
            bo = True
            break


# 시작시간
start = time.time()

num_list = set(num_list)
num_list = list(num_list)
num_list.sort()

sieve = [True] * 100001

m = int(100001 ** 0.5)

for i in range(2, m + 1):
    if sieve[i] == True:
        for j in range(i+i, 100001, i):
            sieve[j] = False  


for i in range(0, len(num_list) - 1):
    cnt = 0
    for j in range(num_list[i], num_list[i + 1] + 1):
        if sieve[j] == True:
            cnt += 1
    print("Number of prime numbers between " + str(num_list[i]) + "," + str(num_list[i + 1]) + ": " + str(cnt))


# 종료시간
end = time.time()

print("Total execution time using Python is" + " " + f"{end - start:.17f} seconds!")