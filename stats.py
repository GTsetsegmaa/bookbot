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

def sorted_dict(dict):
    char_count = []
    for key, value in dict.items():
        char_count.append({"char": key, "num": value})
    char_count.sort(reverse=True, key=sort_on)
    return char_count

def sort_on(items):
    return items["num"]