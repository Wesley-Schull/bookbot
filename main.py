# BookBot, the first of the Boot.Dev projects!

from stats import count_words, count_characters, sort_characters


def get_book_text(file_path):
    file_text = "No file found."
    
    try:
        with open(file_path) as f:
            file_text = f.read()
    except Exception as e:
        print(f"Error encountered: {e}")

    return file_text


def main():
    frankenstein_text = get_book_text("books/frankenstein.txt")
    character_count_list = sort_characters(count_characters(frankenstein_text))
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(frankenstein_text)} total words")
    print("--------- Character Count -------")
    for char_dict in character_count_list:
        print(f"{char_dict["char"]}: {char_dict["count"]}")
    print("============= END ===============")

main()