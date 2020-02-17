

slices , type = list(map(int, input("Slices and Type:").split()))
slices_per_type = list(map(int,input("Slices per type:").split()))

selectedIndex = []
selectedValue = []
solIndex = []
solValue = []

size_of_problem = type
start_index = size_of_problem

sum = 0
max_sum = 0

while ((len(selectedIndex)>0 and selectedIndex[0] != 0) or len(selectedIndex) == 0):
    start_index = start_index - 1

    for i in range(start_index, -1, -1):
        current_slice = slices_per_type[i]
        temp = sum + current_slice
        if (temp == slices):
            sum = temp
            selectedIndex.append(i)
            selectedValue.append(current_slice)
            break
        elif (temp > slices):
            continue
        elif (temp < slices):
            sum = temp
            selectedIndex.append(i)
            selectedValue.append(current_slice)
    if (max_sum < sum):
        max_sum = sum
        solIndex = []
        solValue = []

        for y in selectedIndex:
            solIndex.append(y)
        for y in selectedValue:
            solValue.append(y)

    if (max_sum == slices):
        break
    if (len(selectedValue) != 0):
        last_val = selectedValue.pop()
        sum = sum - last_val
    if (len(selectedIndex) != 0):
        last_index = selectedIndex.pop()
        start_index = last_index
    if((len(selectedIndex) == 0 and (start_index == 0))):
        break
print("Max sum:",max_sum)
#print(solIndex[::-1]) Printing for big inputs = mayhem
