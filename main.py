
def main():
    book_title_1 = "books/frankenstein.txt"
    number_of_words = 0
    char_dict = {}
    
    with open(book_title_1) as f:
        file_contents =f.read()

        print(file_contents)
        number_of_words = count_words(file_contents)
        char_dict = char_count(file_contents, char_dict)
    
    print(f"NUMBER OF WORDS: {number_of_words}")
    print("NUMBER OF EACH CHARACTER:")
    print(char_dict)

    print_report(number_of_words, char_dict)


def count_words(text):
    words = text.split()
    count = 0
    for word in words:
        count += 1
    
    return count


def char_count(text, char_dict):
    for c in text:
        if not c.isalpha():
            continue
        
        temp = c.lower()

        if temp in char_dict:
            char_dict[temp] += 1
        else:
            char_dict[temp] = 1

    return char_dict


def sort_on(dict):
    return dict["num"]


def print_report(num_words, c_dict):
    print("\n\n--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document.\n")

    # TODO: FINISH CONVERTING DICT TO LIST OF DICTS
    characters = []
    for item in c_dict:
        dict_item = {"character": item, "num": c_dict[item]}
        characters.append(dict_item)
    
    characters.sort(reverse=True, key=sort_on)
    
    # TODO: FINISH REPORT 
    for item in characters:
        print(f"The '{item["character"]}' character was found {item["num"]} times.")

    print("--- END REPORT ---")
    

# def dict_to_list(c_dict):
#     c_list = 
# _________________________________________________________________________
main()