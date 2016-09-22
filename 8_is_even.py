#!/usr/bin/python3
def is_even(number):
    if number % 2 == 0:
        print("even")
    else:
        print("odd")

def main():
    print ("Enter a number to test for odd/even")
    number = input(">")
    is_even(number)

if __name__=='__main__':
    main()
