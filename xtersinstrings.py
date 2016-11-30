def find_chars_slow(string1, string2):
    res = []
    for char in string1:
        if char in string2:
            res.append(char)

    return ''.join(res)


from collections import defaultdict

def find_find_char_fast(string1, string2):
    d = defaultdict(int)

    for char in string2:
        d[char] += 1

        res = []

        for char in string1:
            if char in d:
                res.append(char)

        return ''.join(res)
