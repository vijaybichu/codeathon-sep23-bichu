def sort_string_by_frequency(s):
    # Create a dictionary to store the frequency of each character
    freq = {}
    for c in s:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1
    
    # Sort the characters by frequency
    sorted_chars = sorted(freq, key=freq.get, reverse=True)
    
    # Build the sorted string
    sorted_string = ""
    for c in sorted_chars:
        sorted_string += c * freq[c]
    
    return sorted_string
