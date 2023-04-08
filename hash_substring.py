# python3

def read_input():
    # this function needs to acquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    
    input_type = input().rstrip() # read input type choice (I or F)
    
    if input_type == 'I': # if input from keyboard
        pattern = input().rstrip() # read pattern from keyboard
        text = input().rstrip() # read text from keyboard
    elif input_type == 'F': # if input from file
        with open('sample.txt', 'r') as file: # assuming the sample input is in a file named sample.txt
            pattern = file.readline().rstrip() # read pattern from file
            text = file.readline().rstrip() # read text from file
            
    # return both lines in one return as tuple
    return (pattern, text)

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurrences using Rabin Karp algorithm 
    
    occurrences = [] # to store the positions of occurrences
    p = 31 # prime number for hashing
    m = len(pattern) # length of pattern
    n = len(text) # length of text
    pattern_hash = 0 # hash value of pattern
    text_hash = 0 # hash value of current window in text
    p_pow = 1 # power of p
    
    # calculate the hash value of pattern and the initial hash value of the first window in text
    for i in range(m):
        pattern_hash = (pattern_hash + (ord(pattern[i]) - ord('a') + 1) * p_pow) % (10**9 + 9)
        text_hash = (text_hash + (ord(text[i]) - ord('a') + 1) * p_pow) % (10**9 + 9)
        p_pow = (p_pow * p) % (10**9 + 9)
    
    # loop through the text to find occurrences of pattern
    for i in range(n - m + 1):
        if pattern_hash == text_hash: # if the hash values match
            if pattern == text[i:i+m]: # if the strings match
                occurrences.append(i) # add the position to occurrences
        
        # update the hash value of the next window in text
        if i < n - m:
            text_hash = (p * (text_hash - (ord(text[i]) - ord('a') + 1) * p_pow) + (ord(text[i + m]) - ord('a') + 1)) % (10**9 + 9)
    
    # return the list of occurrences
    return occurrences


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))



