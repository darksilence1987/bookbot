def main():
    dict = {}
    num_of_words = 0
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        num_of_words = len(file_contents.split())
        file_contents  = file_contents.lower()
        for character in file_contents:
            if character in dict:
                dict[character] += 1
            else:
                dict[character] = 1

    print_data(dict, num_of_words)

def print_data(dict, word_count):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    print("")
    for char in sort_data(dict):
        print(f"The '{char[1]}' character was found {char[0]} times")  
    print("--- End report ---")

def sort_data(dict):
    char_list = []
    for char, count in dict.items():
        if char.isalpha():
            char_list.append((count, char))
    char_list.sort(reverse=True)
    return char_list

main()