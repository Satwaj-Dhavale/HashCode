def solution(slices, slices_per_type):

    selectedIndex = []
    selectedValue = []
    solIndex = []

    size_of_problem = len(slices_per_type)
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
    return(solIndex[::-1])

def write_output(file):
    input_file = open(input_directory + file + '.in', 'r')
    firstline = input_file.readline()
    secondline = input_file.readline()
    input_file.close()

    slices, type = list(map(int, firstline.split()))
    slices_per_type = list(map(int, secondline.split()))

    output = solution(slices, slices_per_type)

    output_string = ""
    for l in output:
        output_string = output_string + str(l) + " "
    print(output_string)

    output_file = open(output_directory + file + '.out', "w")
    output_file.write(str(len(output)) + "\n")
    output_file.write(output_string)
    output_file.close()

if __name__=='__main__':
    input_directory = "C:\HashCode\Input\\"
    output_directory = "C:\HashCode\Output\\"
    filename = ['a_example', 'b_small', 'c_medium', 'd_quite_big', 'e_also_big']
    for file in filename:
        write_output(file)
