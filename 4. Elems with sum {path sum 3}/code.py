res = 0     #/Global variable

def helper(root, temp, target):
    # 1. Base cases
    if not root: return 0
    
    # 2. Normal cases
    temp.append(root.val)
    sm = 0
    
    for i in range(len(temp) - 1, -1, -1):
        sm += temp[i]
        
        if sm == target: 
            res += 1
    
    left = helper(root.left, temp, target)
    right = helper(root.right, temp, target)
    
    temp.pop()      #/ Backtracking step
    return left + right