class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:
    # WRONG ASSUMPTION:
    # I thought I could special-case the "." by stepping into the next child and
    # continuing with a single loop. But a "." can match several children, and only
    # some may lead to a full match — so I can't commit to one. I need to try each
    # child, and if a branch dead-ends, back up and try the next. That "try a branch,
    # fail, retreat, try another" is backtracking, which needs recursion — a single
    # forward loop can't do it.

    # KEY INSIGHT:
    # DFS + backtracking only kicks in at a ".". A normal letter has exactly one path,
    # so it just commits. The "." is the only fork — loop over every child, return True
    # if ANY recursive call succeeds, and only return False after they all fail.

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_word = True

    def search(self, word: str) -> bool:
        def dfs(index, node):
            if index == len(word):
                return node.is_word   # search: did a full word END here?
                # return True is wrong — that's startsWith (path exists != word ends)

            c = word[index]

            if c == ".":
                for child in node.children.values():   # try every child
                    if dfs(index + 1, child):
                        return True
                return False
            else:
                if c not in node.children:
                    return False
                return dfs(index + 1, node.children[c])

        return dfs(0, self.root)