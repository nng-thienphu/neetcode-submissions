class PrefixNode: 
    # KEY: 
    # The dict lets each node point to several possible next letters, 
    #   so a word becomes a path through a branching tree
    # 
    # node1.children = { "p": node2, "x": node6 }
    def __init__(self): 
        self.children = {} 
        self.word = False

class PrefixTree:
    def __init__(self):
        # KEY: the starting node always gonna be DUMMY NODE
        self.root = PrefixNode() 
    
    # Key: word's boolean value represents whether the word ends at a TrieNode
    # Key: 
        # moving node in linked list: node = node.next
        # moving node in prefix tree: prefixNode = prefixNode.children[c] -> run this for loop
    def insert(self, word: str) -> None:
        curr = self.root 
        for c in word: 
            if c not in curr.children: 
                curr.children[c] = PrefixNode()
            
            curr = curr.children[c]
        curr.word = True  # True = End here 

    # Wrong assumption: 
    # search doesn't ask "does this letter appear somewhere in the tree?" It asks "does a complete word equal to this exist, starting from the root?" 
    def search(self, word: str) -> bool:
        curr = self.root 
        for c in word: 
            if c not in curr.children : 
                return False
            curr = curr.children[c] 
        
        return curr.word


    def startsWith(self, prefix):
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True
