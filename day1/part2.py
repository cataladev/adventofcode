import fileinput

filename = "input.txt"

def main():
    list1 = []
    list2 = {}
    for line in fileinput.input(files=filename):
        lists = line.split()
        list1.append(int(lists[0]))

        list2val = int(lists[1])
        
        if list2val in list2:
            list2[list2val] += 1
        else:
            list2[list2val] = 1
    
    similarityScore = 0

    for val in list1:
        if val in list2:
            similarityScore += val * list2[val]
    
    print(similarityScore)

main()