import sys
from stats import count_words
from stats import count_characters

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents



    

def main():
    file_path = sys.argv[1]
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    count_w = count_words(file_path)
    count_c = count_characters(file_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")
    print("----------- Word Count ----------")
    print(f"Found {count_w} total words")
    print("--------- Character Count -------")
    for char, count in sorted(count_c.items(), key=lambda x: x[1], reverse=True):
        print(f"{char}: {count}")
    print("============= END ===============")

main()