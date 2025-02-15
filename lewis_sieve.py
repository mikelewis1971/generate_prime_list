def lewis_sieve(n):
    # Create a set of all numbers from 2 to n
    numbers = set(range(2, n + 1))
    
    # Limit for sieving
    limit = int(n ** 0.5)
    
    # Iterate up to sqrt(n)
    for p in range(2, limit + 1):
        if p in numbers:  # If still in the set, it is prime
            # Remove all multiples of p
            numbers -= set(range(p * p, n + 1, p))
    
    return sorted(numbers)  # Return primes

# Example Usage
if __name__ == "__main__":
    n = 100  # Change this to any upper limit
    primes = lewis_sieve(n)
    print("Primes from 2 to", n, ":", primes)
