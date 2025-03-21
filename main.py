# BookBot, the first of the Boot.Dev projects!

from stats import count_words, count_characters, sort_characters
from sys import *


def get_book_text(file_path):
    file_text = "No file found."
    
    with open(file_path) as f:
        file_text = f.read()

    return file_text


def main():
    try:
        if len(argv) != 2:
            raise Exception("Usage: python3 main.py <path_to_book>")
            sys.exit(1)
    except Exception as e:
        print(f"Error caught: {e}")
    
    path_to_book = argv[1]
    book_text = get_book_text(path_to_book)
    word_count = count_words(book_text)
    
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    character_count_list = sort_characters(count_characters(book_text))
    for char_dict in character_count_list:
        print(f"{char_dict["char"]}: {char_dict["count"]}")
    print("============= END ===============")


main()