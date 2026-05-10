import sys

def main():
    try:
        file_path = sys.argv[1]
    except Exception:
        print("Usage: python3 main.py <path_to_book>")

    book = get_book_text(file_path)
    num_words = count_words(book)
    num_of_chars = character_count(book)
    sorted_chars = sorted_dict(num_of_chars)
    
    print("\n============= BOOKBOT =============")
    print(f"Analyzing book found at {file_path}...")
    print(f"Found {num_words} total words")
    print("---------- Character Count -------")
    for diction in sorted_chars:
        if diction['char'].isalpha():
            print(f"{diction['char']}: {diction['num']}")
    print("=============== End ===============")


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents


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


main()
