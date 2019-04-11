import math


def isprime(data):
    prime = 0
    if data == 1 or data == 0:
        prime = 1
    else:
        for x in range(2, int(math.sqrt(data) + 1)):
            if (data % x == 0):
                prime = 1
                break
    if prime == 1:
        return False
    else:
        return True


if __name__ == '__main__':
    for case in range(int(input())):
        n, l = input().split()
        list_prime = []
        for i in reversed(range(2, int(n) + 1)):
            if isprime(i) and len(list_prime) < 26:
                list_prime.insert(0, i)
            if len(list_prime) == 26:
                break
        # print(list_prime)
        text = [int(x) for x in input().split()]
        # print(text)
        ans = ''
        first = text[0]
        secound = text[1]
        for prime in list_prime:
            if first % prime == 0 and int(first / prime) in list_prime:
                a = prime
                b = int(first / prime)

            if secound % a
        for prime_two in list_prime:
            if secound % prime_two == 0 and int(secound / prime_two) in list_prime:
                c = prime_two
                d = int(secound / prime_two)
        # print(a, b, c, d)

        if a == c:
            first_cha_prime = b
        elif a == d:
            first_cha_prime = b
        else:
            first_cha_prime = a
        # print(first_cha_prime)

        prime_cha_old = first_cha_prime
        ans += chr(list_prime.index(first_cha_prime) + 65)

        for cha in text:
            next_cha = cha / prime_cha_old
            ans += chr(list_prime.index(next_cha) + 65)
            prime_cha_old = next_cha

        print('Case #{}: {}'.format(case + 1, ans))