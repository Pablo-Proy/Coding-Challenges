
def array_leaders(array):

    """
    Given an array, this function prints all the Leaders in the array.
    An element is a Leader if it is greater than all the elements to its right side. The rightmost element is always a leader.
    """
    leaders=[array[-1]]
    maximum=array[-1]

    for i in range(2,len(array)):

        if array[-i]>maximum:

            leaders.append(array[-i])
            maximum=array[-i]
    
    leaders.reverse()

    return leaders