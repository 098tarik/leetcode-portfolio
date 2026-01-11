
def check_same_message(arr):

  p1 = 0
  p2 = 0

  if len(arr) == 0:
    return True

  user_1 = [] 
  user_2 = []


  while p1 < len(arr) and p2 < len(arr):
    if arr[p1] == 0 or arr[p1] == 1:
      user_1.append(arr[p1])
    elif len(user_1) > 0 and arr[p1] == 2:
        user_1.pop()
    
    if arr[p2] == 10:
      user_2.append(0)
    elif arr[p2] == 11:
      user_2.append(1)
    elif len(user_2) > 0 and arr[p2] == 12:
      user_2.pop()

    p1 += 1
    p2 += 1
    
  if len(user_1) == len(user_2) and user_1 == user_2:
    return True
  
  return False
  
arr = [1, 11, 0, 10, 2, 12]
if (check_same_message(arr)):
    print("valid")
else: 
    print("invalid")
    