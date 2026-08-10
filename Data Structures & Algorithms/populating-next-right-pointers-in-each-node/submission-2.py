class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        q = deque([root])
        while q:
            width = len(q)
            for i in range(width):
                node = q.popleft()
                if i < width - 1:        # not the last of this level
                    node.next = q[0]     # peek: next same-level node is at the front
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return root