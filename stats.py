def count_words(text):
    text_split = text.split()
    count = 0
    for word in text_split:
        count += 1
    return count

def character_count(text):
    text_split = text.lower()
    char_count = {}
    for word in text_split:
        for char in word:
            char_count[char] = char_count.get(char, 0) + 1
    return char_count