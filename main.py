from stats import num_words, count_char_type, sorted_dic
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    text = get_book_text(sys.argv[1])
    count_words = num_words(text)
    count_chars = count_char_type(text.lower())
    sorted_dictionary = sorted_dic(count_chars)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count_words} total words")
    print("--------- Character Count -------")
    for i in sorted_dictionary:
        print(f"{i["char"]}: {i["count"]}")
    print("============= END ===============")




def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


main()