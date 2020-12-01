with open("input1.txt") as input_file:
    arr = []
    for line in input_file:
        arr.append(int(line))

maxi = 2020
print(len(set(arr)))
arr = set(arr)
print(arr)

for i in arr:
    if maxi - i in arr:
        print(i, maxi - i)
        print(i * (maxi - i))

for i in arr:
    for j in arr:
        for k in arr:
            if i + j + k == 2020:
                print(i, j, k)
                print(i * j * k)
