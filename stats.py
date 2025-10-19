def get_book_text(path):
    with open(path) as book:
        return book.read()


def get_num_words(text: str):
    return len(text.split())


def character_occurneces(text: str):
    occurneces_dic = {}
    for c in text:
        char = c.lower()
        if char in occurneces_dic.keys():
            occurneces_dic[char] += 1
        else:
            occurneces_dic[char] = 1
    return occurneces_dic


def sorted_dictionarys(dictionary: dict):
    sorted_list = []
    for item in dictionary:
        sorted_list.append({"char": item, "num": dictionary[item]})

    sorted_list.sort(key=sort_on, reverse=True)
    return sorted_list


def sort_on(items):
    return items["num"]
