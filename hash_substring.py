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

    # Compute hash of the pattern and the initial hash of the first window in the text
    p_hash = sum(ord(c) for c in pattern)
    t_hash = sum(ord(c) for c in text[:p_len])

    # Iterate through all possible windows in the text
    for i in range(t_len - p_len + 1):
        if p_hash == t_hash:  # If the hash of the window matches the hash of the pattern
            if pattern == text[i:i + p_len]:  # If the window matches the pattern
                occurrences.append(i)

        if i < t_len - p_len:  # Update the hash for the next window
            t_hash = t_hash - ord(text[i]) + ord(text[i + p_len])

    # Return an iterable variable
    return occurrences


# This part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))



