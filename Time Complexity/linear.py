def find_common_elements_linear(arr1, arr2):

    if not arr1 or not arr2:
        return("Null input case, so no output")

    
    common_elements = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            if arr1[i] not in common_elements:
                common_elements.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1
    return common_elements

array1 = [1, 6, 9, 10, 11, 21]
array2 = [2, 6, 9, 11, 17, 21]

print("Linear method:", find_common_elements_linear(array1, array2))
