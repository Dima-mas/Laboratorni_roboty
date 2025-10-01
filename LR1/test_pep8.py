# string comment should be split in two lines to fit in the screen better
'''Тестовий файл для ознайомлення з правилами форматування і оформлення коду згідно Python Enhancement Proposals PEP 8 – Style Guide for Python Code.'''

import string
import os # not used
import math, time # import math not used, also SPLIT THE IMPORTS

shift = 3
PI= 3.14 #constant not used anywhere, so why add it?
def PrintTime(x): #the function is not used anywhere
   if x == True:
      print( time.ctime() ) #I guess the spaces are a stylistic choice
   return

def main (): #ouch, why would you do a space there
# many unnesessary spaces, but not an error

    Choice_mode = input("would you like to encode or decode?") #var name starts with capital letter
    word = input("Please enter text")
    LETTERS = string.ascii_letters + string.punctuation + string.digits #var name written in caps, which suggests it's a constant.
                                                                        # however, it changes depending on the user input
    encoded = ""
    if Choice_mode == "encode":
        for letter in word:
            if letter == " ":
                encoded = encoded + " " #not an error, but you can use += instead
            else:
                x = LETTERS.index(letter) + shift
                encoded = encoded + LETTERS[x] #+=
                y=x + 5 #y do you need this var



    if Choice_mode is "decode": #should use == instead of 'is', cus its causing an program error
        for letter in word:
            if letter == " ":
                encoded = encoded+" " #this looks painful. Also, +=
            else:
                x = LETTERS.index(letter)- shift #no consistant spacing between the elements
                encoded=encoded + LETTERS[x] #same here,  and += exists
                y= x - 5 #like really what purpose it serves

    print(encoded)
    print(Word) #bro, even the program tells you to fix yourself 👈🤣.
    #inconsistent variable name, so no proper compilation



if __name__ == '__main__':
#why the space

    main()
