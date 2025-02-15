### **Introducing the Lewis Sieve**  

The **Lewis Sieve** is a method for efficiently finding prime numbers up to a given limit, `n`. It systematically removes non-prime numbers, leaving behind only the primes. This approach relies on set operations to dynamically eliminate composite numbers, ensuring an optimized sieving process.

---

### **How It Works**  

The sieve begins with a set of all numbers from `2` to `n`. It then iterates through potential prime candidates, progressively removing their multiples from the set. This process continues until only prime numbers remain.

---

### **Step-by-Step Execution**  

1. **Initialize the Set of Numbers:**  
   - Create a set containing all integers from `2` to `n`.  

2. **Determine the Sieving Limit:**  
   - Only check numbers up to `sqrt(n)`, as larger numbers will already have been processed through smaller primes.  

3. **Iterate Through the Candidates:**  
   - For each number still in the set, it is a prime.  
   - Remove all multiples of that number from the set.  

4. **Output the Primes:**  
   - Once all candidates have been processed, return the remaining numbers as a sorted list of primes.  

---

### **Code Implementation**  

```python
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
```

---

### **Example Run (n = 30)**  

#### **Initial Set:**  
`{2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30}`  

#### **Processing Steps:**  
- Remove multiples of `2`: `{4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30}`  
- Remove multiples of `3`: `{9, 15, 21, 27}`  
- Remove multiples of `5`: `{25}`  

#### **Final Output:**  
`[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]`  

---

### **Why Use the Lewis Sieve?**  

✔ **Efficient Prime Detection** – Eliminates non-prime numbers systematically.  
✔ **Set-Based Processing** – Uses Python's set operations for quick removal.  
✔ **Optimized Computation** – Limits checks to `sqrt(n)`, reducing redundant operations.  
✔ **Simple Implementation** – Clear and easy-to-understand structure.  

Whether you’re a mathematician, programmer, or curious problem solver, the **Lewis Sieve** provides a powerful tool for prime number generation. 🚀
