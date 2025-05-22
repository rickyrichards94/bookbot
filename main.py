def get_book_text():
    with open("/home/rickyricky/bookbot/books/frankenstein.txt") as file:
        book_text = file.read()
        return book_text

def main():
    book_text = get_book_text()
    print(book_text)

main()