import sys
from stats import get_word_count,get_char_count, get_char_sorted

def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
    return file_content


def main():
    if len(sys.argv) < 2:
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    #print(get_book_text("books/Frankenstein.txt"))
    char_dic = get_char_count(book_text)
    char_list  = get_char_sorted(char_dic)
    #print(char_dic)
    #print(f"Found {get_word_count(book_text)} total words")
    print("============ BOOKBOT ============")

    print("Analyzing book found at books/frankenstein.txt...")
    
    print("----------- Word Count ----------")

    print(f"Found {get_word_count(book_text)} total words")

    print("--------- Character Count -------")

    for dic in char_list:
        print(f"{dic['char']}: {dic['num']} \n")

    print("============= END ===============")



if __name__ == "__main__":
    main()