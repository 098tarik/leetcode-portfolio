def sort_by_frequency(word: str):
    if len(word) == 0:
        return []
    elif len(word) == 1:
        return [word[0]]
    

    freq_map = dict()
    for idx in range(len(word)):
        if word[idx] not in freq_map:
            freq_map[word[idx]] = 0
        freq_map[word[idx]] += 1
    
    sorted_tuples = []
    result = []
    for key, value in freq_map.items():
        sorted_tuples.append((key,value))
    
    sorted_tuples = sorted(sorted_tuples, key=lambda x: (-x[1], x[0]))

    for idx in range(len(sorted_tuples)):
        result.append(sorted_tuples[idx][0])

    return result

word = ""
result = sort_by_frequency(word)

print(result)