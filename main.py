from stats import character_occurneces, get_num_words, sorted_dictionarys
import sys


def main():
    args = sys.argv
    if len(args) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = args[1]
    book = get_book_text(book_path)
    num_words = get_num_words(book)
    num_chars = character_occurneces(book)
    report = sorted_dictionarys(num_chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    print(sorted_report(report))
    print("============= END ===============")


def sorted_report(list: list):
    report = ""
    for item in list:
        char: str = item["char"]
        if not char.isalpha():
            continue
        report += f"{char}: {item["num"]}\n"

    return report


def get_book_text(path):
    with open(path) as book:
        return book.read()


if __name__ == "__main__":
    main()
