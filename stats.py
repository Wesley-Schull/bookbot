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