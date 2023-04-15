#python3

def read_input():
    # this function needs to acquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    input_type = input().rstrip().upper()

    if input_type == 'I':
        # Read input from keyboard
        pattern = input().rstrip()
        text = input().rstrip()
    elif input_type == 'F':
        # Read input from file
        with open('test_sample.txt', 'r') as file:
            pattern = file.readline().rstrip()
            text = file.readline().rstrip()

    # Return both lines as a tuple
    return pattern, text

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurrences using Rabin-Karp algorithm 
    occurrences = []
    p_len = len(pattern)
    t_len = len(text)

    # Compute the hash value of the pattern and the first substring of text
    p_hash = sum(ord(pattern[i]) for i in range(p_len)) % (2**64)
    t_hash = sum(ord(text[i]) for i in range(p_len)) % (2**64)

    # Precompute the power of prime for rolling hash
    prime = 101
    prime_power = 1
    for _ in range(p_len):
        prime_power = (prime_power * prime) % (2**64)

    for i in range(t_len - p_len + 1):
        if p_hash == t_hash:
            if pattern == text[i:i + p_len]:
                occurrences.append(i)
        
        if i < t_len - p_len:
            # Update the rolling hash value for the next substring
            t_hash = (t_hash - ord(text[i])) % (2**64)
            t_hash = (t_hash * prime + ord(text[i + p_len])) % (2**64)
            if t_hash < 0:
                t_hash += 2**64

    # Return an iterable variable
    return occurrences

# This part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
