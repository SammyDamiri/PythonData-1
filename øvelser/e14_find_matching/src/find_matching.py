#!/usr/bin/env python3

def find_matching(L, pattern):
    l = []
    for i, w in enumerate(L):
        if pattern in w:
            # l.append(i)
            l += [i] # Mere street
    return l

def main():
    L = ["sensitive", "engine", "rubbish", "comment"]
    print(find_matching(L, "en"))

if __name__ == "__main__":
    main()
