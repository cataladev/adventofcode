import fileinput

filename = "input.txt"

def main():
    list1 = []
    list2 = []
    for line in fileinput.input(files=filename):
        lists = line.split()
        list1.append(int(lists[0]))
        list2.append(int(lists[1]))
    
    list1.sort()
    list2.sort()

    totalDistance = 0
    for i in range(0, len(list1)):
        totalDistance += abs(list1[i]-list2[i])
    
    print(totalDistance)

main()