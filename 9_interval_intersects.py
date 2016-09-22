#!/usr/bin/python3
def interval_intersects(x,y,a,b):
    if (not ((b <= x) or (y <= a))):
        print("true")
    else:
        print("false")

def main():
    a = 1
    b = 6
    x = 5
    y = 65
    interval_intersects(x,y,a,b)

if __name__=='__main__':
    main()
