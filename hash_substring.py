#python3

def read_input():
    # this function needs to acquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow

    input_type = input().rstrip()
    if input_type == 'I':
        pattern = input().rstrip()
        text = input().rstrip()
    elif input_type == 'F':
        filename = input().rstrip()
        with open('./tests/06', 'r') as f:
            pattern = f.readline().rstrip()
            text = f.readline().rstrip()
    else:
        raise ValueError("Invalid input type")

    return pattern, text


def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))


def get_occurrences(pattern, text):
    # this function should find the occurrences using Rabin Karp algorithm

    p = 1000000007  # prime number
    b = 263  # base

    n = len(text)
    m = len(pattern)

    # calculate b^(m-1) mod p
    b_pow_m_minus_1 = pow(b, m-1, p)

    # calculate the hash value of the pattern
    pattern_hash = sum(ord(pattern[i]) * pow(b, m-i-1, p) for i in range(m)) % p

    # calculate the hash value of the first substring of length m
    text_hash = sum(ord(text[i]) * pow(b, m-i-1, p) for i in range(m)) % p

    occurrences = set()

    if pattern_hash == text_hash and pattern == text[:m]:
        occurrences.add(0)

    for i in range(1, n-m+1):
        # update the rolling hash function
        text_hash = (text_hash - ord(text[i-1]) * b_pow_m_minus_1) % p
        text_hash = (text_hash * b + ord(text[i+m-1])) % p

        if pattern_hash == text_hash and pattern == text[i:i+m]:
            occurrences.add(i)

    return sorted(occurrences)


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))




