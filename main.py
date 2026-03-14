from stats import get_book_text, count_words, count_characters
from report import print_report
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    word_count = count_words(book_text)
    char_counts = count_characters(book_text)

    print_report(book_path, book_text, word_count, char_counts)


# call main at the bottom to execute the program
if __name__ == "__main__":
    main()
