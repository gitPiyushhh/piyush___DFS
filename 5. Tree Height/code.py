def helper(root):
    # 1. Base cases
    if not root: return 0
    
    # 2. Recursive calls
    lh = helper(root.left)
    rh = helper(root.right)
    
    return 1 + max(lh, rh)