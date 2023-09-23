def main():
    book_path = "./books/frankenstein.txt"
    text = read_book(book_path)
    words = count_words(text)
    letters = count_letters(text)
    report = get_report(words, letters)
    print(report)

def read_book(book_path):
    with open(book_path) as f:
        file_contents = f.read()
        return file_contents

def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    non_duplicate_letters = text.lower()
    letters_dict = {}
    for letter in non_duplicate_letters:
        if letter in letters_dict:
            letters_dict[letter] += 1
        else:
            letters_dict[letter] = 1
    return letters_dict

def get_report(words, letters):
    chars_data = ""
    sorted_list = []

    for letter in letters:
        if not letter.isalpha():
            continue
        sorted_list.append(letters[letter])

    sorted_list.sort(reverse=True)

    for char_count in sorted_list:
        for key, value in letters.items():
            if value == char_count:
                char = key
                char_data = f"The '{char}' character was found {char_count} times\n"
                chars_data += char_data

    return f"--- Begin report of books/frankenstein.txt --- \n{words} words found in the document \n\n{chars_data}\n--- End report ---"



main()
