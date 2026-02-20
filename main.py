from stats import get_num_words, get_num_characters, read_book, sort_result
import sys


def print_dict(my_list:list) -> None:
    for dt in my_list:
        print(f"{dt["char"]}: {dt["num"]}")


def main() -> None:
    
    if len(sys.argv) == 2:
        file_path = sys.argv[1]
        book = read_book(file_path)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {file_path}...")
        print("----------- Word Count ----------")
        print(f"Found {get_num_words(book)} total words")
        print("--------- Character Count -------")
        print_dict(sort_result(get_num_characters(book)))
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

if __name__ == "__main__":
    main()
    

