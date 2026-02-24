"""


"""

def all_subsets(arr):
    result = []
    def calculate_subsets(index, path):
        print(path, result)
        if index == len(arr):
            result.append(path.copy())
            return
        
        path.append(arr[index])
        calculate_subsets(index + 1, path)
        path.pop()
        calculate_subsets(index + 1, path)

        return
    calculate_subsets(0,[])
    return result

arr = ['x', 'y', 'z']
print(all_subsets(arr))