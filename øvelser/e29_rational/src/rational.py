#!/usr/bin/env python3
from math import gcd

class Rational(object):
    def __init__(self, t, n):
        self.t = t
        self.n = n

    def __str__(self):
        cd = gcd(self.t, self.n)
        return f"{self.t // cd}/{self.n // cd}" 
    
    def __add__(self, r):
        return Rational(self.t * r.n + r.t * self.n, self.n * r.n)
    
    def __sub__(self, r):
        return Rational(self.t * r.n - r.t * self.n, self.n * r.n)
    
    def __mul__(self, r):
        return Rational(self.t * r.t, self.n * r.n)
           
    def __truediv__(self, r):
        return Rational(self.t * r.n, self.n * r.t)
    
    def __eq__(self, r):
        return self.t * r.n == self.n * r.t
        
    def __gt__(self, r):
        return self.t * r.n > self.n * r.t

    def __lt__(self, r):
        return self.t * r.n < self.n * r.t
    
def main():
    r1=Rational(1,8)
    r2=Rational(1,4)
    print(r1)
    print(r2)
    print(r1*r2)
    print(r1/r2)
    print(r1+r2)
    print(r1-r2)
    print(Rational(1,2) == Rational(2,4))
    print(Rational(1,2) > Rational(2,4))
    print(Rational(1,2) < Rational(2,4))

if __name__ == "__main__":
    main()
