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
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count_w} total words")
    print("--------- Character Count -------")
    for char, count in sorted(count_c.items(), key=lambda x: x[1], reverse=True):
        print(f"{char}: {count}")
    print("============= END ===============")

def maintest():
    test = count_characters("books/frankenstein.txt")
    print(test)


#maintest()
main()