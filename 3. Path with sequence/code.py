def helper(root, arr, i):
    #/ Edge cases 
    if not root: return False
    
    # 1. Base cases
    if not root.left and not root.right and i == len(arr) - 1:
        return True     #/ Got the num

    if i == len(arr) or arr[i] != root.val: 
        return False    #/ Breaking cndn
    
    # 2. Normal cases
    left = helper(root.left, arr, i+1)
    right = helper(root.right, arr, i+1)
    
    return left or right