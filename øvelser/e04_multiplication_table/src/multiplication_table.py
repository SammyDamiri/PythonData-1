#!/usr/bin/env python3


def main():
    for i in range(1, 11):
        for j in range(1, 11):
            # print('{:4d}'.format(i*j), end="")
            print(f"{i*j:4d}", end="") # Søren synes det er pænere. Maybe he is right :-D
        print()

if __name__ == "__main__":
    main()
