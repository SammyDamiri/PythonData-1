#!/usr/bin/env python3

def merge(L1, L2):
    MergedList = L1 + L2
    
    for i in range(len(MergedList)):
        for j in range(0, len(MergedList) - i - 1):
            if MergedList[j] > MergedList[j + 1]:
                MergedList[j], MergedList[j + 1] = MergedList[j + 1], MergedList[j]
        
    return MergedList

def main():
    l1 = [2,4,5,8,11,1,2]
    l2 = [3,6,7,9,12]
    print(merge(l1,l2))

if __name__ == "__main__":
    main()
