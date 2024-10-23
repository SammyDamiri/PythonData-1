#!/usr/bin/env python3

class Prepend(object):
    # Add the methods of the class here

    def __init__(self, start):
        self.start = start

    def write(self, text):
        print(self.start + text)

def main():
    pass

if __name__ == "__main__":
    p = Prepend("+++ ")
    p.write("WazUp")
    main()
