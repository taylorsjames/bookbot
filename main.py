import sys
from stats import get_num_words
from stats import get_num_chars
from stats import sorted_char_count





def main(supplied_path):
    
    path_of_book = supplied_path
    

    my_list = (sorted_char_count(get_num_chars(path_of_book)))
    

    message = f"""============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {get_num_words(path_of_book)} total words
--------- Character Count -------"""
    print(message)

    for n in my_list:
        char_val, num_val = n.values()
        if char_val.isalpha() is True:
            print(f"{char_val}: {num_val}")
        else:
            continue


if len(sys.argv) == 2:
    main(sys.argv[1])
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

