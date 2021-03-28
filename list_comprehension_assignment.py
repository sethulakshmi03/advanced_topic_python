import os
import sys
import time

def full_pathfull_path(dir):
    dir_list = os.listdir(dir)
    l = [os.path.abspath(d) for d in dir_list]
    print(l)
    time.sleep(3)

def items(dir):
    dir_list = os.listdir(dir)
    print(dir_list)
    time.sleep(3)

def print_jpg_png(dir):
    dir_list = os.listdir(dir)
    l = [d for d in dir_list if ".jpg" in str(d) or ".png" in str(d)]
    print(l)
    time.sleep(3)

def num_of_space(string):
    print("Number of spaces in \""+string+"\"",string.count(" "))
    time.sleep(3)

def remove_vowels(string):
    s = ''
    for i in ['a','e','i','o','u']:
        string = string.replace(i,'')
    print(string)
    time.sleep(3)

def find_less_than_4_letters(string):
    l = [w for w in string.split() if len(w)<4]
    print(l)
    time.sleep(3)

def print_word_length(string):
    l = [{w:len(w)} for w in string.split()]
    print(l)
    time.sleep(3)

def main():

    while(1):
        option = str(input("1.printing a list of the full path to items in a directory\n"
              "2.printing a list of the full path to items in a directory (excluding directories)\n"
              "3.printing the list of all .jpg and .png files in a directory\n"
              "4.printing the number of spaces in a string\n"
              "5.removing vowels from a string and printing it\n"
              "6.printing all of the words in a string that have less than 4 letters\n"
              "7.printing length of each word in a sentence\n"
                           "8. exit\n"))
        if option == '1':
            s = str(input("enter directory"))
            full_pathfull_path(s)
        elif option == '2':
            s = str(input("enter directory"))
            items(s)
        elif option == '3':
            s = str(input("enter directory"))
            print_jpg_png(s)
        elif option == '4':
            s = str(input("enter a string"))
            num_of_space(s)
        elif option == '5':
            s = str(input("enter a string"))
            remove_vowels(s)
        elif option == '6':
            s = str(input("enter a string"))
            find_less_than_4_letters(s)
        elif option == '7':
            s = str(input("enter a string"))
            print_word_length(s)
        elif option == '8':
            sys.exit()
        else:
            print("INVALID OPTION!!!!!!!!")


if __name__ == "__main__":
    main()