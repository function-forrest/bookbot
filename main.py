def count_words(book):
    words = book.split()
    return len(words)


def sort_on(dict):
    return dict["num"]


def create_report():
    print("--- Begin report of books/frankenstein.txt ---")
    with open("books/frankenstein.txt", "r") as file:
        text = file.read()

    words_count = count_words(text)
    print(f"{words_count} words found in the document")
    occurrences = count_letters(text)
    occurrences.sort(reverse=True, key=sort_on)
    for pair in occurrences:
        if pair["letter"].isalpha():
            print(f"The {pair['letter']} character was found {pair['num']} times")
    print("--- End report ---")


def count_letters(text):
    letters = {}

    lower_case_letters = [letter.lower() for letter in text]

    for letter in lower_case_letters:
        if letter not in letters:
            letters[letter] = lower_case_letters.count(letter)

    list_of_dicts = [
        {"letter": key, "num": int(value)} for key, value in letters.items()
    ]
    return list_of_dicts


def main():
    create_report()


if __name__ == "__main__":
    main()
