from stats import word_count, character_count, sort_dict
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

# Takes the file path as input and returns the contents of the book as a string.
def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


def main():
    text = get_book_text(sys.argv[1])
    word_num = word_count(text)
    char_dict = sort_dict(character_count(text))

    # Print the report
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_num} total words")
    print("--------- Character Count -------")

    for final_dict in char_dict:
        char = final_dict["char"]
        count = final_dict["num"]
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")
main()
