#!/usr/bin/env python3

import math

def triangle():
    b = float(input("Give base of the triangle: "))
    h = float(input("Give height of the triangle: "))
    return f"{0.5 * h * b:.6f}"

def rectangle():
    w = float(input("Give width of the triangle: "))
    h = float(input("Give height of the triangle: "))
    return f"{w * h:.6f}"

def circle():
    r = float(input("Give radius of the circle: "))
    return f"{math.pi * r ** 2:.6f}"

def main():
    while True:
        selection = input("Choose a shape (triangle, rectangle, circle): ").lower()
        if(selection == ""):
            break
        if(selection == "triangle"):
            print(f"The area is {triangle()}")
        elif(selection == "rectangle"):
            print(f"The area is {rectangle()}")
        elif(selection == "circle"):
            print(f"The area is {circle()}")
        else:
            print("Unknown shape!")

if __name__ == "__main__":
    main()
