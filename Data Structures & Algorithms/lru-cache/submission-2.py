class Node: 
    def __init__(self, key, value): 
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    # KEY: hashmap + doubly linked list, hashmap maps key to node, doubly linked list maintains recency, dummy sentinels eliminate edge cases
    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.hashmap = {}

        self.head = Node(0,0)
        self.tail = Node(0,0) 
        self.head.next = self.tail 
        self.tail.prev = self.head 

    def _remove(self, node): 
        # KEY: Don't need to handle edge case because we have dummy node already 
        node.prev.next = node.next 
        node.next.prev = node.prev 
    
    def _insert_at_head(self, node): 
        node.prev = self.head 
        node.next = self.head.next 

        self.head.next.prev = node 
        self.head.next = node  

    def get(self, key: int) -> int: 
        # step 1: check if this exist, else return -1
        if key not in self.hashmap: 
            return -1 

        # step 2: O(1) calling node instead of checking linkedlist traversal
        #.       by calling hashmap
        node = self.hashmap[key] 

        # step 3: remove + re-inserted at head 
        self._remove(node) 
        self._insert_at_head(node) 

        return node.value
        
    def put(self, key: int, value: int) -> None:
        # step 1: check if key exist 
        #.   if exist: update value -> then move to head
        #.   else: add NEW value
        if key in self.hashmap: 
            node = self.hashmap[key]
            node.value = value
            self._remove(node)
            self._insert_at_head(node)
            return 

        # else 
        # step 2: if full capcaity, remove tail and then add to head
        # init node tree
        node = Node(key, value)

        if len(self.hashmap) == self.capacity: 
            lru_node = self.tail.prev
            self._remove(lru_node) 
            del self.hashmap[lru_node.key]
 
        # step 3: if not, then add to head
        new_node = Node(key, value) 
        self._insert_at_head(new_node) 
        self.hashmap[key] = new_node
