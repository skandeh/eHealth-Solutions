def compact(array):
    prev = array[0]
    
    idx = 1
    while (idx < len(array)):
        if prev == array[idx]:
            del array[idx]
        else:
            prev = array[idx]
            idx += 1
    return len(array)
