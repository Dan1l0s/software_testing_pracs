import math


# Check if dot is in circle with center in (0,0) and radius R, author: Dan1l0s
def check_dot_in_circle(x: float, y: float, radius: float) -> str:
    if (type(x) != float and type(x) != int) or (type(y) != float and type(y) != int) or (type(radius) != float and type(radius) != int):
        return "Incorrect data!"

    distance = math.sqrt(x * x + y * y)

    if distance < radius:
        return "Inside"
    if distance > radius:
        return "Outside"
    return "On the circle"


# Convert rbg color to hex color, author: Dan1l0s
def rgb_to_hex(r: int, g: int, b: int) -> str:
    if type(r) != int or type(g) != int or type(b) != int:
        return "Incorrect data!"
    if min(r, g, b) < 0 or max(r, g, b) > 255:
        return "Colors must have 0-255 values"
    return (f"#{hex(r)[2:]:0>2}{hex(g)[2:]:0>2}{hex(b)[2:]:0>2}").upper()


# Check if dot is in quadrangle, author: MaximAkhmin
def check_dot_in_quadrangle(dot: list, s1: list, s2: list, s3: list, s4: list) -> int:

    def vector_product(vec1: list, vec2: list):
        return vec1[0] * vec2[1] - vec1[1] * vec2[0]

    def calc_vector(vec1: list, vec2: list):
        return [vec1[0] - vec2[0], vec1[1] - vec2[1]]

    vec1 = vector_product(calc_vector(dot, s1), calc_vector(s2, s1))
    vec2 = vector_product(calc_vector(dot, s4), calc_vector(s3, s4))
    vec3 = vector_product(calc_vector(dot, s2), calc_vector(s3, s2))
    vec4 = vector_product(calc_vector(dot, s1), calc_vector(s4, s1))

    if vec1 * vec2 < 0 and vec3 * vec4 < 0:
        return 1
    elif vec1 * vec2 * vec3 * vec4 == 0:
        return 0
    else:
        return -1


# Check if provided number is a prime one, author: MaximAkhmin
def check_prime(number: int) -> bool:
    if number < 2:
        return False
    for i in range(2, int(number**(1 / 2) + 1)):
        if number % i == 0:
            return False
    return True


# Get two numbers' greatest common divisor, author: Kokhie
def get_gcd(a: int, b: int) -> int:
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a + b


# Get two lines common length, author: Kokhie
def get_joint_length(a1: int | float, a2: int | float, b1: int | float, b2: int | float) -> str | int | float:
    l1 = (a1, a2) if a2 > a1 else (a2, a1)
    l2 = (b1, b2) if b2 > b1 else (b2, b1)

    if l1[1] < l2[0] or l2[1] < l1[0]:
        return "No common ground"
    if l1[1] == l2[0] or l2[1] == l1[0]:
        return 0
    if l1[1] < l2[1]:
        return l1[1] - max(l1[0], l2[0])
    return l2[1] - max(l1[0], l2[0])


# Get power of a number in a faster way than math.pow, author: Acrid
def fast_power(base: int | float, exponent: int) -> int | float:
    if exponent == 0:
        return 1

    elif exponent % 2 == 0:
        half_power = fast_power(base, exponent // 2)
        return half_power * half_power

    else:
        half_power = fast_power(base, (exponent - 1) // 2)
        return base * half_power * half_power


# Get all prime numbers in range [2, n], author: Acrid
def generate_primes(n: int) -> list[int]:
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    primes = []
    for p in range(2, n + 1):
        if sieve[p]:
            primes.append(p)
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return primes
