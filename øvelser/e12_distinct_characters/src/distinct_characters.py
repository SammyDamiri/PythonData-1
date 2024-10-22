#!/usr/bin/env python3

def distinct_characters(L):
    D = {}
    for word in L:
       D[word] = len(set(word))
    return D
   

def main():
    print(distinct_characters(["check", "look", "try", "pop"]))

if __name__ == "__main__":
    main()
