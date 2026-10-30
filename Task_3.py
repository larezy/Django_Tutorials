def count_words(file_path):
    try:
        # open and read the file content
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Split the content into words using whitespace as the delimiter
        words = content.split()

        # Count the number of words
        word_count = len(words)

        return word_count

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None

    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexception error occurred: {e}")
        return None

def main():
    # Ask the user for the filename/path
    file_path = input("Enter the path of the text file: ")

    # call the function to count words
    result = count_words(file_path)

    # display the result if successful
    if result is not None:
        print(f"The file '{file_path}'contains {result} words.")

if __name__ == "__main__":
    main()