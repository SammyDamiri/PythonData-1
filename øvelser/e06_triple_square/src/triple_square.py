#!/usr/bin/env python3

def triple(a):
    return a + a + a

def square(a):
    return a**2

def main():
    for i in range(1,11):
        tr = triple(i)
        sq = square(i)
        if(sq > tr):
            break
        print(f"triple({i})=={tr} square({i})=={sq}")


if __name__ == "__main__":
    main()
