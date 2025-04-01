def num_words(text):
    count = 0
    for t in text.split():
        count += 1
    return count

def count_char_type(text):
    char_dic = {}
    
    for c in text:
        if c not in char_dic:
            char_dic[c] = 1
        else:
            char_dic[c] += 1
    
    return char_dic