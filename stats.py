def word_count(text):
    words = text.split()
    counter = 0
    for word in words:
        counter += 1
    return counter

def character_count(text):
    characters = {}
    words = text.split()
    for word in words:
        for char in word:
            char = char.lower()
            if char in characters:
                characters[char] += 1
            else:
                characters[char] = 1
    return characters

def sort_on(dict):
    return dict["num"]

def sort_dict(char_dict):
    char_dict_list = []
    for char, num in char_dict.items():
        char_dict_list.append({"char": char, "num": num})
    char_dict_list.sort(reverse=True, key=sort_on)
    return char_dict_list
