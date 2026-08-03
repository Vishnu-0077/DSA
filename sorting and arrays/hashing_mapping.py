def Frequency(array,n):
    count_array = {}
    for i in range(n):
        if array[i] not in count_array:
            count_array[array[i]]=1
        else:
            count_array[array[i]]=count_array[array[i]]+1
    return count_array

print(Frequency([5,10,20,5,10,15,5,5],8))

# if want to print max and min frequesncy
def max_min_frequency(array, n):
    count_array = Frequency(array, n)
    max_freq = max(count_array.values())
    min_freq = min(count_array.values())
    max_elements = [k for k, v in count_array.items() if v == max_freq]
    min_elements = [k for k, v in count_array.items() if v == min_freq]
    
    return {
        "max_frequency": (max_elements, max_freq),
        "min_frequency": (min_elements, min_freq)
    }
print(max_min_frequency([5,10,20,5,10,15,5,5], 8))