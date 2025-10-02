def get_books_text(path_to_book):
    
    with open(path_to_book, 'r') as f:
        file_contents = f.read()

    return file_contents

def get_num_words():
    book_to_analyze = get_books_text("./books/frankenstein.txt")

    list_of_words = book_to_analyze.split()
    #number_of_words = list_of_words.count()

    print(f"Found {len(list_of_words)} total words")

def get_num_chars():
    
    dict_of_chars = {}
    string_of_book = get_books_text("./books/frankenstein.txt")
    
    chars_list = [char for char in string_of_book]
    

    for item in chars_list:
        dict_of_chars[item.lower()] = dict_of_chars.get(item.lower(), 0) + 1
     
    print(dict_of_chars)

get_num_chars()

