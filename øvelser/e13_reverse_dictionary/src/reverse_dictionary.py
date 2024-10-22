#!/usr/bin/env python3

def reverse_dictionary(d):
    rd ={}
    for key, vL in d.items():
        for w in vL:
            if w in rd:
                rd[w] += [key]
            else:
                rd[w] = [key]
                
    return rd

def main():
    d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    print(reverse_dictionary(d))
    pass

if __name__ == "__main__":
    main()
