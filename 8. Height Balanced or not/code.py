def solve(root):
    
    def helper(root):
        # 1. Base cases 
        if not root: return 0
        
        # 2. Recursive calls
        lh = helper(root.left)
        rh = helper(root.right)
        
        return 1 + max(lh, rh)
    
    #########################
    ### Main mthd
    if not root: return True
    
    # 1. Cur calc
    lh = helper(root.left)
    rh = helper(root.right)
    
    if abs(lh - rh) > 1: return False
    
    # 2. Recursive calls
    return solve(root.left) and solve(root.right)