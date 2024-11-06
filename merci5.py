def get_proper_divisors(n):
    """Return a list of proper divisors of n (excluding n itself)."""
    divisors = [1]  # 1 is a proper divisor of every number greater than 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:  # i is a divisor of n
            divisors.append(i)
            if i != n // i:  # Avoid adding the square root twice
                divisors.append(n // i)
    return divisors

def find_perfect_numbers(limit):
    """Find and print all perfect numbers less than the given limit."""
    perfect_numbers = []
    
    for num in range(2, limit):
        divisors_sum = sum(get_proper_divisors(num))
        if divisors_sum == num:
            perfect_numbers.append(num)
    
    return perfect_numbers

# Find and print perfect numbers less than 1,000,000
limit = 1000000
perfect_numbers = find_perfect_numbers(limit)
print(f"Perfect numbers less than {limit} are: {perfect_numbers}")