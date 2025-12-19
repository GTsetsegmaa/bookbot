from stats import count_words, character_count

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def main():
    frankenstein = get_book_text("books/frankenstein.txt")
    num_words = count_words(frankenstein)
    print(f"Found {num_words} total words")
    print(character_count(frankenstein))

main()
