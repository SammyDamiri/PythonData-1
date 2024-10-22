#!/usr/bin/env python3

def interleave(*lists):
    flattenedList = []
    for tup in zip(*lists):
        flattenedList.extend(tup)
    return flattenedList

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()
