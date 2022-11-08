def helper(root, pathSum):
    #/ Edge case
    if not root: return 0
    
    # 1. Calc 
    pathSum = pathSum * 10 + root.val
    
    # 2. Base cases 
    if not root.left and not root.right: 
        return pathSum  #/ Root to leaf
    
    # 3. Recursive calls  
    left = helper(root.left, pathSum)
    right = helper(root.right, pathSum)
    
    return left + right