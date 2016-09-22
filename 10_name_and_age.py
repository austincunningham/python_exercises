#!/usr/bin/python3


def name_and_age(name,old):
    if int(old) <= 0:
        print("Error:invalid age")
    else:
        print("%s is %i years old" %(name,int(old)))


def main():
    print ("Enter name")
    name = input(">")
    print(name)
    print ("Enter age")
    old = input(">")
    name_and_age(name,old)

if __name__ == '__main__':
    main()
