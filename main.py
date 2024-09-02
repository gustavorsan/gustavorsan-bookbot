def main():
    path_to_file = "books/frankenstein.txt"
    text = get_book_text(path_to_file)
    num_words = get_num_words(text)
    frequency = get_char_frequency(text)
    sorted_dict = sort_dict(frequency)

    print(f"--- Begin report of {path_to_file} ---")
    print(f"{num_words} words found in the document")
    print()

    for key, value in sorted_dict.items():
        if key.isalpha():
            print("The "+key+" character was found "+str(value)+" times")   
    
    print(f"{num_words} words found in the document")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_frequency(text):
    words = text.split()
    my_dict = {}
    for word in words:
        for char in word.lower():
            if char in my_dict:
                my_dict[char] += 1
            else:
                my_dict[char] = 0
    
    return my_dict;

def sort_dict(items):
    items_list = list(items.items())

    items_list.sort(key=lambda item: item[1])
    
    sorted_dict = dict(items_list)
    
    return sorted_dict



main()