def get_books_text(path_to_book):
    
    with open(path_to_book, 'r') as f:
        file_contents = f.read()

    return file_contents

def get_num_words(path_to_book):
    book_to_analyze = get_books_text(path_to_book)

    list_of_words = book_to_analyze.split()
    #number_of_words = list_of_words.count()

    return(len(list_of_words))

def get_num_chars(path_to_book):
    
    dict_of_chars = {}
    string_of_book = get_books_text(path_to_book)
    
    chars_list = [char for char in string_of_book]
    

    for item in chars_list:
        dict_of_chars[item.lower()] = dict_of_chars.get(item.lower(), 0) + 1
     
    return(dict_of_chars)

def sort_on(items):
    return items["num"]

def sorted_char_count(my_dict):
    list_of_char_count = []

    for key, value in my_dict.items():
        list_of_char_count.append({"char": key, "num": value})
    
    list_of_char_count.sort(reverse=True, key=sort_on)

    return(list_of_char_count)








