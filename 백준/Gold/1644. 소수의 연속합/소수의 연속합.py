import sys
import math
input = sys.stdin.readline

def isPrimeNum(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

n = int(input())

if n == 1:
    print(0)
    exit()

primes = []

for i in range(2, n + 1):
    if isPrimeNum(i):
        primes.append(i)

start, end = 0, 0
sum = primes[0]
cnt = 0

while start <= end and end < len(primes):
    if sum < n:
        end += 1
        if end < len(primes):
            sum += primes[end]
    elif sum == n:
        cnt += 1
        end += 1
        if end < len(primes):
            sum += primes[end]
    elif sum > n:
        sum -= primes[start]
        start += 1

        if start > end and start < len(primes):
            end = start
            sum = primes[start]

print(cnt)