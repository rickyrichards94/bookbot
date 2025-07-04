def word_count(book_text):
    words = book_text.split()
    return len(words)

def char_count(book_text):
    lower_text = book_text.lower()
    chars_count = {}
    for char in lower_text:
        if char in chars_count:    
            chars_count[char]+=1
        else:
            chars_count[char] = 1
    return chars_count

def sort_by_num(d):
    return d["num"]

def book_sort(chars_final):
    letter_count = []
    for ch in chars_final:  
        letter_count.append({"char": ch, "num": chars_final[ch]})
    letter_count.sort(reverse=True, key=sort_by_num)
    return letter_count