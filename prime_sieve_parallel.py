import bspy


def primes_below(bsp: bspy.BSPObject, n):
    # Keep a list of primes
    small_primes = []

    # Go through all numbers less than sqrt(n)
    sqrt_n = int(n ** 0.5)
    for num in range(2, sqrt_n + 1):
        for prime in small_primes:
            # If num is divisible by prime
            if num % prime == 0:
                break
        else:
            # If num is not divisible by any of the primes
            small_primes.append(num)

    # Filter all the other numbers
    chunk_size = int(n - sqrt_n) // bsp.cores

    large_primes = 0
    for num in range(sqrt_n + chunk_size * bsp.pid, sqrt_n + chunk_size * (bsp.pid + 1)):
        for prime in small_primes:
            # If num is divisible by prime
            if num % prime == 0:
                break
        else:
            # If num is not divisible by any of the primes
            large_primes += 1

    bsp.sync()

    # Send the number of primes we found to processor 0
    bsp.send(large_primes, 0)

    bsp.sync()

    # Only processor 0 needs to do anything in this superstep
    if bsp.pid == 0:
        # Note that we only count these here
        found_primes = len(small_primes)

        # Add every message we got to the found primes
        while (message := bsp.move()) is not None:
            found_primes += message

        print(found_primes)


if __name__ == "__main__":
    bspy.run(primes_below, 4, 10**7)