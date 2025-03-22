# BookBot, the first of the Boot.Dev projects!

from stats import * # importing everything from the stats.py file
from sys import argv # only importing argv, since that's all we're using here



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
    
    # Take second argument (argv[1]) as input to get the book's filepath
    path_to_book = argv[1]
    
    # Generate data to input for the report
    book_text = get_book_text(path_to_book)
    word_count = count_words(book_text)
    character_count_list = sort_characters(count_characters(book_text))

    # Print a report to the console using our data
    print_report(path_to_book, word_count, character_count_list)
    
    


main()