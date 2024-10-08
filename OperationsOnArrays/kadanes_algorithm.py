
def kadanes_algorithm(array):

    """
    Given an array of intergers, this function finds the contigous subarray(containing at least one number) which 
    has the maximum sum and return its sum.
    """
    global_max=array[0]
    temp_max=array[0]

    for i in range(1,len(array)):

        temp_max=max(temp_max+array[i],array[i])
        global_max=max(temp_max,global_max)
    
    return global_max

# x=[2, 3, -8, 7, -1, 2, 3]
# print(kadanes_algorithm(x))