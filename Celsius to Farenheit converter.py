def exactly3Divisors(N):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    count = 0
    for i in range(2, int(N**0.5) + 1):
        if is_prime(i):
                # Increment count if i*i is less than or equal to N
            if i*i <= N:
                count += 1

    return count

C = int(input("Enter the value: "))
print(exactly3Divisors(C))