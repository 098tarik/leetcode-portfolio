
def index_of(s, t):
    if not t or not s or len(t) > len(s):
        return -1
    
    for i in range(len(s) - len(t) + 1):
        match = True
        for j in range(len(t)):
            if s[i + j] != t[j]:
                match = False
                break
        if match:
            return i
    
    return -1

s = "needle in a haystack"
t = "a"

result = index_of(s,t)
print(result)
