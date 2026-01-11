
def split(s,c): # beekeeper
    result = []
    current_segment = []
    for index in range(len(s)):
        if s[index] == c:
            result.append(''.join(current_segment)) # b, ""
            current_segment = []
        else:
            current_segment.append(s[index]) # b, 
    result.append(''.join(current_segment))  # Add final segment
    return result

s = "beekeeper needed"
c = "e"
result = split(s,c)
print(result)

