def rotate(array, npos):
    """
    Rotates the provided array by the number of position specified in npos.
    """
    if len(array):
        # ensure npos is positive & greater than array length
        npos = abs(npos) % len(array)
        if npos:
            chunk = array[-npos:]
            del array[-npos:]

            chunk.reverse()
            for x in chunk:
                array.insert(o, x)
    return array
