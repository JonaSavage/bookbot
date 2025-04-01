from stats import num_words, count_char_type

def main():
    text = (get_book_text("books/frankenstein.txt"))
    # print(text)
    count_words = num_words(text)
    count_chars = count_char_type(text.lower())
    print(f"{count_words} words found in the document")
    print(count_chars)





def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


main()