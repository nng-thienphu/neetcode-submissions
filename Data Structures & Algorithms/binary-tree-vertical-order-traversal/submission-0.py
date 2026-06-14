# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # KEY INSIGHTS 1: 
    # create a hashmap, where columns is key, and value is node
    # columns can be negative as it follow node = node.left then col = col - 1

    # KEY INSIGHT 2: 
    # need to store row value as well, since we need to decide the order of node
    # in the same column
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        hashmap = defaultdict(list) # {col : {row, node value}}

        # STEP 1. go through the whole tree with dfs pre-order
        def dfs(row, col, node): 
            if not node: 
                return
            
            # STEP 2. while travel through the tree, 
            # assign the value base on the operation
            # value -= 1 when moving to the left
            # value += 1 when moving to the right
            # root -> value = 0
            hashmap[col].append((row, node.val))
            dfs(row+1, col-1, node.left)
            dfs(row+1, col+1, node.right)

        dfs(0,0, root)
        
        # STEP 3. convert the hashmap to result list
        # KEY: need to sort the hashmap here
        result = [] 
        for key in sorted(hashmap): 
            sorted_node = sorted(hashmap[key], key= lambda x: x[0])
            result.append([val for row, val in sorted_node])

        return result
            
            
        