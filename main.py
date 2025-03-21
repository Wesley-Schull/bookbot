# BookBot, the first of the Boot.Dev projects!

def get_book_text(file_path):
    file_text = "No file found."
    
    try:
        with open(file_path) as f:
            file_text = f.read()
    except Exception as e:
        print(f"Error encountered: {e}")

    return file_text


def count_words(input_text):
    words = input_text.split()
    
    return len(words)


def main():
    frankenstein_text = get_book_text("./books/frankenstein.txt")
    
    print(f"{count_words(frankenstein_text)} words found in the document")

main()