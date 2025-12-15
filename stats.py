def get_word_count(text):
    text_list = text.split()
    return len(text_list)

def get_char_count(text):
    char_dic = {}
    for char in text.lower():
        if char in char_dic:
            char_dic[char] += 1
        else:
            char_dic[char] = 1
    return char_dic


def get_char_sorted(dictionary):
    
        
    char_list = []
    for char in dictionary:
        char_list.append({"char":char,"num":dictionary[char]})
    
    def sort_on(rand_dict):
        return rand_dict["num"]
    char_list.sort(reverse=True, key = sort_on)

    return char_list