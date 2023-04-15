#python3

class RabinKarp:
    def __init__(self, pattern, text):
        self.pattern = pattern
        self.text = text
        self.prime = 101
        self.multiplier = 256
        self.bucket_count = len(text) - len(pattern) + 1
        self.buckets = [[] for _ in range(self.bucket_count)]

    def _hash_func(self, s):
        # Hash function
        ans = 0
        for c in reversed(s):
            ans = (ans * self.multiplier + ord(c)) % self.prime
        return ans % self.bucket_count

    def add(self, string):
        hashed = self._hash_func(string)
        bucket = self.buckets[hashed]
        if string not in bucket:
            self.buckets[hashed].append(string)

    def delete(self, string):
        hashed = self._hash_func(string)
        bucket = self.buckets[hashed]
        for i in range(len(bucket)):
            if bucket[i] == string:
                bucket.pop(i)
                break

    def find(self, string):
        hashed = self._hash_func(string)
        if string in self.buckets[hashed]:
            return "yes"
        else:
            return "no"


def rabin_karp(pattern, text):
    occurrences = []
    p_len = len(pattern)
    t_len = len(text)
    p_hash = hash(pattern)
    t_hash = hash(text[:p_len])

    for i in range(t_len - p_len + 1):
        if p_hash == t_hash:
            if pattern == text[i:i + p_len]:
                occurrences.append(i)

        if i < t_len - p_len:
            t_hash = hash(text[i + 1:i + p_len + 1])

    return occurrences


if __name__ == '__main__':
    input_type = input().rstrip().upper()

    if input_type == 'I':
        pattern = input().rstrip()
        text = input().rstrip()
    elif input_type == 'F':
        with open('test_sample.txt', 'r') as file:
            pattern = file.readline().rstrip()
            text = file.readline().rstrip()

    occurrences = rabin_karp(pattern, text)
    print_occurrences(occurrences)





