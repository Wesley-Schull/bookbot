# BookBot, the first of the Boot.Dev projects!

def get_book_text(filepath):
    file_text = "No file found."
    
    try:
        with open(filepath) as f:
            file_text = f.read()
    except Exception as e:
        print(f"Error encountered: {e}")

    return file_text

def main():
    print(get_book_text("./books/frankenstein.txt"))
    # print(get_book_text("f"))

main()