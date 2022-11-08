def helper(root, target):
    # 1. Base cases
    if not root: 
        return False    #/ No such path found
    
    
    if root.val == target and not root.left and not root.right:
        return True     #/ Path found
    
    # 2. Normal cases
    left = helper(root.left, target - root.val)
    right = helper(root.right, target - root.val)
    
    return left or right