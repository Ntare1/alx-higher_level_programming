#!/usr/bin/python3
import sys
if __name__ == "__main__":
    y = 0
    for x in range(len(sys.argv) - 1):
        y += int(sys.argv[x + 1])
    print("{}".format(y))
