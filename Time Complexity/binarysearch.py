def binary_search(arr1, arr2):
    
    """
    This function finds the common elements in two sorted arrays using a binary search method.
    
    Args:
    arr1 (list): The first sorted array
    arr2 (list): The second sorted array
    
    Returns:
    list: A list of common elements found in both arrays
    """
    
    if not arr1 or not arr2:
        return("Null input case, so no output")
    
    common_elements = []
    for i in arr1:
        if binary_search(arr2, i) and i not in common_elements:
            common_elements.append(i)
    return common_elements

array1 = [1, 6, 9, 10, 11, 21]
array2 = [2, 6, 9, 11, 17, 21]


print("Binary search method:", binary_search(array1, array2))
