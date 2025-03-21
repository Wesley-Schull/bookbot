# BookBot, the first of the Boot.Dev projects!

from stats import count_words, count_characters


def get_book_text(file_path):
    file_text = "No file found."
    
    try:
        with open(file_path) as f:
            file_text = f.read()
    except Exception as e:
        print(f"Error encountered: {e}")

    return file_text


def main():
    frankenstein_text = get_book_text("./books/frankenstein.txt")
    
    print(f"{count_words(frankenstein_text)} words found in the document")
    print(count_characters(frankenstein_text))

main()