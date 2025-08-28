import os
import sys
from stats import number_of_words, char_histogram, sorted_hist
def get_book_text(filepath):
    file_contents=""
    #print(filepath)
    with open(filepath) as f:
        #print(len(f.read()))
        file_contents = f.read()
    return file_contents




def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    fp = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {fp}...")
    print("----------- Word Count ----------")
    
    booktext = get_book_text(fp)
    nw = number_of_words(booktext)
    print(f"Found {nw} total words")
    print("--------- Character Count -------")
    ctr = char_histogram(booktext)
    sort_hist = sorted_hist(ctr)
    for h in sort_hist:
        print(f"{h["char"]}: {h["num"]}")
    print("============= END ===============")

if __name__=="__main__":
    main()