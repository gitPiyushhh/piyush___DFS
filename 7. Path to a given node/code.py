def helper(root, target, ds):
    # 1. Base cases
    if not root: return False
    
    # 2. Chk found {breaking cndn}
    if root.val == target: return True
    
    # 3. Create ds
    ds.append(root.val)
    
    # 4. Recursive calls
    left = helper(root.left, target, ds)
    right = helper(root.right, target, ds)
    
    if left or right: return True
    
    # 5. Backtracking
    ds.pop()
    return False    #/ We cant even find till