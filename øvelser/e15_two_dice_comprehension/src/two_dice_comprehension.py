#!/usr/bin/env python3

def main():
    D = [(a , b) 
         for a in range(1,7) 
         for b in range(1,7) 
         if a + b == 5]
    print(*D, sep="\n")

if __name__ == "__main__":
    main()
