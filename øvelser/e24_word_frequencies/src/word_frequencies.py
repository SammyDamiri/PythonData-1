#!/usr/bin/env python3

def word_frequencies(filename):
    wd = {}
    with open(filename, "r", newline="\r\n") as file:
        for line in file:
            words = [w.strip("""!"#$%&'()*,-./:;?@[]_""") for w in line.split()]
            # print(words)
            for w in words:
                if w in wd:
                    wd[w] += 1
                else:
                    wd[w] = 1
           
    return wd

def main():
    fname = r'C:\Users\samza\source\repos\H3_Opgaver\PythonData-1\øvelser\e24_word_frequencies\src\alice.txt'
    wd = word_frequencies(fname)

    wd = dict(sorted(wd.items(), key=lambda i: i[1], reverse=True))

    for w, c in list(wd.items())[:5]:
        print(w, c, sep="\t")

if __name__ == "__main__":
    main()
