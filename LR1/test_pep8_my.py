
'''Тестовий файл для ознайомлення з правилами форматування і оформлення коду
згідно Python Enhancement Proposals PEP 8 – Style Guide for Python Code.'''
import string

SHIFT = 3

def main():
    choice_mode = input("would you like to encode or decode?")
    word = input("Please enter text")
    letters = string.ascii_letters + string.punctuation + string.digits
    encoded = ""

    if choice_mode == "encode":
        for letter in word:
            if letter == " ":
                encoded += " "
            else:
                x = letters.index(letter) + SHIFT
                encoded += letters[x]
    
    elif choice_mode == "decode":
        for letter in word:
            if letter == " ":
                encoded += " "
            else:
                x = letters.index(letter) - SHIFT
                encoded += letters[x] #same here,  and += exists
    else:
        print("not a variant you can choose, sorry ¯\_(ツ)_/¯")

    print(encoded)
    print(word)


if __name__ == '__main__':
    main()