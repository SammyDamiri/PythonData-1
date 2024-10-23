#!/usr/bin/env python3

def transform(s1, s2):
    L1 = s1.split()
    L2 = s2.split()
    zipped = zip(map(int,L1), map(int,L2))
    return [i*j for i,j in zipped]

def main():
    s1 = "1 5 3" 
    s2 = "2 6 -1"
    print(transform(s1, s2))

if __name__ == "__main__":
    main()
