# function to create a frequency list
def create_freq_list(arr):
    # create an empty list to store elements and their counts
    freq_list = []

    # iterate through the array
    for i in arr:
        # check if the element is already in the list
        found = False
        for j in freq_list:
            if j[0] == i:
                # increment the count if element is already in the list
                j[1] += 1
                found = True
                break
        # add the element to the list if it's not already in the list
        if not found:
            freq_list.append([i, 1])

    # remove elements with repeating values
    freq_list = [i for i in freq_list if i[1] == 1]

    return freq_list

# test the function
arr = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 9,8, 5]
print("Original list: ", arr)
print("Frequency list: ", create_freq_list(arr))





