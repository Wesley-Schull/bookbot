def count_words(input_text):
    words = input_text.split()
    
    return len(words)


def count_characters(input_text):
    char_count_dict = {}
    
    for char in input_text.lower():
        if char not in char_count_dict:
            char_count_dict[char] = 0
        char_count_dict[char] += 1

    return char_count_dict


def sort_by_count(dict):
    return dict["count"]


def sort_characters(char_dict):
    alphabetic_chars_list = []
    
    for key in char_dict:
        if key.isalpha():
            alphabetic_chars_list.append({"char": key, "count": char_dict[key]})
    
    alphabetic_chars_list.sort(reverse=True, key=sort_by_count)
    
    return alphabetic_chars_list #.sort(reverse=True, key=sort_by_count)