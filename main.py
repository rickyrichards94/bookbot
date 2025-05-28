import sys
from stats import (word_count, char_count, book_sort)



def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = word_count(book_text)
    chars_dict = char_count(book_text)
    char_sorted_list = book_sort(chars_dict)
    print_report(book_path, num_words, char_sorted_list)

def get_book_text(path):
    print(f"Function called with path: {path}")  # Debug line
    with open(path) as f:
        return f.read()

def print_report(book_path, num_words, char_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in char_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()