def primes_below(n):
    # Keep a list of small primes
    small_primes = []

    # Go through all numbers less than sqrt(n)
    sqrt_n = int(n ** 0.5)
    for num in range(2, sqrt_n + 1):
        for prime in small_primes:
            # If num is divisible by prime
            if num % prime == 0:
                break
        else:
            # If num is not divisible by any of the small primes
            small_primes.append(num)

    # Filter all the other numbers
    large_primes = 0
    for num in range(sqrt_n + 1, n + 1):
        for prime in small_primes:
            # If num is divisible by prime
            if num % prime == 0:
                break
        else:
            # If num is not divisible by any of the small primes
            large_primes += 1

    print(len(small_primes) + large_primes)

primes_below(10**7)