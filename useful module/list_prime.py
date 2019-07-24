# how to use : find_prime(number)
# return : primes between 2 to number


def find_prime(n):
    is_prime = [True] * (n + 1)

    for a in range(2, int(n ** 0.5) + 1):
        if is_prime[a]:
            for j in range(a ** 2, n + 1, a):
                is_prime[j] = False

    return [a for a in range(2, n + 1) if is_prime[a]]
