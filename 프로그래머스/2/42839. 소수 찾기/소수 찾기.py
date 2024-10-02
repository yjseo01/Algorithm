import math
from itertools import permutations

def solution(numbers):
    answer = 0
    
    def isPrime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    
    unique_numbers = set()
    
    for i in range(1, len(numbers) + 1):
        perms = permutations(numbers, i)
        for perm in perms:
            num = int(''.join(perm))
            unique_numbers.add(num)
    
    answer = sum(1 for num in unique_numbers if isPrime(num))
        
    return answer