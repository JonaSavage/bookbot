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

def sort_on(dict):
    return dict["count"]

def sorted_dic(unsorted_dic):
    sorted_list = []
    # sorted_dic = {"letter": "t", }

    for item in unsorted_dic:
        if item.isalpha():
            temp_dic = {"char": item, "count": unsorted_dic[item]}
            sorted_list.append(temp_dic)
    
    sorted_list.sort(reverse=True, key=sort_on)
    #print(sorted_list)

    
    #sorted_dic.sort(reverse=True, key=sort_on)
    return sorted_list