from stats import get_num_words
from stats import get_num_chars
from stats import sorted_char_count



def main():
    message = f"""
    ============ BOOKBOT ============
    Analyzing book found at books/frankenstein.txt...
    ----------- Word Count ----------
    Found {get_num_words()} total words
    --------- Character Count -------
    {(sorted_char_count(get_num_chars()))}

    """
    print(message)
main()
