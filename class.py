def count_primes(num):
    primes = [2]
    x = 3

    if num < 2:  # for the case of num = 0 or 1
        return 0

    while x <= num:  # x is my (odd) counter up to the input number
        for y in range(3,x,2):  # divide this x by every odd y beneath it to see if this x is prime
            if x%y == 0:   # 0 means that this x isn't prime
                x += 2   # so move on to the next odd counter
                break   # and go back to while?
        else:   # this gets run if this x IS a prime number
            primes.append(x)
            x += 2

    print(primes)
    return len(primes)
