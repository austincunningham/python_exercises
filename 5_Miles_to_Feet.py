#!/usr/bin/python3
def Miles_to_Feet(Miles):
    feet = (Miles * 5280)
    print ("%1.0f feet in %1.0f miles" %(feet,Miles))

def main():
    print("Enter number of miles to convert to feet")
    mile = input(">")
    Miles_to_Feet(mile)

if __name__=='__main__':
    main()
