from stats import count_words, character_count, sorted_dict
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

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
main()
