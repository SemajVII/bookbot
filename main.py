from stats import get_book_txt
from stats import word_count
from stats import character_count
from stats import sort_on
from stats import new_dic
import sys

def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    print("============ BOOKBOT ============")
    print("Analyzing book found at", filepath)
    print("----------- Word Count ----------")
    print("Found",word_count(get_book_txt(filepath)),"total words")
    print("--------- Character Count -------")
    character_dic = character_count(get_book_txt(filepath))
    new_chr_dic = new_dic(character_dic)
    new_chr_dic.sort(reverse=True, key=sort_on)
    for dic in new_chr_dic:
        if dic["char"].isalpha():
            print(f"{dic["char"]}: {dic["num"]}")
main()
