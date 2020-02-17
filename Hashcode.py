def solution(slices, slices_per_type):



M = slices
N = len(slices_per_type)

selectedIndex = []
selectedValue = []
solIndex = []

start_index = -1
S = 0
max_sum = 0

#start_index 
while ((len(selectedIndex)>0 and selectedIndex[0] != N-1) or len(selectedIndex) == 0):
    start_index = start_index + 1
    
    for i in range(start_index,N):
        current_slice = slices_per_type[i]
        #add the slice into temp
        temp = S + current_slice

        #check temp for following 3 conditions
        if (temp == M):
            S = temp
            selectedIndex.append(i)
            selectedValue.append(current_slice)
            break
        elif (temp > M):
            continue
        elif (temp < M):
            S = temp
            selectedIndex.append(i)
            selectedValue.append(current_slice)
   
    if (max_sum < S):
        max_sum = S
        #clear the list
        solIndex = []
        solValue = []

        for i in selectedIndex:
            solIndex.append(i)
        for v in selectedValue:
            solValue.append(v)

    if (max_sum == M):
        break
    
    if (len(selectedValue) != 0):
        last_val = selectedValue.pop()
        S = S - last_val
        
    if (len(selectedIndex) != 0):
        last_index = selectedIndex.pop()
        start_index = last_index
   
    if((len(selectedIndex) == 0 and (start_index == N-1))):
        break
    
    return(solIndex) 

 
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
