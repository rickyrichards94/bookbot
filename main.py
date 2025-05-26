from stats import word_count, char_count

def get_book_text():
    with open("/home/rickyricky/bookbot/books/frankenstein.txt") as file:
        book_text = file.read()
        return book_text

def main():
    book_text = get_book_text()
    print(word_count(book_text), "words found in the document")
    print(char_count(book_text))

main()