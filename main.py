from stats import count_words, character_count, sorted_dict

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def main():
    frankenstein = get_book_text("books/frankenstein.txt")
    num_words = count_words(frankenstein)
    num_of_chars = character_count(frankenstein)
    sorted_chars = sorted_dict(num_of_chars)
    
    print("============= BOOKBOT =============")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print(f"Found {num_words} total words")
    print("---------- Character Count -------")
    for diction in sorted_chars:
        if diction['char'].isalpha():
            print(f"{diction['char']}: {diction['num']}")
main()
