"""
https://leetcode.com/problems/lfu-cache/
"""

class Node:
    def __init__(self, value, count):
        self.val=value
        self.count=count

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_count = None
        self.key_nodes = {}
        self.count_nodes = defaultdict(OrderedDict)
        

    def get(self, key: int) -> int:
        if key not in self.key_nodes:
            return -1
        
        node = self.key_nodes[key]
        
        del self.count_nodes[node.count][key]
        
        node.count+=1
        self.count_nodes[node.count][key] = node
        
        if not self.count_nodes[self.min_count]:
            self.min_count+=1
        
        
        
        return node.val

    def put(self, key: int, value: int) -> None:
        if not self.capacity:
            return
        
        if key in self.key_nodes:
            
            self.key_nodes[key].val = value
            
            self.get(key)
            return
            
        if len(self.key_nodes) == self.capacity:
            k,_ = self.count_nodes[self.min_count].popitem(last=False)
            del self.key_nodes[k]
        
        node = Node(value,1)
        self.key_nodes[key] = node
        self.count_nodes[1][key] = node
        self.min_count=1
        
            
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)