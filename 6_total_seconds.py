#!/usr/bin/python3
def total_seconds(hours,minutes,seconds):
    totalSeconds= ((hours * 3600) + (minutes * 60) + (seconds))
    print("There are %i seconds in %i hours, %i minutes and %i seconds" %(totalSeconds,hours,minutes,seconds))

def main():
    print("Enter number of Hours ")
    hours = input(">")
    print("Enter number of Minutes ")
    minutes = input(">")
    print("Enter number of Seconds")
    seconds = input(">")
    total_seconds(hours,minutes,seconds)

if __name__=='__main__':
    main()
