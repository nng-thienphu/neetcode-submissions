class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        result = []     # keep all legit word in matrix 
        rows = len(board) 
        cols = len(board[0])

        # KEY CODE TECHNIQUE: 1. Build the trie from the words list, not the board
        #    This is the thing we will be consulting while running dfs 
        # root = {
            #   'b': {
            #     'a': {
            #       'c': {
            #         'k': {
            #           '#': 'back'
            #         }
            #       }
            #     }
            #   }
            # }
        # then if we need to insert the word "backend" 
        # root = {
            #   'b': {
            #     'a': {
            #       'c': {
            #         'k': {
            #           '#': 'back',        # ← still here, untouched
            #           'e': {
            #             'n': {
            #               'd': {
            #                 '#': 'backend'
            #               }
            #             }
            #           }
            #         }
            #       }
            #     }
            #   }
            # }
        root = {}          # this is the self.children in Trie class 
        for word in words: 
            node = root    # node = dictionary {}
            # descend into it
            for ch in word: 
                if ch not in node: 
                    node[ch] = {}      
                node = node[ch] # it moves your pointer one level deeper into the trie
            node['#'] = word               

        # 2. DFS from every trie
        for r in range(rows): 
            for c in range(cols): 
                self.dfs(board, r, c, root, result)
        
        return result 

    def dfs(self, board, r, c, node, result): 
        if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) : 
            return
        
        ch = board[r][c] 

        # letter gate (also catches visited cells — see note below)

        if ch not in node: 
            return
        nxt = node[ch]

        # word checked
        if "#" in nxt: 
            result.append(nxt["#"]) 
            del nxt["#"]
        
        # mark visted
        board[r][c] = "#" 
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            self.dfs(board, r+dr, c+dc, nxt, result)
        board[r][c] = ch  
