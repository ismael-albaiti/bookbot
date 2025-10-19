def main():
    book = get_book_text("./books/frankenstein.txt")
    num_words = get_text_wordcount(book)
    print(f"Found {num_words} total words")
<<<<<<< Updated upstream
=======
    print("--------- Charact"./books/frankenstein.txt"er Count -------")
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
>>>>>>> Stashed changes


def get_book_text(path):
    with open(path) as book:
        return book.read()


def get_text_wordcount(text: str):
    return len(text.split())


if __name__ == "__main__":
    main()
