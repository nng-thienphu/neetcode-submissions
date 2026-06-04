class TrieNode: 
    # self.children -> represent the linkedlist to connect with children node 
    # root.children      = {'d': <d node>}
    #    d_node.children = {'a': <a node>}
    #       a_node.children = {'y': <y node>}
    #          y_node.children = {}        (empty — nothing after y)
    def __init__(self): 
        self.children = {}  # this represent the node = node.next
        self.last_node = False 

class Solution:
    # KEY: insert all words into one shared trie, 
    # then walk the single un-forked stem until the first fork or word-end
    def __init__(self): 
        self.trieTree = TrieNode() 

    def longestCommonPrefix(self, strs: List[str]) -> str:
        for word in strs: 
            self.insert(word)
            
        node = self.trieTree
        prefix = []
        while len(node.children) == 1 and not node.last_node: 
            ch = list(node.children)[0]
            prefix.append(ch)
            node = node.children[ch] 
        
        return "".join(prefix)

    def insert(self, word): 
        node = self.trieTree 
        
        for ch in word: 
            if ch not in node.children: 
                node.children[ch] = TrieNode()  # KEY: simply trienode-ize 
            node = node.children[ch]       

        node.last_node = True  


