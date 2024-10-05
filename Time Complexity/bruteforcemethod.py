def find_common_elements_brute_force(arr1, arr2):

     
    if not arr1 or not arr2:
        return("Null input case, so no output")
    
    common_elements = []
    for i in arr1:
        for j in arr2:
            if i == j and i not in common_elements:
                common_elements.append(i)
    return common_elements

array1 = [1, 6, 9, 10, 11, 21]
array2 = [2, 6, 9, 11, 17, 21]

print("Brute-force method:", find_common_elements_brute_force(array1, array2))

