from stats import count_words
from stats import count_characters

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents



    

def main():
    book = get_book_text("books/frankenstein.txt")
    count_w = count_words("books/frankenstein.txt")
    count_c = count_characters("books/frankenstein.txt")
    print(count_c)

def maintest():
    test = count_characters("books/frankenstein.txt")
    print(test)


#maintest()
main()