def read_book(file_path:str) -> str:
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def get_num_words(book:str) -> int:
    return len(book.split())

def get_num_characters(book:str) -> dict[str, int]:
    book_text = book.lower()

    character_count = {}
    for character in book_text:
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1
    
    return character_count

def sort_on(items):
    return items["num"]

def sort_result(result:dict[str, int]) -> list:
    temp_list = []

    for key in result:
        temp_list.append({"char":key, "num":result[key]})
    temp_list.sort(reverse=True, key=sort_on)

    return temp_list

