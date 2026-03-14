from collections import Counter


def get_book_text(path_to_file: str) -> str:
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def count_words(book_text: str) -> int:
    words = book_text.split()
    return len(words)


def count_characters(book_text: str) -> list[dict[str, int]]:
    character_counts = {}
    uncapitalized_text = book_text.lower()

    # Check character counts
    character_counts = Counter(book_text.lower())

    # Change Character counts dict to list
    character_count_list = []
    for key, value in character_counts.items():
        character_count_list.append({"char": key, "count": value})

    character_count_list.sort(reverse=True, key=lambda x: x["count"])

    return character_count_list
