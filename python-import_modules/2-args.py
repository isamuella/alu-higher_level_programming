#!/usr/bin/python3

from sys import argv
if __name__ == "__main__":
    arg_num = len(argv)-1
    if arg_num == 0:
    print("{} arguments.".format(arg_num))
    elif arg_num == 1:
        print("{} arguments:".format(arg_num))
    else:
        print("{} argumrnts:".format(arg_num))
        
    for num in range(1, len(argv)):
        print("{}: {}".format(num, argv[num]))
