# Read contents of frankenstein.txt
import string

with open('books/frankenstein.txt') as frankenstein:
    file_contents = frankenstein.read()
    # print(file_contents)

    def get_num_words(text: str) -> int:
        """
        Get string and returns number of words within that string.
        :param text             str
        :return num_words       int
        """
        num_words = len(text.split())
#        print(num_words)
        return num_words

    # Call function to get num of words in Frankstein the book
    frankenstein_num_words = get_num_words(file_contents)

    # Define function that returns number of occurence for each character in the provided text
    def get_char_num(text: str) -> dict:
        # Convert input to lowercase to avoid duplicated
        lower_case_text = text.lower()

        # Generate dict with entire english alphabet as keys and count of all those characters (from the provided text input) as value for that dict
        text_char_count = dict.fromkeys(string.ascii_lowercase, 0)
        characters = list(string.ascii_lowercase)

        for char in characters:
            char_count = lower_case_text.count(char)
            text_char_count[char] = char_count

#        print(text_char_count)
        return text_char_count

    # Call the get_char_num function to return a dict with count of each character in Frankenstein
    frankenstein_char_count = get_char_num(file_contents)

# Convert the the dictionary with the char counts to a list of tuples
list_items = list(frankenstein_char_count.items())

# Print the Report with the counts
for item in list_items:
    # print(item)
    char = item[0]
    count = item[1]
    print(f"The '{char}' character was found {count} times")
