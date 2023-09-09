import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def count_primes_between(x, y):
    count = 0
    for n in range(x+1, y):
        if is_prime(n):
            count += 1
    return count

def main():
    m = 0
    while m <= 1 or m > 30:
        m = int(input("Input the number of numbers to process : "))
    
    n = 0
    while n <= 1 or n > 100000:
        n = int(input("Input the numbers to be processed "))
    nums = list(map(int, input().split()))
    nums = sorted(list(set(nums)))
    
    count = 0

    primes_counts = []
    for i in range(len(nums)-1):
        primes_count = count_primes_between(nums[i], nums[i+1])
        primes_counts.append(primes_count)
    for i in range(len(primes_counts)):
        print("Number of prime numbers between "+nums[i]+", "+nums[i+1]+":"+primes_counts[i])