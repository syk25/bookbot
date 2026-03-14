from stats import get_book_text, count_words, count_characters


def print_report(
    my_book_path: str, book_text: str, word_count: int, char_counts: list[dict]
) -> None:

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {my_book_path}...")

    print("--------- Word Count ---------")
    print(f"Found {word_count} total words")

    print("--------- Character Count ---------")
    for char_entry in char_counts:
        print(f"{char_entry['char']}: {char_entry['count']}")

    print("-------------- END ---------------")
