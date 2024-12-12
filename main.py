def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = book_counter(text)
    char_count = count_character(text)
    sorted_chars = organizing_it_up(char_count)
    print(f'--- Begin report of {book_path} ---')
    print(f'{word_count} words found in the document')
    for char_dict in sorted_chars:
        if char_dict['char'].isalpha():
            print(f"The '{char_dict['char']}' character was found {char_dict['num']} times")


def get_book_text(path):
    with open(path) as f:
        return f.read()


def book_counter(book_string):
    book = book_string.split()
    return len(book)

def count_character(characters):
    dict= {}
    characters= characters.lower()
    for character in characters:
    	dict[character]= dict.get(character, 0) + 1
    return dict

def sort_on(dict):
    return dict["num"]

def organizing_it_up(org):
    char_list= []
    for char, count in org.items():
        char_dict= {'char': char, 'num': count}
        char_list.append(char_dict)
    char_list.sort(reverse=True, key=sort_on)
    return char_list



main()
