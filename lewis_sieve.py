def sieve_with_factors(n):
    # Create a dictionary to hold factors
    factors = {i: set() for i in range(2, n + 1)}
    
    # Create a set of all numbers from 2 to n
    numbers = set(range(2, n + 1))
    
    # Limit for sieving
    limit = int(n ** 0.5)
    
    # Iterate up to sqrt(n)
    for p in range(2, limit + 1):
        if p in numbers:  # If still in the set, it is prime
            for multiple in range(p * p, n + 1, p):
                numbers.discard(multiple)  # Remove multiple
                factors[multiple].add(p)  # Add p to factors of the multiple
                
            factors[p].add(p)  # Add p to its own factors (since it's a prime)
    
    # Add remaining prime numbers to their own factors
    for prime in numbers:
        factors[prime].add(prime)
    
    return sorted(numbers), factors  # Return primes and factors dictionary

# Example usage
n = 30
primes, prime_factors = sieve_with_factors(n)
print("Primes:", primes)
print("Prime Factors:", prime_factors)
