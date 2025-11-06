def count_words(string):
    with open(string) as f:
        count = f.read()
    split_string = count.split()
    words = len(split_string)
    return f"Found {words} total words"

def count_characters(string):
    with open(string) as f:
        c = f.read()
    c = c.lower()
    
    char_count = {}
    for char in c:
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1

    return char_count