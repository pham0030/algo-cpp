# python3


def read_input():
    return (input().rstrip(), input().rstrip())


def print_occurrences(output):
    print(' '.join(map(str, output)))


def get_occurrences_naive(pattern, text):
    return [
        i
        for i in range(len(text) - len(pattern) + 1)
        if text[i:i + len(pattern)] == pattern
    ]


def poly_hash(string, prime, x):
    hash_ = 0
    for c in reversed(string):
        hash_ = (hash_ * x + ord(c)) % prime
    return hash_


def precompute_hashes(text, len_pattern, prime, x):
    len_text = len(text)
    Hashes = [None] * (len_text - len_pattern + 1)
    string = text[len_text-len_pattern:]
    Hashes[len_text-len_pattern] = poly_hash(string, prime, x)  # last hash
    y = pow(x, len_pattern, prime)  # efficient power mod prime in python3
    for i in reversed(range(len_text-len_pattern)):
        prehash = x * Hashes[i+1] + \
            ord(text[i]) - (ord(text[i + len_pattern]) * y) % prime
        while prehash < 0:
            prehash += prime
        Hashes[i] = prehash % prime
    return Hashes


def RabinKarp(pattern, text):
    prime = 1000000007
    x = 31
    len_text = len(text)
    len_pattern = len(pattern)
    pHash = poly_hash(pattern, prime, x)
    Hashes = precompute_hashes(text, len_pattern, prime, x)
    result = [
            i
            for i in range(len_text-len_pattern + 1)
            if pHash == Hashes[i] and pattern == text[i:i+len_pattern]
    ]
    return result

if __name__ == '__main__':
    print_occurrences(RabinKarp(*read_input()))
