from stats import get_num_words
from stats import get_num_chars
from stats import sorted_char_count



def main():
    my_list = (sorted_char_count(get_num_chars()))
    

    message = f"""============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {get_num_words()} total words
--------- Character Count -------"""
    print(message)

    for n in my_list:
        char_val, num_val = n.values()
        if char_val.isalpha() is True:
            print(f"{char_val}: {num_val}")
        else:
            continue

main()
