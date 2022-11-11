dia = 0

def helper(root):
    # 1. Base cases
    if not root: return 0
    
    # 2. Recursive calls
    lh = helper(root.left)
    rh = helper(root.right)
    
    # Code crux #
    dia = max(dia, lh + rh)     #/Inclase we have to calc vertices then we have to take the (1+lh+rh)
    
    return 1 + max(lh, rh)